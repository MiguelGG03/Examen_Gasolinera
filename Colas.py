from multiprocessing import Process, Queue, Pool



def f(name):
    print('hello', name)


def g(x):
    return x*x


if __name__ == '__main__':
    names=['bob','joe','jane']
    for name in names:
        p = Process(target=f, args=(name,))
        p.start()
        p.join()

    with Pool(5) as p:
        print(p.map(g, [i for i in range(100)]))
