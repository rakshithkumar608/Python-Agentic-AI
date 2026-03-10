from multiprocessing import Process, Queue

def workers(q):
    q.put("Hello from the worker process!")
    
if __name__ == "__main__":
    
    q = Queue()

    p = Process(target=workers, args=(q,))
    p.start()
    p.join()
    print(q.get())