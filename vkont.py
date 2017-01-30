import requests
import random
import vk
from time import sleep
from send_mess import *

from selt import query
from bsuir_bot.send_mess import send_to_ai

api = vk.API(vk.AuthSession(app_id = '5794681', user_login = 'ilovehloyaproject@gmail.com',
                            user_password = '154    57578', scope = 'messages'))
messages = {}
classes = (155, 260, 375, 480, 595)
times_set = {1: "8:00-9:35", 2: "9:45-11:20", 3: "11:40-13:15", 4: "13:25-15:00", 5: "15:20-16:55"}
days = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}


def classes(user):
    try:
        para = js['result']['contexts'][0]["parameters"]['para']
        corp = js['result']['contexts'][0]["parameters"]['corp']
        date = js['result']['contexts'][0]["parameters"]['date']
        response = requests.get(
                url = "http://www.bsuir.by/schedule/rest/currentWeek/date/" + date[:4] + "." + date[5:7] + "." + date[
                                                                                                                 8:10])
        week = str(response.content)[2]
        day = days[response.headers['date'][:3]]
        valid = query(week, day, corp, para)
        print(valid)
        api.messages.setActivity(chat_id = user)
        api.messages.send(user_id = user, message = str(valid))
    except:
        resp = js['result']['fulfillment']['speech']
        sleep(0.5)
        if resp:
            print(resp)
            api.messages.setActivity(chat_id = user)
            api.messages.send(user_id = user, message = resp)
    sleep(1)


def news(user):
    a = api.newsfeed.search(q = "TAG", count = 5)#count = 1-5:)
    for post in a[1:]:
        if str(post["from_id"]) == "-99068826":
            api.messages.send(user_id = user, random_id = random.randint(1, 2000), #random_id to не отправлять одно сообщение несколько раз
                          attachment = "wall" + str(post["from_id"]) + "_" + str(post["id"]))


while True:
    mes = (api.messages.get(count = 10))
    sleep(1)
    mes = mes[1:]
    message = list([a['uid'], a['body']] for a in mes if a['read_state'] == 0)
    if message != []:
        print(message)
        for mess in message:
            js = send_to_ai(mess[1])
            # Если поиск аудиторий
            if js['result']['fulfillment']['speech'] == 'сек':  # js['result']['metadata']['intentName'] == "schedule-confirm-yes":
                classes(user = mess[0])
            if js['result']['fulfillment']['speech'] == 'жопа':
                news(user = mess[0])
