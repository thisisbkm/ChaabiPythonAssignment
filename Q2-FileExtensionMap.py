
def mapToExtension()->dict:
    extMap = str(input("Enter extension and type values : ")).strip().split(";")
    extensions = {i[0]:i[1] for i in list(j.split(",") for j in extMap if j!="") if i!=[]}
    fileNames = str(input("Enter file Names Separated by spaces : ")).split()
    answerMap={x:extensions.get(x.split(".")[-1], "unknown") for x in list(fileNames)}
    return answerMap

if __name__=="__main__":
    print(mapToExtension())