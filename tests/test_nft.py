def test_naming(nft):
    assert nft.symbol() == "SNFT"
    assert nft.name() == "Scroll L2 NFT"

def test_owner(nft, deployer):
    assert nft.owner() == deployer
