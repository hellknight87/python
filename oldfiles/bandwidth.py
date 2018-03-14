#This is a sample program that I made in excel and now converted to Python
print ("This program will calculate the time required to download when the size and badnwidth is entered")

download = float(input("Please enter the size of the download in GB: "))
speed = float(input("Please enter the speed in Mb/s: "))

download_bytes = (download*1024*1024)
speed_bytes = (speed*1024)/8
#print("The speed in kB/s is :", speed_bytes)

time_sec = float(download_bytes)/float(speed_bytes)
time_mins = time_sec/60
time_hours = time_mins/60
time_days = time_hours/24

print()
print ('The time taken to download in seconds :--> {0:.2f} '. format(time_sec))
print ('The time taken to download in minutes :--> {0:.2f} '. format(time_mins))
print ('The time taken to download in hours :--> {0:.2f}'. format(time_hours))
print ('The time taken to download in days :--> {0:.2f}'. format(time_days))
