def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    print(arr)


def shift_down(arr, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        # если дочерние элементы существуют
        if max(l, r) < upper:
            if arr[i] >= max(arr[l], arr[r]):
                break
            elif arr[l] > arr[r]:
                print(f'меняем {arr[i]} на левый {arr[l]}')
                swap(arr, i, l)
                # проверим новый узел
                i = l
            else:
                print(f'меняем {arr[i]} на правый {arr[r]}')
                swap(arr, i, r)
                i = r

        elif l < upper:
            if arr[l] > arr[i]:
                print(f'меняем {arr[i]} на левый {arr[l]}')
                swap(arr, i, l)
                i = l
            else:
                break
        elif r < upper:
            if arr[r] > arr[i]:
                print(f'меняем {arr[i]} на правый {arr[r]}')
                swap(arr, i, r)
                i = r
            else:
                break
        else:
            break


def heapsort(arr):
    for j in range((len(arr) - 2) // 2, -1, -1):
        print(f'{j=}')
        # просеиваем список, от индекса елемента, до верхней границы списка
        shift_down(arr, j, len(arr))
    for end in range(len(arr) - 1, 0, -1):
        print(f'{end=}')
        print(f'меняем первый {arr[0]} на последний {arr[end]}')
        swap(arr, 0, end)
        shift_down(arr, 0, end)


my_list = [25, 18, 5, 10, 15, 12, 3, 4, 2, 8, 6, 9, 7, 1]
print(my_list)
heapsort(my_list)
print(my_list)
