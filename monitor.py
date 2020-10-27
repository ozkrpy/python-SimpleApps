import speedtest
import datetime
import time
import csv

s = speedtest.Speedtest()

with open('test.csv', mode='a') as speedcsv:
	csv_writer = csv.DictWriter(speedcsv, fieldnames=['toma','subida','bajada'])
	csv_writer.writeheader()
	while True:
		time_now = datetime.datetime.now().strftime("%H:%M:%S")
		downspeed = round((round(s.download())/1048576), 2)
		upspeed = round((round(s.upload())/1048576), 2)
		print(f"Toma: {time_now}, descarga: {downspeed} MB/s, subida: {upspeed} MB/s")
		csv_writer.writerow({
			'toma': time_now,
			'subida': downspeed,
			'bajada': upspeed
		})
		time.sleep(60)
	
