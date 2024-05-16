from datetime import datetime, timedelta

dt = (datetime.now()+timedelta(hours=-24, days=-1000)).strftime("%Y%m%d %H%M%S.%f")
print("timestamp", dt)

#1. generate logs this hour/xhours ago -> timedelta
#2. generate logs today/xdays ago
#3. generate logs this month
#4. generate logs this year
