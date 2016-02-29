
# coding: utf-8

# In[1]:

import gzip


# Opening the gz files of moniCa. Given month, day, hours and minutes

# In[47]:

month = 11
if month <= 9:
    monthS = "0" + str(month)
else:
    monthS = str(month)

day = 5
if day <= 9:
    dayS = "0" + str(day)
else:
    dayS = str(day)

minutes = 0
if minutes <= 9:
    minutesS = "0" + str(minutes)
else:
    minutesS = str(minutes)
    
hours = 0
if hours <= 9:
    hoursS = "0" + str(hours)
else:
    hoursS = str(hours)

location = "\\\\winstorage\\users\\bspeckma\\TrafficData\\MoniCa"+"\\" + monthS+"\\"+ dayS+"\\15"+monthS+dayS+hoursS+minutesS+".01G.gz"


# MoniCa file: 11050000 
# 
# Contains: 12775 line of data
# 
# Last line: [SIV] 1446681600 05-11-15 01:00 j 60 60 60 132 0 0 255 1 1 G

# In[48]:

f=gzip.open(location,'rb')
file_content=f.read()
allLines=str(file_content).split("\\n")


# In[46]:

allLines[-2]

