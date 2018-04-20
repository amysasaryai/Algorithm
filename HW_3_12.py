from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for i in range(len(aString)):
        if aString[i] != " ":
            chardeque.addRear(aString[i])

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjf sk f "))
print(palchecker("ra  d a r"))
print(palchecker("ra a d da ar"))
