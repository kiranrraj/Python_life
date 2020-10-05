import datetime

def todayDate():
    dateTimeNow = str(datetime.datetime.now()).split()
    dateList = dateTimeNow[0].split("-")
    dateList.reverse()
    dt, mo, yr = dateList
    return (f"Date => {dt}/{mo}/{yr}")

def todayTime():
    dateTimeNow = str(datetime.datetime.now()).split()
    timenow = list(map(int, map(float, dateTimeNow[1].split(":"))))
    dot =":"
    h, m, s = timenow
    return (f"Time => {h}:{m}:{s}") 

# todayTime()
# todayDate()

def greet(func1, func2):
    print(func1(), func2())

greet(todayDate, todayTime)


