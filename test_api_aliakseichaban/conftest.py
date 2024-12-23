import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject, UpdateObjectParameter
from endpoints.get_object import GetObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def update_object_parameter_endpoint():
    return UpdateObjectParameter()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


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
