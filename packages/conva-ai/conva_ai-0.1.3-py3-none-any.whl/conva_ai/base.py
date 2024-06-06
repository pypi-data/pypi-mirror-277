import uuid
import requests


class BaseClient:

    def __init__(self, assistant_id: str, assistant_version: str, api_key: str, host: str = "https://infer.conva.ai"):
        self.assistant_id: str = assistant_id
        self.api_key: str = api_key
        self.assistant_version: str = assistant_version
        self.host: str = host
        self.keep_conversation_history: bool = True
        self.domain: str = ""
        self.history: str = ""

    def clear_history(self):
        """
        Clears the history tracked by the client
        """
        self.history: str = ""

    def use_history(self, use_history):
        self.keep_conversation_history = use_history
