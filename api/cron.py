import requests
import os





apik=os.environ.get("TELEGRAM")
url = "https://api.telegram.org/bot"+apik
def get(metthod):
    message = {
        "chat_id":1462438140,
        "text":"hello"
    }

    req = url+metthod
    resp = requests.get(req, data=message)
    print(resp.text)
    return True, 200



