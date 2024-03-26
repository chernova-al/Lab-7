import numpy
from time import perf_counter
import random
import matplotlib.pyplot as plt

def z1():
    list1 = [random.random() for _ in range(10**6)]
    list2 = [random.random() for _ in range(10**6)]

    start_time = perf_counter()  # измерим время перемножения
    multiply1 = [x*y for x in list1 for y in list2]
    end_time = perf_counter()
    result1 = end_time - start_time

    start_time = perf_counter()  # измерим время перемножения с numpy
    multiply2 = numpy.multiply(list1, list2)
    end_time = perf_counter()
    result2 = end_time - start_time

    if result2 < result1:
        print('Перемножение массивов NumPy быстрее на', result1 - result2)

def z2():
    arr = numpy.genfromtxt('data1.csv', delimiter=';')
    time = arr[:100, 0]
    time = time[:, numpy.newaxis]
    position = arr[:100, 3]
    position = position[:, numpy.newaxis]
    fuel = arr[:100, 9]
    fuel = fuel[:, numpy.newaxis]

    plt.plot(time, position*100, 'b', time, fuel, 'r')
    plt.title('График')
    plt.xlabel('Время')
    plt.ylabel('Значения')
    plt.show()

def z3():
    numpy.random.seed(40)
    xs = numpy.linspace(-10, 10, 20)
    ys = numpy.linspace(-0.5, 0.5, 20)
    zs = numpy.tan(xs + ys)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
