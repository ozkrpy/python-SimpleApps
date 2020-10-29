#!/usr/bin/env python3

import speedtest
import datetime
import time
import csv
import psycopg2


s = speedtest.Speedtest()
conn = psycopg2.connect(
    host="pg12-pre",
    database="monitor",
    user="dbadmin",
    password="areguapgpre")
try:
	downspeed = s.download()
	upspeed = s.upload()

	cur = conn.cursor()
	
	cur.execute('insert into toma_muestras (velocidad_subida, velocidad_bajada) values (%s);', (downspeed,upspeed))
	# cur.execute()
	conn.commit()
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
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
	if conn is not None:
        	conn.close()
        	print('Database connection closed.')
	
