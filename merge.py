class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(head1, head2):
    """
    Merge two sorted linked lists

    :param head1: the head of the first sorted linked lists
    :param head2: the head of the second sorted linked lists
    :return: the head of the result
    """
    p1, p2 = head1, head2
    pre_result_head = p = Node(None)

    while p1 is not None and p2 is not None:
        if p1.data < p2.data:
            p.next, p1 = p1, p1.next
        else:
            p.next, p2 = p2, p2.next
        p = p.next
    p.next = p1 or p2
    
    result_head = pre_result_head.next
    del pre_result_head

    return result_head
