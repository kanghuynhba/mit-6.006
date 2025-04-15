class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        newNode=Doubly_Linked_List_Node(x)
        if self.head==None:
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
        self.head=newNode
        ###########################
        pass

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        newNode=Doubly_Linked_List_Node(x)
        if self.tail==None:
            self.head=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
        self.tail=newNode
        ###########################
        pass

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        x=self.head.item
        if self.head.next!=None:
            self.head.next.prev=None
        else:
            self.tail=None
        self.head=self.head.next
        ###########################
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        x=self.tail.item
        if self.tail.prev!=None:
            self.tail.prev.next=None
        else:
            self.head=None
        self.tail=self.tail.prev
        ###########################
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        L2.head=x1
        L2.tail=x2
        if x1.prev!=None:
            x1.prev.next=x2.next
        if x1==self.head:
            self.head=x2.next
        if x2.next!=None:
            x2.next.prev=x1.prev
        if x2==self.tail:
            self.tail=x1.prev
        ###########################
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! #
        if x.next!=None:
            x.next.prev=L2.tail
        else:
            self.tail=L2.tail
        L2.tail.next=x.next
        x.next=L2.head
        L2.head.prev=x
        ###########################
        pass
