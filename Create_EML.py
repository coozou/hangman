#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:59:12 2019

@author: shinozakiryo
"""

import email
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email import generator





honbun = """●●様
NTT Com篠崎です。お世話になっております。
本日はありがとうございました。
"""

from_addr = 'r.shinozaki@ntt.com'
to_addr = 'coozou@icloud.com'
subject = "御礼"
body = honbun


encoding = 'utf-8'
sender_name = Header('Ryo Shinozaki', encoding).encode()

message = MIMEText(body.encode(encoding), 'plain', _charset=encoding)
message['Subject'] = Header(subject, encoding)
message['From'] = formataddr((sender_name, from_addr))
message['To'] = to_addr
message.add_header('X-Unsent', '1')

with open('test.eml', 'w') as eml:
    gen = generator.Generator(eml)
    gen.flatten(message)

print("** end **")
