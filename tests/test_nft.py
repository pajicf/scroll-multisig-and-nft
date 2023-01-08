import pytest
import brownie

def test_naming(nft):
    assert nft.symbol() == "SNFT"
    assert nft.name() == "Scroll L2 NFT"

def test_owner(nft, deployer):
    assert nft.owner() == deployer

def test_minting(nft, deployer, not_owner, receiver, accounts):
    with brownie.reverts():
        nft.mint(receiver, {"from": not_owner})

    nft.mint(receiver, {"from": deployer})
    assert nft.ownerOf(0) == receiver
