# Main.py
import time
import matplotlib.pyplot as plt
import random

from Table import Table


def linear_rehash(key, i, size):
    """
    Linear rehash method
    :param key: Position in the table
    :param iteration: Current iteration
    :param size: Size of the table
    :return: Index of the rehashed key
    """
    return (key + i) % size


def quadratic_rehash(key, i, size):
    """
    Quadratic rehash method
    :param key: Position in the table
    :param iteration: Current iteration
    :param size: Size of the table
    :return: Index of the rehashed key
    """
    return (key + i ** 2) % size


def double_hash(key, i, size):
    """
    Double hash method
    :param key: Position in the table
    :param iteration: Current iteration
    :param size: Size of the table
    :return: Index of the rehashed key
    """
    return (key + i * (7 - (key % 7))) % size


def hash_function(key, size):
    return key % size


def test_linear_rehash(table_size, num_elements, israndom=False):
    # create table with linear rehashing
    table = Table(table_size, hash_method=hash_function, rehash_method=linear_rehash)

    # insert elements into table and measure time
    start_time = time.time()
    for i in range(num_elements):
        if israndom:
            index = random.randint(0, 100000)
            table.insert(index, i)
        else:
            index = i
            table.insert(i, i)
        # remove the element
        table.delete(index)
    end_time = time.time()

    return end_time - start_time


def test_quadratic_rehash(table_size, num_elements, israndom=False):
    # create table with quadratic rehashing
    table = Table(table_size, hash_method=hash_function, rehash_method=quadratic_rehash)

    # insert elements into table and measure time
    start_time = time.time()
    for i in range(num_elements):
        if israndom:
            index = random.randint(0, 100000)
            table.insert(index, i)
        else:
            index = i
            table.insert(i, i)
        # remove the element
        table.delete(index)
    end_time = time.time()

    return end_time - start_time


def test_double_hash(table_size, num_elements, israndom=False):
    table = Table(table_size, hash_method=hash_function, rehash_method=double_hash)

    # insert elements into table and measure time
    start_time = time.time()
    for i in range(num_elements):
        if israndom:
            index = random.randint(0, 100000)
            table.insert(index, i)
        else:
            index = i
            table.insert(i, i)
        # remove the element
        table.delete(index)
    end_time = time.time()

    return end_time - start_time


def test_search_linear(table_size, num_elements, israndom=False):
    table = Table(table_size, hash_method=hash_function, rehash_method=linear_rehash)

    # insert elements into table and measure time
    start_time = time.time()
    for i in range(num_elements):
        if israndom:
            index = random.randint(0, 100000)
            table.insert(index, i)
        else:
            index = i
            table.insert(i, i)
        # search the element
        table.exist(index)
        # delete the element
        table.delete(index)

    end_time = time.time()

    return end_time - start_time


def test_search_quadratic(table_size, num_elements, israndom=False):
    table = Table(table_size, hash_method=hash_function, rehash_method=quadratic_rehash)

    # insert elements into table and measure time
    start_time = time.time()
    for i in range(num_elements):
        if israndom:
            index = random.randint(0, 100000)
            table.insert(index, i)
        else:
            index = i
            table.insert(i, i)
        # search the element
        table.exist(index)
        # delete the element
        table.delete(index)

    end_time = time.time()

    return end_time - start_time


def test_search_double(table_size, num_elements, israndom=False):
    table = Table(table_size, hash_method=hash_function, rehash_method=double_hash)

    # insert elements into table and measure time
    start_time = time.time()
    for i in range(num_elements):
        if israndom:
            index = random.randint(0, 100000)
            table.insert(index, i)
        else:
            index = i
            table.insert(i, i)
        # search the element
        table.exist(index)
        # delete the element
        table.delete(index)

    end_time = time.time()

    return end_time - start_time


