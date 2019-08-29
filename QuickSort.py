import numpy as np


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            t = A[i]
            A[i] = A[j]
            A[j] = t

    t2 = A[i+1]
    A[i+1] = A[r]
    A[r] = t2

    return i + 1

# Hoare提出的最初版本的划分算法
def hoare_partition(A, p, r):
    x = A[p]
    i = p
    j = r

    while i < j:
        if A[j] > x:
            j -= 1
            continue

        if A[i] < x:
            i += 1
            continue

        if A[i] == x and A[j] == x:
            i += 1

        t3 = A[i]
        A[i] = A[j]
        A[j] = t3

    return j


def quick_sort(A, p, r):
    if p < r:
        # q = partition(A, p, r)
        q = hoare_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


if __name__ == '__main__':
    A_size = 100
    A = list(np.random.randint(-100, 100, size=A_size))
    print('Unsorted list:', A)

    quick_sort(A, 0, len(A)-1)
    print('\nSorted list:', A)