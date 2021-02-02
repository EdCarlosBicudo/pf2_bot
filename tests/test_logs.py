import pytest
import os
from log import log


@pytest.fixture()
def user(request):

    def teardown():
        if os.path.exists("log/know_users.txt"):
            os.remove("log/know_users.txt")
    request.addfinalizer(teardown)

    return "USUARIO_TESTE"


def test_add_know_user(user):
    log.add_known_user(user)

    assert log.is_user_known(user)


def test_add_already_know_user(user):
    log.add_known_user(user)

    assert log.is_user_known(user)

    log.add_known_user(user)

    file = open("log/know_users.txt", "r")

    assert len(file.readlines()) == 1

    file.close()


def test_check_known_user(user):
    log.add_known_user(user)

    assert log.is_user_known(user)


def test_check_unknown_user(user):
    assert not log.is_user_known(user)


def test_add_access(user):
    command = "class"
    log.log_access(user, command)

    find = f"{user}:{command}"

    found = False
    file = open("log/access_log.txt", 'r')
    for line in file.readlines():
        if find in line:
            found = True
    file.close()
    assert found
