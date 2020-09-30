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

    results = executor.map(do_something, seconds)

    for result in results:
        print(result)


finish = time.perf_counter();

print(f"Total time = {round(finish - start, 2)} second(s)")