
#Developed by Rafael Niquefa

import time
import algorithms
import constants
import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)
        #print(times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    targets = []
    for _ in range(samples_by_size):
        samples.append(data_generator.random_list(size))
        #agregar condicion para que el target esté dentro del array generado
        targets.append(data_generator.gen_target(samples[-1]))
        
    return [
        take_time_for_algorithm(samples,targets, algorithms.linear_search),
        take_time_for_algorithm(samples,targets, algorithms.binary_search),
        take_time_for_algorithm(samples,targets, algorithms.ternary_search),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, targets, search_algorithm):
    times = []
    tg_cnt = -1
    for sample in samples_array:
        tg_cnt += 1
        start_time = time.time()
        search_algorithm(sample,targets[tg_cnt]) 
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))
    #print(times)

    times.sort()
    return times[len(times) // 2]


