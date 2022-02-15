import speedtest
import pymysql
import os

print("Starting...")

db = pymysql.connect(
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWD'],
    database=os.environ['DB_DATABASE']
)
dbCurson = db.cursor()

s = speedtest.Speedtest()
s.get_servers()
s.get_best_server()

isp = s.config['client']['isp']

download = s.download()
download /= pow(10,6) #convert to mbits/s
download = round(download, 2) #round

upload = s.upload()
upload /= pow(10,6) #convert to mbits/s
upload = round(upload, 2) #round

print("Current connection: "+isp+"\nDownload: "+str(download)+"\nUpload: "+str(upload))

dbCurson.execute("INSERT INTO Speedtest(isp,download,upload) VALUES ('%s', '%f', '%f')" % (isp,download,upload))
db.commit()

db.close()