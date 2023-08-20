# pip install redis
import redis

# open redis receiver
with redis.Redis() as rr:
    while True:
        value = rr.rpop("queue")
        if value == None:
            continue
        if value == b'stop':
            break
        else:
            print(value)

