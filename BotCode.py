#   Avinash Varma
#   Code Responsible for the running of telegram bot @IWCgobot

import json
import requests
import time
import ResponseAnalysis

URL = "https://api.telegram.org/bot{}/".format("1228146641:AAFNB98sebEXBLKhDgJwWK6gcxsmLCgfOq4")


def get_url(url) :

    response = requests.get(url)
    content = response.content.decode("utf8")
    return (content)


def message(message_id, user_id, user_first_name, user_message) :

    reply = ResponseAnalysis.launchRA(user_message, user_first_name)
    send_message(reply, message_id)
    print("\n"+user_id+" : "+user_message+"\n\tbot : "+reply)
    return (0)


def get_json_from_url(url) :

    return (json.loads(get_url(url)))


def echo_all(updates,trig) :

    for update in updates["result"] :
        try :
            message_id = update["message"]["chat"]["id"]
            user_id = update["message"]["chat"]["username"]
            user_first_name = update["message"]["chat"]["first_name"]
            user_message = update["message"]["text"]

            if user_message == "END" or user_message == "End" or user_message == "end" :
                message(message_id, user_id, user_first_name, user_message)
                return (8)
            message(message_id, user_id, user_first_name, user_message)
            return (1)

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


def BotGO(trig) :

    last_update_id = None
    while trig :

        updates = get_updates(last_update_id)

        if trig == 8 :
            print("\n\nBot completed the Job!\nGood Bye!")
            return (0)

        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            trig = echo_all(updates, trig)

        time.sleep(0.1)

BotGO(1)