
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        nodes = []
        nodes.append(str(self.val))
        node = self

        while node.next:
            node = node.next
            nodes.append(str(node.val))

        print(" -> ".join(nodes))

def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next

def create_single_linked_list(arr):
    next = None
    for key, value in enumerate(reversed(arr)):
        next = ListNode(value, next)

    return next

l1 = create_single_linked_list([1,2,3,4,5,6])
reverse_sublist(l1, 3, 5).print()