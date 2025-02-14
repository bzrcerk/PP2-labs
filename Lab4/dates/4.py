from datetime import datetime, timedelta

date1 = datetime(2021, 12, 31, 23, 59, 0)
date2 = datetime(2022, 1, 1, 0, 0, 0)

print(abs((date1 - date2).total_seconds()))