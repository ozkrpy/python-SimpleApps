#!/usr/bin/env python3

import speedtest
import datetime
import time
import csv
import psycopg2
import cv2

conn = psycopg2.connect(
			host="pg12-pre",
			database="monitor",
			user="dbadmin",
			password="areguapgpre")


def insertar_db(bajada: int, subida: int):
	global conn 
	# global cur
	try:
		cur = conn.cursor()
		sql = 'insert into toma_muestras (velocidad_subida, velocidad_bajada) values (%s, %s);'
		cur.execute(sql, (bajada,subida,))
		# cur.execute()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	# finally:
	# 	if conn is not None:
	# 		conn.close()
	# 		print('Database connection closed.')

def consulta_db():
	global conn 
	# global cur
	try:
		cur = conn.cursor()
		sql = 'select max(fecha_registro) from public.toma_muestras;'
		cur.execute(sql)
		ultimo = cur.fetchone()
		# cur.execute()
		# print(ultimo)
		
		return ultimo[0].strftime("%b %d %Y %H:%M:%S")
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

def tomar_muestra():
	s = speedtest.Speedtest()
	downspeed = s.download()
	upspeed = s.upload()
	insertar_db(downspeed, upspeed)
	
try:
	while True:
		k = cv2.waitKey(1) & 0xFF
		# press 'q' to exit
		if k == ord('q'):
			conn.close()
			break
		tomar_muestra()
		print ('ultimo registro insertado:', consulta_db())
		time.sleep(60)
except (Exception, psycopg2.DatabaseError) as error:
	print(error)
	#print(db_version)
	
	# with open('test.csv', mode='w') as speedcsv:
	# 	csv_writer = csv.DictWriter(speedcsv, fieldnames=['toma','subida','bajada'])
	# 	csv_writer.writeheader()
	# 	while True:
	# 		time_now = datetime.datetime.now().strftime("%H:%M:%S")
	# 		downspeed = round((round(s.download())/1048576), 2)
	# 		upspeed = round((round(s.upload())/1048576), 2)
	# 		print(f"Toma: {time_now}, descarga: {downspeed} MB/s, subida: {upspeed} MB/s")
	# 		csv_writer.writerow({
	# 			'toma': time_now,
	# 			'subida': downspeed,
	# 			'bajada': upspeed
	# 		})
	#time.sleep(60)

	
