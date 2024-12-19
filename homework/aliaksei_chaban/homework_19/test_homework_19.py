import allure
import requests
import pytest


def get_object(object_id):
    return requests.get(f'http://167.172.172.115:52353/object/{object_id}')


@allure.feature('Other Objects')
@allure.story('Create objects')
@allure.title('Создание нового объекта')
@pytest.mark.critical
@pytest.mark.parametrize('names', ['first_name', 'second_name', 'third_name'])
def test_create_object(session_boundary, boundaries_of_tests, names):
    with allure.step('Run post request'):
        body = {
            "name": names,
            "data": {
                "info": "Some text here"
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
        object_id = response.json()['id']

    with allure.step('Check status code is 200'):
        assert response.status_code == 200, "Wrong status code. 200 is expected"

    with allure.step('Check id is int type'):
        assert isinstance(object_id, int), "'id' field is not of type int"


@allure.feature('Objects')
@allure.story('Get objects')
@allure.title('Получение нового объекта')
def test_get_object(new_object_id):
    with allure.step(f'Get the object with id {new_object_id}'):
        response = requests.get(f'http://167.172.172.115:52353/object/{new_object_id}')

    with allure.step('Check status code is 200'):
        assert response.status_code == 200, "Wrong status code. 200 is expected"


@allure.feature('Objects')
@allure.story('Update objects')
@allure.title('Полное обновление объекта')
@pytest.mark.medium
def test_update_whole_object(new_object_id):
    with allure.step('Prepare test data'):
        body = {
            "name": "AC_TEST",
            "data": {
                "info": "Modified data here"

            }
        }
        headers = {'Content-Type': 'application/json'}

    with allure.step('Run a request to update an object'):
        response = requests.put(
            f'http://167.172.172.115:52353/object/{new_object_id}', json=body, headers=headers
        ).json()

    with allure.step('Check if update has been applied'):
        assert response['data']['info'] == "Modified data here", "The 'info' parameter hasn't been updated"


@allure.story('Update objects')
@allure.feature('Objects')
@allure.title('Частичное обновление объекта')
def test_update_objects_parameter(new_object_id):
    with allure.step(f'Update particular object parameter with id {new_object_id}'):
        body = {
            "name": "AC_TEST_UPDATED_NAME",
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{new_object_id}', json=body, headers=headers
        ).json()

    with allure.step('Check if parameter has been updated'):
        assert response['name'] == "AC_TEST_UPDATED_NAME", "The 'Name' parameter hasn't been updated"


@allure.feature('Objects')
@allure.story('Remove objects')
@allure.title('Удаление объекта')
def test_delete_object(new_object_id):
    with allure.step(f'Remove object with id {new_object_id}'):
        requests.delete(f'http://167.172.172.115:52353/object/{new_object_id}')

    with allure.step(f'Check if object with id {new_object_id} has been removed'):
        assert get_object(new_object_id).status_code == 404, "The object hasn't been removed. Something went wrong"
