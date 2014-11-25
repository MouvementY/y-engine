from django.conf import settings

import redis


PUSH_CHANNEL_SIGNATURE = 'signatures'


##
# Redis client *singleton*

redis_conf = settings.REDIS
redis_client = redis.StrictRedis(host=redis_conf.hostname,
                                 port=redis_conf.port,
                                 db=0)
