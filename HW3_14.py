class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext



class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

#Implement the remove method so that it works 
# correctly in the case where the item is not in the list.


    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())

            else:
                previous = current
                current = current.getNext()
        if found:
            print ("item found and removed")
        else:
            print ("item not found")


mylist = UnorderedList()
mylist.add(5)
mylist.add(50)
mylist.remove(50)
mylist.remove(50)


