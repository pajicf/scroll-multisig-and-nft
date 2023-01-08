import pytest
import brownie
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

# Test minting through the multisig
def test_multisig_minting(nft, multisig, receiver, deployer, multisig_owners):
    nft.transferOwnership(multisig.address, {"from": deployer})
    assert nft.owner() == multisig.address

    multisig_tx = build_nft_mint_multisig_tx(receiver, nft)

    proposalId = 0
    # propose tx
    multisig.propose(proposalId, multisig_tx["proposal_hash"], {"from": deployer})

    # should revert until approved
    with brownie.reverts():
        multisig.execute(
            proposalId,
            multisig_tx["target"],
            multisig_tx["calldata"],
            multisig_tx["value"],
        )

    # let's approve it
    multisig.approve(proposalId, {"from": multisig_owners[0]})
    multisig.approve(proposalId, {"from": multisig_owners[1]})

    print(multisig_tx)

    # and now mint it
    multisig.execute(
        proposalId,
        multisig_tx["target"],
        multisig_tx["calldata"],
        multisig_tx["value"],
    )

    assert nft.ownerOf(0) == receiver
