# Main.py
import time
import matplotlib.pyplot as plt

from Table import Table


def linear_rehash(key, size):
    return (key + 1) % size


def quadratic_rehash(key, size):
    return (key + 1 + key ** 2) % size


def double_hash(key, size):
    return (key + 1 + key ** 2) % size


def hash(key, size):
    return key % size


if __name__ == '__main__':
    size = 10000
    table = Table(size, hash_method=hash, rehash_method=linear_rehash)

    measures = []

    for n in range(1000, 10001, 1000):
        start_time = time.time()
        for i in range(n):
            table.insert(i, 'value')
        end_time = time.time()
        measures.append((n, end_time - start_time))

    table = Table(size, hash_method=hash, rehash_method=quadratic_rehash)
    measures_quad = []
    for n in range(1000, 10001, 1000):
        start_time = time.time()
        for i in range(n):
            table.insert(i, 'value')
        end_time = time.time()
        measures_quad.append((n, end_time - start_time))

    table = Table(size, hash_method=hash, rehash_method=double_hash)
    measures_double = []
    for n in range(1000, 10001, 1000):
        start_time = time.time()
        for i in range(n):
            table.insert(i, 'value')
        end_time = time.time()
        measures_double.append((n, end_time - start_time))

    fig, axs = plt.subplots(nrows=3, ncols=1)
    axs[0].plot([x[0] for x in measures], [x[1] for x in measures], label='Linear')
    axs[1].plot([x[0] for x in measures_quad], [x[1] for x in measures_quad], label='Quadratic')
    axs[2].plot([x[0] for x in measures_double], [x[1] for x in measures_double], label='Double')
    axs[0].set_title('Linear rehash')
    axs[1].set_title('Quadratic rehash')
    axs[2].set_title('Double rehash')
    axs[0].set_xlabel('Number of elements')
    axs[1].set_xlabel('Number of elements')
    axs[2].set_xlabel('Number of elements')
    axs[0].set_ylabel('Time (s)')
    axs[1].set_ylabel('Time (s)')
    axs[2].set_ylabel('Time (s)')
    axs[0].legend()
    axs[1].legend()
    axs[2].legend()

    plt.show()
