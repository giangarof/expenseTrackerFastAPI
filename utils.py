def newId(theList):
    if len(theList) == 0:
        newId = 1
    else:
        newId = theList[-1].id + 1

    return newId

