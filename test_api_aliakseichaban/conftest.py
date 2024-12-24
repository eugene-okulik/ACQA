import pytest
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
def new_object_id(create_object_endpoint, delete_object_endpoint):
    body = {
        "name": "AC_TEST",
        "data": {
            "info": "Some text here"
        }
    }

    create_object_endpoint.new_object(body=body)
    object_id = create_object_endpoint.json['id']

    yield object_id

    delete_object_endpoint.delete_object(object_id)
