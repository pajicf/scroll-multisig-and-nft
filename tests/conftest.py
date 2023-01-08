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

@pytest.fixture()
def multisig_owners(accounts):
    return accounts[:3]

@pytest.fixture()
def multisig_threshold():
    return 2

@pytest.fixture()
def multisig(deployer, Supersig, multisig_owners, multisig_threshold):
    return Supersig.deploy(multisig_owners, multisig_threshold, {"from": deployer})


