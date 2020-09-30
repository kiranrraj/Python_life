import concurrent.futures
import time
threads =[]

start = time.perf_counter()

def do_something(seconds):
    print(f"Will sleep for {seconds} second(s)")
    time.sleep(seconds)
    return f"Finished..{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]

    #using list comprehension method
    results = [executor.submit(do_something, second) for second in seconds]


    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter();

print(f"Total time = {round(finish - start, 2)} second(s)")