class Node:
    def __init__(self,):
        self.node = None
        self.data = ""

class List:
    def __init__(self, *args):
        self.root = Node()
        for a in args:
            self.add(a)

    def add(self, element):
        ptr = self.root

        while ptr.node != None:
            ptr = ptr.node
        ptr.node = Node()
        ptr.data = element

    def __iter__(self):
        self.next = self.root
        return self

    def __next__(self):
        if self.next.node != None:
            result = self.next.data
            self.next = self.next.node
            return result
        else:
            raise StopIteration


#l = List(1,2,3,4)
#for n in l:
#    print(n)
