class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_node(self):
        print(self.val)
        current_node = self.next
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next

    def add_node_to_end(self, val):
        new_node = ListNode(val)
        if self.next == None:
            self.next = ListNode(val)
            return

        current_node = self.next
        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = new_node