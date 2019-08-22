#single linked list
#https://stackabuse.com/python-linked-lists/
class ListNode: 
  
    # Constructor to initialize the node object 
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def __init__(self, x):
        "Constructor to initiate this object"
        
        #store data
        self.val = x 
        
        #store reference (next item)
        self.next = None
        return
    def push(self, item):
        "add an item at the end of the list"
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.ead is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.val == value:
            return True
        else: 
            return False
    def list_length(self):
        "return the # of list items"
        count = 0
        current_node = self.head
        while current_node is not None:
            #increase counter by one
            count = count + 1
            #jump to the linked node
            current_node = current_node.next
        return count
    
    def output_list(self):
        "Output the list (the value of the node)"
        current_node = self.head
        while current_node is not None:
            print(current_node.val)
            #jump to the linked ode
            current_node = current_node.next
        return
    def unordered_search (self, value):
        "search the linked list for the node that has this value"
        #define current_node
        current_node = self.head
        #define position
        node_id = 1
        #define list of results
        results =[]
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            #jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        return results
    def remove_list_item_by_id (self, item_id):
        "remove the list item with the item id"
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                #if this is the first node(head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    #we dont have to look any further
                    return
            #needed for the next iteraton
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        return
