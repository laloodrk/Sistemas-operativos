import threading
import time

semaphore = threading.Semaphore(2)

def tarea(id):
    
    print(f"Traea {id} intentando acceder al recurso")
    with semaphore:
        print(f"Traea {id} ha intentado acceder al recurso")
        time.sleep(2)
        print(f"Traea {id} ha liberado acceder al recurso")

threads = []
for i in range(5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
    
