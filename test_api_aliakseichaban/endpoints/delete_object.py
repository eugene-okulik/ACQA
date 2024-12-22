import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_object(self, new_object_id):
        self.response = requests.delete(
            f'{self.url}/{new_object_id}'
        )
        self.json = {"message": self.response.text}
        return self.response
