# coding:utf-8
import os

redis = "D:\\DevTools\\redis\\Redis-x64-3.0.504\\redis-server.exe D:\\DevTools\\redis\\Redis-x64-3.0.504\\redis.windows.conf"
os.system(redis)


"""
命令:
flushall  清空
keys * 查看所有
get image_code_aaa 根据key查看值  image_code_aaa是key
"""