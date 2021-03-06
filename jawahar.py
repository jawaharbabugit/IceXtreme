        
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node=self.head
        for i in range(index+1):
            if node==None:
                return(-1)
            node=node.next
        return node.val
            
            
            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newnode=node(val)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newnode=node(val)
        if self.head==None:
            self.head=newnode
        else:
            node=self.head
            while node.next!=None:
                node=node.next
            node.next=newnode
                
                

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        newnode=node(val)
        node=self.head
        for i in range(index-1):
            if node==None:
                return
            node=node.next
        newnode.next=node.next
        node.next=newnode
  

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None"""
        node=self.head
        for i in range(index-1):
            if node==None:
                return
            node=node.next
        node.next=node.next.next
        
        
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        

UnboundLocalError: local variable 'node' referenced before assignment
    newnode=node(val)
Line 53 in addAtTail (Solution.py)
    __Deserializer__()._deserialize(json.dumps(p[0], escape_forward_slashes=False), "integer"))
Line 130 in __helper_select_method__ (Solution.py)
    ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
Line 182 in _driver (Solution.py)
    _driver()
Line 190 in <module> (Solution.py)
