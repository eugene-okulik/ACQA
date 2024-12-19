import pytest
import requests


@pytest.fixture()
def new_object_id():
    body = {
        "name": "AC_TEST",
        "data": {
            "info": "Some text here"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    object_id = response.json()['id']

    yield object_id

    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(autouse=True)
def boundaries_of_tests():
    print('\n~~~ before test ~~~')
    yield
    print('\n~~~ after test ~~~')


@pytest.fixture(scope='session')
def session_boundary():
    print('\n---------------------------- Start testing ---------------------------')
    yield
    print('\n--------------------------- Testing completed ---------------------------')
