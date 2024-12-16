import requests


def new_object():
    body = {
        "name": "AC_TEST",
        "data": {
            "info": "Some text here"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)

    return response.json()['id']


def get_object(object_id):
    return requests.get(f'http://167.172.172.115:52353/object/{object_id}')


def clear(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def create_object():
    body = {
        "name": "AC_TEST",
        "data": {
            "info": "Some text here"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    object_id = response.json()['id']

    assert response.status_code == 200, "Wrong status code. 200 is expected"
    assert isinstance(object_id, int), "'id' field is not of type int"

    clear(object_id)


def update_whole_object():
    object_id = new_object()
    body = {
        "name": "AC_TEST",
        "data": {
            "info": "Modified data here"

        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_object()}', json=body, headers=headers
    ).json()

    assert response['data']['info'] == "Modified data here", "The 'info' parameter hasn't been updated"

    clear(object_id)


def update_objects_parameter():
    object_id = new_object()

    body = {
        "name": "AC_TEST_UPDATED_NAME",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353/object/{object_id}', json=body, headers=headers).json()

    assert response['name'] == "AC_TEST_UPDATED_NAME", "The 'Name' parameter hasn't been updated"

    clear(object_id)


def delete_object():
    object_id = new_object()

    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')

    assert get_object(object_id).status_code == 404, "The object hasn't been removed. Something went wrong"


create_object()
update_whole_object()
update_objects_parameter()
delete_object()
