import requests

class PerplexityAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai/chat/completions"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def create_payload(self, model, messages, **kwargs):
        payload = {
            "model": model,
            "messages": messages
        }
        payload.update(kwargs)
        return payload

    def send_request(self, model, messages, **kwargs):
        payload = self.create_payload(model, messages, **kwargs)
        response = requests.post(self.base_url, json=payload, headers=self.headers)
        return response.json()