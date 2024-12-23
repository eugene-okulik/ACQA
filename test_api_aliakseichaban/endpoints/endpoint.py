import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, "The 'Name' parameter hasn't been updated"

    @allure.step('Check status code')
    def check_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, "Wrong status code"
