# (1) DB연결
import pymysql
import dbconnect as db
from dh11sensor import temperature, humidity

def insert():
  #온습도 내역 포맷팅
  hum = '{0:0.0f}'.format(humidity)
  temp = '{0:0.1f}'.format(temperature)
  
  #DB연결
  conn = db.dbconnect()
  print('연결완료')
  
  cur = conn.cursor()
  sql ="""INSERT INTO TEMP_HUM (TEMPERATURE, HUMIDITY) VALUES(%s, %s)""" 
  cur.execute(sql, (temp, hum))
  conn.commit() 
  conn.close() # 커넥트 해제
  print('연결해제')

if __name__=="__main__" :
  if temperature is not None and humidity is not None:
    print('성공')
    insert()
  else : print('X') 