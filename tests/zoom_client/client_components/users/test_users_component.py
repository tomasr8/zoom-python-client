import responses
from tests.zoom_client.base_test_case import TestCaseWithAuth
from zoom_client.client_components.users.users_component import UsersComponent
from zoom_client.zoom_api_client import ZoomApiClient


class TestUsersComponent(TestCaseWithAuth):
    @responses.activate
    def test_users_component(self):
        responses.add(
            responses.GET,
            "http://localhost/users/12345",
            json={"response": "ok"},
            status=200,
        )
        zoom_client = ZoomApiClient("aaa", "bbb", "ccc", "http://localhost")
        users_component = UsersComponent(zoom_client)
        user = users_component.get_user("12345")
        assert user == {"response": "ok"}