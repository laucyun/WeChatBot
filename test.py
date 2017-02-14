#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Name        : test.py
 Created on  : 2017/02/14 15:11
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2016 - 2017, ]Liuker Team[.
 Description : .
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from wechat import *


class MyWeChat(WeChat):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            # self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            # self.send_file_msg_by_uid("img/1.png", msg['user']['id'])


'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWeChat()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False  # 如果确定通讯录过大，无法获取，可以直接配置，跳过检查。假如不是过大的话，这个方法可能无法获取所有的联系人
    bot.run()


if __name__ == '__main__':
    main()
