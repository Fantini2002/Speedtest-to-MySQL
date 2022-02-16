import speedtest
import pymysql
import os
import time

print("Starting...")

db = pymysql.connect(
    host=os.environ['DB_HOST'],
    port=int(os.environ['DB_PORT']),
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWD'],
    database=os.environ['DB_DATABASE']
)
dbCurson = db.cursor()

while 1:
    print("Start speedtest")
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

    dbCurson.execute("INSERT INTO Speedtest(isp,download,upload,date,time) VALUES ('%s', '%f', '%f', CURDATE(), CURTIME())" % (isp,download,upload))
    db.commit()

    print("Sleep for "+os.environ['TIME'])
    time.sleep(int(os.environ['TIME']))

db.close()