def plotit(
        title,
        sizes,
        linear_times,
        quadratic_times,
        double_times,
        linear_times_random,
        quadratic_times_random,
        double_times_random
):
    axs, fig = plt.subplots(ncols=2, nrows=4, figsize=(10, 10))
    # add margin between subplots
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    # x = [10, 100, 1000, 10000] in variable size and y is the time for each size
    fig[0, 0].plot(sizes, linear_times, label='Linear rehashing')
    fig[0, 0].set_title('Linear rehashing')
    fig[0, 0].set_xlabel('Number of elements')
    fig[0, 0].set_ylabel('Time (s)')
    fig[1, 0].plot(sizes, quadratic_times, label='Quadratic rehashing')
    fig[1, 0].set_title('Quadratic rehashing')
    fig[1, 0].set_xlabel('Number of elements')
    fig[1, 0].set_ylabel('Time (s)')
    fig[2, 0].plot(sizes, double_times, label='Double hash')
    fig[2, 0].set_title('Double hash')
    fig[2, 0].set_xlabel('Number of elements')
    fig[2, 0].set_ylabel('Time (s)')
    fig[0, 1].plot(sizes, linear_times_random, label='Linear rehashing with random keys')
    fig[0, 1].set_title('Linear rehashing with random keys')
    fig[0, 1].set_xlabel('Number of elements')
    fig[0, 1].set_ylabel('Time (s)')
    fig[1, 1].plot(sizes, quadratic_times_random, label='Quadratic rehashing with random keys')
    fig[1, 1].set_title('Quadratic rehashing with random keys')
    fig[1, 1].set_xlabel('Number of elements')
    fig[1, 1].set_ylabel('Time (s)')
    fig[2, 1].plot(sizes, double_times_random, label='Double hash with random keys')
    fig[2, 1].set_xlabel('Number of elements')
    fig[2, 1].set_ylabel('Time (s)')
    fig[2, 1].set_title('Double hash with random keys')
    # all values for each test on the same graph
    fig[3, 0].plot(sizes, linear_times, label='Linear rehashing')
    fig[3, 0].plot(sizes, quadratic_times, label='Quadratic rehashing')
    fig[3, 0].plot(sizes, double_times, label='Double hash')
    fig[3, 0].set_title('All tests')
    fig[3, 0].set_xlabel('Number of elements')
    fig[3, 0].set_ylabel('Time (s)')
    # move the legend outside the plot
    fig[3, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    # all values for each test on the same graph with random keys
    fig[3, 1].plot(sizes, linear_times_random, label='Linear rehashing with random keys')
    fig[3, 1].plot(sizes, quadratic_times_random, label='Quadratic rehashing with random keys')
    fig[3, 1].plot(sizes, double_times_random, label='Double hash with random keys')
    fig[3, 1].set_title('All tests with random keys')
    fig[3, 1].set_xlabel('Number of elements')
    fig[3, 1].set_ylabel('Time (s)')
    # move the legend outside the plot
    fig[3, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    # set the title of the plot
    plt.suptitle(title)
    plt.show()
    # save the plot as png file
    plt.savefig(title + '.png')

if __name__ == '__main__':
    # sizes are 100, 100*10, 100*10*10 until 100000000
    sizes = []
    for i in range(1, 9):
        sizes.append(10 ** i)

    # test linear rehashing
    linear_times = []
    for i, size in enumerate(sizes):
        linear_times.append(test_linear_rehash(size, i))

    # test quadratic rehashing
    quadratic_times = []
    for i, size in enumerate(sizes):
        quadratic_times.append(test_quadratic_rehash(size, i))

    # test double hash
    double_times = []
    for i, size in enumerate(sizes):
        double_times.append(test_double_hash(size, i))

    # test linear rehashing with random keys
    linear_times_random = []
    for i, size in enumerate(sizes):
        linear_times_random.append(test_linear_rehash(size, i, israndom=True))

    # test quadratic rehashing with random keys
    quadratic_times_random = []
    for i, size in enumerate(sizes):
        quadratic_times_random.append(test_quadratic_rehash(size, i, israndom=True))

    # test double hash with random keys
    double_times_random = []
    for i, size in enumerate(sizes):
        double_times_random.append(test_double_hash(size, i, israndom=True))

    # test search linear rehashing
    search_linear_times = []
    for i, size in enumerate(sizes):
        search_linear_times.append(test_search_linear(size, i))

    # test search quadratic rehashing
    search_quadratic_times = []
    for i, size in enumerate(sizes):
        search_quadratic_times.append(test_search_quadratic(size, i))

    # test search double hash
    search_double_times = []
    for i, size in enumerate(sizes):
        search_double_times.append(test_search_double(size, i))

    # test search linear rehashing with random keys
    search_linear_times_random = []
    for i, size in enumerate(sizes):
        search_linear_times_random.append(test_search_linear(size, i, israndom=True))

    # test search quadratic rehashing with random keys
    search_quadratic_times_random = []
    for i, size in enumerate(sizes):
        search_quadratic_times_random.append(test_search_quadratic(size, i, israndom=True))

    # test search double hash with random keys
    search_double_times_random = []
    for i, size in enumerate(sizes):
        search_double_times_random.append(test_search_double(size, i, israndom=True))

    plotit(
        "Insertion.png",
        sizes,
        linear_times,
        quadratic_times,
        double_times,
        linear_times_random,
        quadratic_times_random,
        double_times_random
    )
    plotit(
        "Search.png",
        sizes,
        search_linear_times,
        search_quadratic_times,
        search_double_times,
        search_linear_times_random,
        search_quadratic_times_random,
        search_double_times_random
    )
