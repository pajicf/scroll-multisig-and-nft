from brownie import TheNFT, Supersig

# If using Etherscan supported network, you can run this for easier verification
def main(nftAddress, multisigAddress):
    nft = TheNFT.at(nftAddress)
    multisig = Supersig.at(multisigAddress)

    TheNFT.publish_source(nft)
    Supersig.publish_source(multisig)
