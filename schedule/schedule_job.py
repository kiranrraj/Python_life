import schedule

def print_job():
    print("I am printing")

schedule.every(2).seconds.do(print_job)

while True:
    schedule.run_pending()