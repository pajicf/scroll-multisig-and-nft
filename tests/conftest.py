import pytest

@pytest.fixture()
def deployer(accounts):
    return accounts[0]

@pytest.fixture()
def not_owner(accounts):
    return accounts[4]

@pytest.fixture()
def receiver(accounts):
    return accounts[5]

@pytest.fixture()
def nft(deployer, TheNFT):
    return TheNFT.deploy({"from": deployer})
