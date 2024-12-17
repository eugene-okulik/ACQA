import requests
import pytest


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


def get_object(object_id):
    return requests.get(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.mark.critical
@pytest.mark.parametrize('names', ['first_name', 'second_name', 'third_name'])
def test_create_object(session_boundary, boundaries_of_tests, names):
    body = {
        "name": names,
        "data": {
            "info": "Some text here"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    object_id = response.json()['id']

    assert response.status_code == 200, "Wrong status code. 200 is expected"
    assert isinstance(object_id, int), "'id' field is not of type int"


def test_get_object(new_object_id):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_object_id}')

    assert response.status_code == 200, "Wrong status code. 200 is expected"


@pytest.mark.medium
def test_update_whole_object(new_object_id):
    body = {
        "name": "AC_TEST",
        "data": {
            "info": "Modified data here"

        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_object_id}', json=body, headers=headers
    ).json()

    assert response['data']['info'] == "Modified data here", "The 'info' parameter hasn't been updated"


def test_update_objects_parameter(new_object_id):
    body = {
        "name": "AC_TEST_UPDATED_NAME",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_object_id}', json=body, headers=headers
    ).json()

    assert response['name'] == "AC_TEST_UPDATED_NAME", "The 'Name' parameter hasn't been updated"


def test_delete_object(new_object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{new_object_id}')

    assert get_object(new_object_id).status_code == 404, "The object hasn't been removed. Something went wrong"
