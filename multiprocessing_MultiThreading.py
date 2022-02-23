from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from concurrent import futures
import time



def task(item):
    print(str(item), " now i am having a sleep for 10 sec")
    time.sleep(item)
    print(str(item), " i am done")
    return item+1


    


#Multi_processing with iterable e.g. list using map

lst=[30,10,20]
with ProcessPoolExecutor() as executor:
    results = executor.map(task,lst)
    for r in results:
        print(r)


################################################


#multi_threading with single variable e.g. a
a=50
with ThreadPoolExecutor() as executor:
    result = executor.submit(task,a).result()
    print(result)


