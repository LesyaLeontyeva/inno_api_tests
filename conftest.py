import pytest

from api.client import Client
from model.login import UserData


@pytest.fixture(scope="session")
def unauth_client(request):
    url = request.config.getoption("--base-url")
    return Client(url=url)


@pytest.fixture(scope='session')
def auth_client(request):
    url = request.config.getoption("--base-url")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    client = Client(url=url)
    client.set_cookies(UserData(username=username, password=password))
    return client


@pytest.fixture()
def get_username(request):
    return request.config.getoption("--username")


@pytest.fixture()
def get_password(request):
    return request.config.getoption("--password")


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://restful-booker.herokuapp.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="admin",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="password123",
        help="enter password",
    ),
