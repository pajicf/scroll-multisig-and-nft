from brownie import TheNFT, network, accounts
import click

def main(nftAddress, multisigAddress):
    print(f"You are using the '{network.show_active()}' network")
    deployer = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'deployer' [{deployer.address}]")

    nft = TheNFT.at(nftAddress)
    nft.transferOwnership(multisigAddress, {"from": deployer})
