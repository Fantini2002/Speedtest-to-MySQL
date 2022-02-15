import speedtest

print("Starting...")

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