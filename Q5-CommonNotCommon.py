
def comnotcom(l1, l2):
    print("Common Elements : ", list(set(l1).intersection(l2)))
    print("Not Common Elements : ", list(set(l1).symmetric_difference(l2)))


if __name__=="__main__":
    comnotcom(["One Punch Man","Attack On Titan","One Piece","SwordArt Online","Bleach","Dragon Ball Z","One Piece"],
    ["Full Metal Alchemist","Code Geass","DeathNote","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]
    )
