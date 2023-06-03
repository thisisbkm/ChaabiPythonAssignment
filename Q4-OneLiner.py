

def interchangeItems(dictionary)->dict:
    return {value: key for key,value in dictionary.items()}


if __name__=="__main__":
    print(interchangeItems({1:"a",2:"b",3:"c"}))
    print(interchangeItems({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}))