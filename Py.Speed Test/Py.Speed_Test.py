import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print(f'Sorat Download Barabar: {download_speed}')
print(f'Sorat Upload Barabar: {upload_speed}')




