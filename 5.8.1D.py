# search.py

def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)
