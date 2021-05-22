import os
import time
import yaml
from twitchobserver import Observer


global NAME
global OAUTH
global CHANNEL
global MESSAGE
global LIMIT


# Open Configure File
with open('config.yml', 'r') as file:
    conf = yaml.safe_load(file)
    NAME = conf['NAME']
    OAUTH = os.environ['oauth']
    CHANNEL = conf['CHANNEL']
    MESSAGE = conf['MESSAGE']
    LIMIT = conf['LIMIT']
    

with Observer(NAME, OAUTH) as observer:
    observer.join_channel(CHANNEL)
    print('JOINED {}'.format(CHANNEL))


    while True:
        try:
            COUNT = 0
            for event in observer.get_events():
                if COUNT == LIMIT:
                    COUNT = 0
                    break
                if event.type == 'TWITCHCHATJOIN' and event.nickname != NAME and event.nickname != "nightbot" and event.nickname != "twip" and event.nickname != "ssakdook" and event.nickname != "bbangdduck":
                    COUNT = COUNT + 1
                    print(MESSAGE.format(event.nickname, COUNT))
                    observer.send_message(MESSAGE.format(event.nickname), event.channel)
                # if event.type == 'TWITCHCHATMESSAGE' and event.nickname != NAME:
                #     print('[INFO] {}'.format(event.message))

            time.sleep(1)

        except KeyboardInterrupt:
            observer.leave_channel(CHANNEL)
            break