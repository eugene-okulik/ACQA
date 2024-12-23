import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Update whole object')
    def update_whole_object(self, new_object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_object_id}', json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response


class UpdateObjectParameter(Endpoint):
    def update_objects_parameter(self, new_object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{new_object_id}', json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response
