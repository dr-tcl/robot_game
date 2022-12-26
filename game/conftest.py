import pytest


@pytest.fixture(scope='function', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    django_db_blocker.unblock()
