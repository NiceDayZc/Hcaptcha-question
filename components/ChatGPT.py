from httpx import Client
from time import sleep
from string import ascii_lowercase, digits
from random import choices


class chat(Client):
    def __init__(self):
        super().__init__(
            headers={
                "accept": "application/json, text/plain, */*",
                "accept-language": "th-TH,th;q=0.9",
                "authorization": "Bearer null",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin"
            },

            timeout=90
        )

    def create_conversation(self, question):
        requests = self.post(
            url='https://chatgptproxy.me/api/v1/chat/conversation',
            json={"data":{"parent_id":"0","session_id": self.session_id,"question":question,"user_fake_id": self.user_fake_id}}
        ).json()

        return requests['resp_data']['chat_id']
    
    def fetch_result(self, chat_id):
        while True:
            requests = self.post(
                url='https://chatgptproxy.me/api/v1/chat/result',
                json={"data":{"chat_id":chat_id,"user_fake_id": self.user_fake_id,"session_id": self.session_id}}
            ).json()
            
            if (requests['resp_data']['answer'] != ''):
                return requests['resp_data']['answer']

            sleep(1)

    def conversation_result(self, question):
        self.session_id = ''.join(choices(ascii_lowercase + digits, k=16))
        self.user_fake_id = ''.join(choices(ascii_lowercase + digits, k=16))

        return self.fetch_result(
            chat_id=self.create_conversation(question)
        )