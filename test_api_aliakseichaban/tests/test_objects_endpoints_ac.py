import pytest

TEST_DATA = [
    {"name": "Alex", "data": {"info": "Some text here"}},
    {"name": "Bob", "data": {"info": "Some text here"}},
    {"name": "Trevor", "data": {"info": "Some text here"}},
]

DATA_FOR_UPDATING = [{"name": "New name", "data": {"info": "Modified text"}}]
NAME_FOR_UPDATING = [{"name": "AC_TEST_UPDATED_NAME", }]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(create_object_endpoint, data):
    create_object_endpoint.new_object(body=data)
    create_object_endpoint.check_status_code(200)
    create_object_endpoint.check_response_name_is_correct(data['name'])


def test_get_object(get_object_endpoint, new_object_id):
    get_object_endpoint.get_object(new_object_id)
    get_object_endpoint.check_status_code(200)


@pytest.mark.parametrize('data', DATA_FOR_UPDATING)
def test_update_whole_object(update_object_endpoint, new_object_id, data):
    update_object_endpoint.update_whole_object(new_object_id, body=data)
    update_object_endpoint.check_status_code(200)
    update_object_endpoint.check_response_name_is_correct(data['name'])


@pytest.mark.parametrize('data', NAME_FOR_UPDATING)
def test_update_objects_parameter(update_object_parameter_endpoint, new_object_id, data):
    update_object_parameter_endpoint.update_objects_parameter(new_object_id, body=data)
    update_object_parameter_endpoint.check_status_code(200)
    update_object_parameter_endpoint.check_response_name_is_correct(data['name'])


def test_delete_object(delete_object_endpoint, get_object_endpoint, new_object_id):
    delete_object_endpoint.delete_object(new_object_id)
    delete_object_endpoint.check_status_code(200)
    get_object_endpoint.get_check_status_code_is_404(new_object_id)
