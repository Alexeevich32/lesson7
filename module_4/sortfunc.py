    #nums = [5, 7, 3, 1, 4, 8] # пузырьковая сортировка

def bubble_sort(ls): # пузырьковая сортировка
    swapped = True # чтобы цикл сработал хотя бы один раз, задаем значение переменной True
    while swapped:
        swapped = False
        for i in range(len(ls) -1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i] # меняем элементы местами
                swapped = True # меняем значение переменной swap для следующего повтора цикла


# bubble_sort(nums)
# print(nums)

def selection_sort(ls):  # сортировка выборкой
    for i in range(len(ls)): # i количество отсортерованных элементов
        lowest = i # изначально считаем минимальным первый элемент
        for j in range(i + 1, len(ls)): # цикл для перебора неотсортерованных элементов
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i] # самый минимальный элемент меняем с первым элементом


# selection_sort(nums)
# print(nums)