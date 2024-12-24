import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    def get_request_helper(self, new_object_id):
        self.response = requests.get(
            f'{self.url}/{new_object_id}'
        )

    @allure.step('Get the object')
    def get_object(self, new_object_id):
        self.get_request_helper(new_object_id)
        return self.response

    @allure.step('Get removed object. Check status code is 404')
    def get_check_status_code_is_404(self, new_object_id):
        self.get_request_helper(new_object_id)
        self.check_status_code(404)
