def sublist(l:list, i:int, j:int)->list:
    return l[i:j+1:2]


if __name__=="__main__":
    print(sublist([1,2,3,4,5,5,6], 0, 4))