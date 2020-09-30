import threading
import time
threads =[]

start = time.perf_counter()

def do_something():
    print("Will sleep for 1 second")
    time.sleep(1)
    print("Finished..")

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter();

print(f"Total time = {round(finish - start)}second(s)")