#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sqlite3

cone= sqlite3.connect("/home/jpc/pd110/src/db.sqlite3")

cursor = cone.cursor()

print("conexión realizada a ",cursor)

### Para ver nombres de tablas que se han creado ###
# cursor.execute("select * from sqlite_master")
# print (cursor)
# for cur in cursor:
#     print cur
cursor.execute("select * from boletin_registrado")
for cur in cursor:
    print cur

cursor.close()
cone.close()
