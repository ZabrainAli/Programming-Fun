from ListNode import ListNode

def mergeTwoLists(list1, list2):
    """
    :type list1: [ListNode]
    :type list2: [ListNode]
    :rtype: [ListNode]
    """
    print("List1:")
    list1.print_node()
    print("\nList2:")
    list2.print_node()


    if list1.val >= list2.val:
        mergedList = ListNode(list2.val)
        list2 = list2.next
    else:
        mergedList = ListNode(list1.val)
        list1 = list1.next

    tmp1 = list1
    tmp2 = list2

    while tmp1 != None and tmp2 != None:
        if tmp1.val >= tmp2.val:
            mergedList.add_node_to_end(tmp2.val)
            tmp2 = tmp2.next
        else:
            mergedList.add_node_to_end(tmp1.val)
            tmp1 = tmp1.next

    if tmp1 == None:
        while tmp2 != None:
            mergedList.add_node_to_end(tmp2.val)
            tmp2 = tmp2.next
    elif tmp2 == None:
        while tmp1 != None:
            mergedList.add_node_to_end(tmp1.val)
            tmp1 = tmp1.next

    return mergedList
    

def main():
    list1 = ListNode(6)
    list1.add_node_to_end(7)
    list1.add_node_to_end(9)
    list1.add_node_to_end(11)
    
    list2 = ListNode(1)
    list2.add_node_to_end(3)
    list2.add_node_to_end(6)

    sol = mergeTwoLists(list1, list2)

    print("\nMerged List:")
    sol.print_node()

main()