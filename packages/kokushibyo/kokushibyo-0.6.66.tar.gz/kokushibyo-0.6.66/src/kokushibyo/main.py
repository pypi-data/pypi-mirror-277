from multiprocessing import Process

def crack_database(pool_size, max_interferred_len, func, alphabet, end_alphabet, start, key_file, data_base): 

    max_num = max_interferred_len

    procs = []

    for i in range(pool_size):
        print(f"starting worker {i+1}")
        proc = Process(target=func, args = (i, max_num, alphabet, end_alphabet, start, key_file, data_base))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
