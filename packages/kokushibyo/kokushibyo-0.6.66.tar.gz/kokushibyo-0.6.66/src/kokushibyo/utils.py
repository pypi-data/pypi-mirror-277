
import subprocess
import time
from itertools import product
from sailing_log import MetricsLogger

logger = MetricsLogger("logs")

def iterative_guess_sample_end(worker_num:int, max_num:int, alphabet:list, end_alphabet:list, start:str, key_file:str, data_base:str): 

    worker_start = alphabet[worker_num]
    start += worker_start
    logger.log({"message":f"start string for worker {worker_num} is >> {start}"})
    cntr = 0
    contin = True
    time1 = time.time()
    while contin:
        for i in range(1, max_num+1): 
            logger.log({"message": f"Entering {i} letter combination for woker {worker_num}"})
            combi = product(alphabet, repeat=i)
            for combo in combi:

                cntr += 1 
                if cntr % 1000000 == 0:
                    print(cntr)
                tmp = "".join(list(combo))
                for end in end_alphabet:
                    guess = start + tmp + end
                    success = check_password_keepassxc(guess=guess, key_file=key_file, data_base=data_base)
                    if success == 0: 
                        time2 = time.time()
                        logger.log(metrics={"password":guess, "time": time2-time1, "trials": cntr, "guessed_string":tmp, "searched_leaf_str":worker_start}) 
                        
                        contin = False
                        
                        break
            if contin == False: 
                break
    
    


def iterative_guess(worker_num, max_num, alphabet):
    """Parallelizing through the first guess to avoid duplicates (good luck with your small password)

    Args:
        worker_num (_type_): _description_
        max_num (_type_): _description_
        alphabet (_type_): _description_
    """
    wanted = "p"
    start = ""
    end = "d"
    worker_start = characters_list[worker_num]
    start += worker_start
    print(f"start string for worker {worker_num} is >> {start}")
    cntr = 0
    contin = True
    time1 = time.time()
    while contin: 
        for i in range(1, max_num+1): 
            print(f"Entering {i} letter combination for woker {worker_num}")
            combi = product(characters_list, repeat=i)
            for combo in combi:

                cntr += 1 
                if cntr % 1000000 == 0:
                    print(cntr)
                tmp = "".join(list(combo))
                guess = start + tmp + end
                if guess == wanted: 
                    time2 = time.time()
                    logger.log(metrics={"password":guess, "time": time2-time1, "trials": cntr, "guessed_string":tmp, "searched_leaf_str":worker_start}) 
                    
                    contin = False

def check_password_keepassxc(guess:str, key_file:str, data_base:str)->bool:

     
        out = subprocess.run([f'echo "{guess}"| keepassxc-cli open {data_base} -q --key-file {key_file}'], shell=True,
                         stderr=subprocess.DEVNULL)
        if out.returncode == 0: 
            logger.log({"password":guess})
            return out
        else: 
            return out