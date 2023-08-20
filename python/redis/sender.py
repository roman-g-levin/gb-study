# pip install redis
import redis
import random

# open redis generator and sender
with redis.Redis() as rs:
    for i in range(10):
        rs.lpush("queue",random.randint(0,100))
    rs.lpush("queue",'stop')
