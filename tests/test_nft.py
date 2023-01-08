import pytest
import brownie

# Test if Token naming is correct
def test_naming(nft):
    assert nft.symbol() == "SNFT"
    assert nft.name() == "Scroll L2 NFT"

# Test if Ownable is working properly
def test_owner(nft, deployer):
    assert nft.owner() == deployer

# Test if NFT minting is working as well as the authorization system
def test_minting(nft, deployer, not_owner, receiver, accounts):
    with brownie.reverts():
        nft.mint(receiver, {"from": not_owner})

    nft.mint(receiver, {"from": deployer})
    assert nft.ownerOf(0) == receiver

# Test if ownership can successfully be changed
def test_ownership_change(nft, multisig, deployer):
    assert nft.owner() == deployer
    nft.transferOwnership(multisig.address, {"from": deployer})
    assert nft.owner() == multisig.address
