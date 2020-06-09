#   Avinash Varma
#   Code Responsible for the running of telegram bot @IWCgobot
# 1105528767:AAHw0JFtfExVC5wj7wz7L10uKVN7FFFZDkQ

import json
import requests
import time
import BotResponse
import os

BotToken = os.environ['botapi']

URL = "https://api.telegram.org/bot{}/".format(BotToken)


def get_url(url) :

    response = requests.get(url)
    content = response.content.decode("utf8")
    return (content)


def message(message_id, user_id, user_first_name, user_message) :

    reply = BotResponse.launchRA(user_id, user_first_name, user_message)
    send_message(reply, message_id)
    print("\n"+user_id+" : "+user_message+"\n\tbot : "+reply)
    return (0)


def get_json_from_url(url) :

    return (json.loads(get_url(url)))


def echo_all(updates) :

    for update in updates["result"] :
        try :
            message_id = update["message"]["chat"]["id"]
            user_id = update["message"]["chat"]["username"]
            user_first_name = update["message"]["chat"]["first_name"]
            user_message = update["message"]["text"]

            message(message_id, user_id, user_first_name, user_message)

        except Exception as e:
            print (e)


def get_last_update_id(updates) :

    update_ids = []
    for update in updates["result"] :
        update_ids.append(int(update["update_id"]))
    return (max(update_ids))


def get_updates(offset=None) :

    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return (js)


def send_message(text, chat_id) :

    get_url(URL + "sendMessage?text={}&chat_id={}".format(text, chat_id))


print("\nLost My Bag Bot @lostmybagbot Started\n")
last_update_id = None
while 1 :

    updates = get_updates(last_update_id)

    if len(updates["result"]) > 0:
        last_update_id = get_last_update_id(updates) + 1
        echo_all(updates)

    time.sleep(0.1)