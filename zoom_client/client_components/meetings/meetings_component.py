from zoom_client.zoom_client_interface import ZoomClientInterface


class MeetingsComponent:
    def __init__(self, client: ZoomClientInterface) -> None:
        self.client = client

    def get_meeting(self, meeting_id: str) -> dict:
        api_path = f"/meetings/{meeting_id}"
        response = self.client.make_get_request(api_path)
        result = response.json()
        return result
