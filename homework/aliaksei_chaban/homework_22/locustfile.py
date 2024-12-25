import random
from locust import task, HttpUser


class MemeUser(HttpUser):
    object_id = None
    object_id_to_delete = None

    def on_start(self):
        response = self.client.post(
            '/object',
            json={
                "name": "AC_TEST",
                "data": {
                    "info": "Some text here"
                }
            },
            headers={'Content-Type': 'application/json'}
        )

        self.object_id = response.json()['id']

    def create_object(self):
        response = self.client.post(
            '/object',
            json={
                "name": "AC_TEST",
                "data": {
                    "info": "Some text here"
                }
            },
            headers={'Content-Type': 'application/json'}
        )

        return response.json()['id']

    @task
    def get_all_objects(self):
        self.client.get(
            '/object',
        )

    @task(3)
    def get_object(self):
        self.client.get(
            f'/object/{self.object_id}',
        )

    @task
    def post_new_object(self):
        self.client.post(
            '/object',
            json={
                "name": "AC_TEST",
                "data": {
                    "info": "Some text here"
                }
            },
            headers={'Content-Type': 'application/json'}
        )

    @task
    def update_object(self):
        self.client.put(
            f'/object/{self.object_id}',
            json={
                "name": "Updated",
                "data": {
                    "info": "Updated"
                }
            },
            headers={'Content-Type': 'application/json'}
        )

    @task
    def update_object_parameter(self):
        self.client.patch(
            f'/object/{self.object_id}',
            json={
                "data": {
                    "info": "Updated"
                }
            },
            headers={'Content-Type': 'application/json'}
        )

    @task
    def delete_object(self):
        if self.object_id_to_delete is None:
            self.object_id_to_delete = self.create_object()
        self.client.delete(
            f'/object/{self.object_id_to_delete}'
        )
        self.object_id_to_delete = None
