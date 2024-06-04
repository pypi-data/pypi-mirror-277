import requests

class YellowBalloonAI:
    def __init__(self, api_key, base_url="https://api.example.com"):
        self.api_key = api_key
        self.base_url = base_url

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_resource(self, resource_id):
        url = f"{self.base_url}/resource/{resource_id}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def create_resource(self, data):
        url = f"{self.base_url}/resource"
        response = requests.post(url, headers=self.get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    # 추가적인 API 메소드들을 여기에 정의
