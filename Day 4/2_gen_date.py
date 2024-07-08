from datetime import datetime, timedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

while start_date < end_date:
    print(start_date.strftime("%Y-%m-%d"))
    start_date += timedelta(days=1)