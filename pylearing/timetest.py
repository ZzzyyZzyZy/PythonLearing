import time
import calendar
# 格式化时间
print(time.asctime(time.localtime(time.time())))

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))


print (calendar.month(2015,1))