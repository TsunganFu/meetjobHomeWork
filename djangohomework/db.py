# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:02:13 2022

@author: User
"""

import pymysql

conn1 = pymysql.connect(host="127.0.0.1" , port=3306 , db="djangohomework" , user="root" , passwd="123456789" , charset="utf8")
cur1 = conn1.cursor()

# Python 在一個py文件中，連接多個MySQL資料庫並區分調用
# host 資料庫主機
# port 資料庫端口
# user 資料庫用戶名
# password 資料庫密碼
# db 資料庫名子
# charset 資料庫編碼

