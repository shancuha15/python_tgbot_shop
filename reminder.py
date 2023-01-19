import requests
import const as nav

# This function generates a URL link
def send_text(token, chatID, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&parse_mode=Markdown&text={message}'
    response = requests.get(url)
    return response.json()

