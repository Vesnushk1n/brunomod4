def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = []
a = int(input('Введите первое число: '))
arr.append(a)
b = int(input('Введите второе число: '))
arr.append(b)
c = int(input('Введите третье число: '))
arr.append(c)
d = int(input('Введите четвёртое число: '))
arr.append(d)
e = int(input('Введите пятое число: '))
arr.append(e)
sort(arr)
for i in range(len(arr)):
    print(arr[i])