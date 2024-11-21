import requests

class Telegram:
    def __init__(self, token, id):
        self._token = token
        self._chatId = id
        self._lastChatUrl = "https://api.telegram.org/bot{}/getUpdates".format(self.__token__)
        self._messageUrl = "https://api.telegram.org/bot{}/sendMessage".format(self.__token__)

    def last_chat_id(self):
        try:
            response = requests.get(self._lastChatUrl)
            if response.status_code == 200:
                json_msg = response.json()
                for json_result in reversed(json_msg['result']):
                    message_keys = json_result['message'].keys()
                    if ('new_chat_menber' in message_keys) or ('group_chat_created' in message_keys):
                        print(json_result['message']['chat']['id'])
                        return json_result['message']['chat']['id']
                print('nada encontrado')
            else:
                print(response.status_code)
        except Exception as e:
            print(e)

    def send_message(self, message):
        try:
            data = {
                "chat_id":self._chatId,
                "text":message
            }

            requests.post(self._messageUrl, data)
        except Exception as e:
            print(e)