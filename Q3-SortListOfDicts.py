
def sortListofDicts(l, key)->list:
    return sorted(l, key=lambda x:x[key])

if __name__=="__main__":
    print(sortListofDicts([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}],"fruit"))