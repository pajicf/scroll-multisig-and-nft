from brownie import TheNFT, Supersig, network, accounts
import click
import hexbytes
import eth_utils
import eth_abi

def build_nft_mint_multisig_tx(receiver, nft):
    tx_object = {
        "value": 0,
        "target": nft.address,
        "calldata": hexbytes.HexBytes(nft.mint.encode_input(receiver))
    }

    proposal_hash = eth_utils.keccak(
        eth_abi.encode_abi(
           ["address", "bytes", "uint256"],
           [tx_object["target"], tx_object["calldata"], tx_object["value"]]
        )
    )

    tx_object["proposal_hash"] = proposal_hash

    return tx_object

def create_proposal(nft, multisig, multisig_tx, deployer, proposal_id):
    print(f"Creating proposal {proposal_id}")
    multisig.propose(proposal_id, multisig_tx["proposal_hash"], {"from": deployer})
    print(f"Proposal {proposal_id} created")

def approve_proposal(multisig, deployer, proposal_id):
    print(f"Approving proposal {proposal_id}")
    multisig.approve(proposal_id, {"from": deployer})
    print(f"Proposal {proposal_id} approved by {deployer.address}")

def execute_proposal(multisig, multisig_tx, deployer, proposal_id):
    print(f"Executing proposal {proposal_id}")
    multisig.execute(
        proposal_id,
        multisig_tx["target"],
        multisig_tx["calldata"],
        multisig_tx["value"],
        {"from": deployer}
    )
    print(f"Proposal {proposal_id} executed by {deployer.address}")

def main(nftAddress, multisigAddress, proposal_id = 0):
    print(f"You are using the '{network.show_active()}' network")
    deployer = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'deployer' [{deployer.address}]")

    nft = TheNFT.at(nftAddress)
    multisig = Supersig.at(multisigAddress)

    multisig_tx = build_nft_mint_multisig_tx(deployer.address, nft)

    create_proposal(nft, multisig, multisig_tx, deployer, proposal_id)
    approve_proposal(multisig, deployer, proposal_id)
    execute_proposal(multisig, multisig_tx, deployer, proposal_id)
