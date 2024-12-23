import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get the object')
    def get_object(self, new_object_id):
        self.response = requests.get(
            f'{self.url}/{new_object_id}'
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check status code is 404')
    def get_check_status_code_is_404(self, new_object_id):
        self.response = requests.get(
            f'{self.url}/{new_object_id}'
        )

        assert self.response.status_code == 404, "Wrong status code. 404 is expected"
