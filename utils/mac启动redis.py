# coding:utf-8
import os

redis = "/Users/sss/devTools/redis-6.0.6/src/redis-server /Users/sss/devTools/redis-6.0.6/redis.conf"
os.system(redis)


"""
命令:
flushall  清空
keys * 查看所有
get image_code_aaa 根据key查看值  image_code_aaa是key
"""