# n next
# l 3 lines after and before
# cl clear
# p print
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        k = i
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = chave
    return lista


l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = insertion_sort(l)
print(a)
