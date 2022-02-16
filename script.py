import speedtest
import pymysql
import os
import time

print('Starting...')

#connect to db
db = pymysql.connect(
    host=os.environ['DB_HOST'],
    port=int(os.environ['DB_PORT']),
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWD'],
    database=os.environ['DB_DATABASE']
)
dbCurson = db.cursor()

#check connection
if dbCurson.connection:
    #check if table exist
    if dbCurson.execute("SHOW TABLES LIKE 'Speedtest'") != 1:
        try:
            dbCurson.execute("CREATE TABLE `Speedtest` (\
                `id` int(11) unsigned NOT NULL AUTO_INCREMENT,\
                `isp` text,\
                `download` float,\
                `upload` float,\
                `timestamp` timestamp,\
                PRIMARY KEY (`id`)\
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8")
            db.commit()
            print("Created table 'Speedtest'")
        except pymysql.Error as e:
            print("Error %d creating table 'Speedtest': %s" % (e.args[0], e.args[1]))
            exit(-1)

    while 1:
        print("Starting speedtest...")
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

        print("Current connection: "+isp+"\nDownload: "+str(download)+" Mbps\nUpload: "+str(upload)+" Mbps")

        dbCurson.execute("INSERT INTO Speedtest(isp,download,upload,timestamp) VALUES ('%s', '%f', '%f', CURRENT_TIMESTAMP())" % (isp,download,upload))
        db.commit()

        print("Sleep for "+os.environ['TIME']+"s")
        time.sleep(int(os.environ['TIME']))

    db.close()

else:
    print("Error connecting to db")
