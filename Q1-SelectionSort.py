
def selectionSort(l:list=[]) -> list:
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1, len(l)):
            min_idx = j if (l[j]<l[min_idx]) else min_idx
        l[min_idx], l[i] = l[i], l[min_idx]
    return l

if __name__=="__main__":
    unsortedlist:list = [1, 0, 212, 32, 43, 3, 4, 5]
    sortedlist:list = selectionSort(unsortedlist)
    print(selectionSort(sortedlist))