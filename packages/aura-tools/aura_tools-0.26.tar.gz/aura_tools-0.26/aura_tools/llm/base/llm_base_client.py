from abc import ABC, abstractmethod


class LLMBaseClient(ABC):
    def __init__(self, api_key, model="", max_retries=3, retry_interval=60):
        self.api_key = api_key
        self.model = model
        self.max_retries = max_retries
        self.retry_interval = retry_interval

    @abstractmethod
    def send_request(self, messages):
        pass

    @abstractmethod
    def parse_result(self, response):
        pass

    def simple_send_request(self, question):
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
        response = self.send_request(messages)
        result = self.parse_result(response)
        return result
