import requests
import os
import json

from .config import configuration
internal_requests = requests.Session()


def register_service():
    internal_requests.headers.update({'Tenant': os.getenv("TENANT")})
    internal_requests.post(
        "http://web:8000/api/v1/service/alive/",
        {
            "service": os.getenv("SERVICE_NAME"),
            "config": json.dumps(configuration)
        }
    ).raise_for_status()

def get_config():
    response = internal_requests.get(f"http://web:8000/api/v1/service/configstore/{os.getenv('SERVICE_NAME')}").json()

    return response.get("params")


class Conversation:
    def get_messages(conversation_id):
        response = internal_requests.get(f"http://web:8000/api/v1/conversations/{conversation_id}").json()
        return response.get("params")

    def add_message(message):
        print("This is being handled by the bff for now, comming soon.")

    def on_initialize():
        print("comming soon...")