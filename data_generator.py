import random
from array import array
import constants


def random_list(size, lim = constants.MAX_VALUE):
    list_x =[x for x in range(0, size)]
    #while len(ran_list) < size : 
        #ran_list.append(random.randint(0, lim))
    #ran_list.sort()
    ran_array =array('i',list_x)   
    return ran_array

def gen_target(sample_array):
    
    #random.choice(sample_array)
    return -12