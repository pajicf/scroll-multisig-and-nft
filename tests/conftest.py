import pytest

@pytest.fixture(scope="session")
def deployer(accounts):
    return accounts[0]  # NOTE: Also Owner 1

@pytest.fixture(scope="session")
def not_owner(accounts):
    return accounts[4]

@pytest.fixture()
def nft(deployer, TheNFT):
    return deployer.deploy(TheNFT)
