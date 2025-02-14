from datetime import datetime, timedelta

curr = datetime.today().date()

res = timedelta(days=5)

print(curr - res)