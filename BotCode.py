import json
import requests
import time
import BotResponse
import os

# Here we take the Token which telegram uses to uniquely identify our bot
BotToken = os.environ['botapi']
URL = "https://api.telegram.org/bot{}/".format(BotToken)


def get_url(url) :

    response = requests.get(url)
    return (response.content.decode("utf8"))


def get_json_from_url(url) :

    return (json.loads(get_url(url)))

# This method is used to extract the relevant information from every message the user and calls BotRespose file to tell what to reply back
def echo_all(updates) :

    for update in updates["result"] :
        try :
            message_id = update["message"]["chat"]["id"]
            user_id = update["message"]["chat"]["username"]
            user_first_name = update["message"]["chat"]["first_name"]
            user_message = update["message"]["text"]

            reply = BotResponse.launchRA(user_id, user_first_name, user_message)
            send_message(reply, message_id)
            print("\n" + user_id + " : " + user_message + "\n\tbot : " + reply)

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
    return (get_json_from_url(url))


def send_message(text, chat_id) :

    get_url(URL + "sendMessage?text={}&chat_id={}".format(text, chat_id))


print("\nLost My Bag Bot @lostmybagbot Started\n")
last_update_id = None
while 1 :

    updates = get_updates(last_update_id)       # This is where we check for the message from the user
    if len(updates["result"]) > 0:          # This execute if we get a message from the user
        last_update_id = get_last_update_id(updates) + 1
        echo_all(updates)

    time.sleep(0.1)