import requests
import os

internal_requests = requests.Session()


def register_service():
    internal_requests.headers.update({'Tenant': os.getenv("TENANT")})
    internal_requests.post("http://web:8000/api/v1/service/alive/").raise_for_status()


class Conversation:
    def get_messages(conversation_id):
        return internal_requests.get(f"http://web:8000/api/v1/conversations/{conversation_id}").json()

    def add_message(message):
        print("This is being handled by the bff for now, comming soon.")

    def on_initialize():
        print("comming soon...")