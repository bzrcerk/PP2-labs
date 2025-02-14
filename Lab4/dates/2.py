from datetime import datetime, timedelta

curr = datetime.today().date().strftime('%d/%m')

yest = curr - timedelta(days=1)
tomm = curr + timedelta(days=1)

print(f'Today: {curr}\nYest: {yest}\nTom: {tomm}')

