from brownie import TheNFT, Supersig, accounts, network
import click

def deployNFTContract(deployer):
    nft = TheNFT.deploy({"from": deployer})
    print("NFT deployed at: {}", nft.address)

def deployMultisigContract(deployer):
    owners = [deployer.address]
    threshold = 1
    multisig = Supersig.deploy(owners, threshold, {"from": deployer})
    print("Multisig deployed at: {}", multisig.address)

def main():
    print(f"You are using the '{network.show_active()}' network")
    deployer = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'deployer' [{deployer.address}]")

    deployNFTContract(deployer)
    deployMultisigContract(deployer)
