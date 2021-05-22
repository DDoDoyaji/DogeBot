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
    OAUTH = conf['OAUTH']
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
                if event.type == 'TWITCHCHATJOIN' and event.nickname not in [NAME, 'nightbot', 'twip', 'ssakdook', 'bbangdduck']:
                    COUNT = COUNT + 1
                    print(MESSAGE.format(event.nickname))
                    # observer.send_message(MESSAGE.format(event.nickname), event.channel)

            time.sleep(1)

        except KeyboardInterrupt:
            observer.leave_channel(CHANNEL)
            break