import datetime
import multiprocessing
import time


def read_info(name):
    all_data = []
    my_file1 = open(name, 'r', encoding='utf-8')
    non_void_line = True
    while non_void_line:
        non_void_line = my_file1.readline()
        if non_void_line:
            all_data.append(non_void_line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

n_proc = 4

if __name__ == "__main__":

    time1 = time.time()

    for my_file in filenames:
        read_info(my_file)
    time2 = time.time()

    print(f'{datetime.timedelta(seconds=time2 - time1)} (линейный)')

    time1 = time.time()

    pool = multiprocessing.Pool(processes=n_proc)
    pool.map(read_info, filenames)
    pool.close()
    pool.join()

    time2 = time.time()

    print(f'{datetime.timedelta(seconds=time2 - time1)}  (многопроцессный)')
