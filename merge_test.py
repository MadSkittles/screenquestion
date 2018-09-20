import os
import unittest
from typing import List

from merge import Node, merge


def list_to_linked_list(l: List[int]) -> Node:
    """
    Convert list to linked list

    :param l: the list to be converted
    :return: a linked list, equivalent to l
    """
    if not l:
        return None
    head = p = Node(l[0])
    for n in l[1:]:
        p.next = Node(n)
        p = p.next
    return head


def check_answer(answer: Node, expect_answer: Node) -> bool:
    """
    Check whether the answer of merge function is correct

    :param answer: the answer of merge
    :param expect_answer: the correct answer
    :return: whether answer if correct
    """
    p1, p2 = answer, expect_answer
    while p1 is not None and p2 is not None:
        if p1.data != p2.data:
            return False
        p1, p2 = p1.next, p2.next
    return p1 == p2


def read_testcases(testcase_id):
    """
    Read testcases from files

    :return: a tuple with three elements, two linked list as input of merge and a linked list as the answer for checking 
    """
    testcases_dir = os.path.join(os.path.dirname(__file__), "testcases")
    testcase_file=os.path.join(testcases_dir, "{}.txt".format(testcase_id))

    with open(testcase_file, "r") as f:
        input_list1, input_list2, input_list3 = (
                f.readline().strip().split(" "),
                f.readline().strip().split(" "),
                f.readline().strip().split(" "),
            )
        list1, list2, answer = (
                [int(n) for n in input_list1 if n],
                [int(n) for n in input_list2 if n],
                [int(n) for n in input_list3 if n],
            )
    return (list_to_linked_list(list1), list_to_linked_list(list2), list_to_linked_list(answer))


class MergeFuncTestCase(unittest.TestCase):
    def test_merge_1(self):
        """
        Unit test for merge function

        len(list1) = len(list2) = 0
        """
        list1, list2, expect_answer = read_testcases(1)
        answer = merge(list1, list2)
        self.assertTrue(check_answer(answer, expect_answer))

    def test_merge_2(self):
        """
        Unit test for merge function

        len(list1) > 0
        len(list2) = 0
        """
        list1, list2, expect_answer = read_testcases(2)
        answer = merge(list1, list2)
        self.assertTrue(check_answer(answer, expect_answer))

    def test_merge_3(self):
        """
        Unit test for merge function

        len(list1) > 0
        len(list2) = 0
        """
        list1, list2, expect_answer = read_testcases(3)
        answer = merge(list1, list2)
        self.assertTrue(check_answer(answer, expect_answer))

    def test_merge_4(self):
        """
        Unit test for merge function

        len(list1) > len(list2) > 0
        """
        list1, list2, expect_answer = read_testcases(4)
        answer = merge(list1, list2)
        self.assertTrue(check_answer(answer, expect_answer))

    def test_merge_5(self):
        """
        Unit test for merge function

        len(list2) > len(list1) > 0
        """
        list1, list2, expect_answer = read_testcases(5)
        answer = merge(list1, list2)
        self.assertTrue(check_answer(answer, expect_answer))

    def test_merge_6(self):
        """
        Unit test for merge function

        len(list1) = len(list2) > 0
        """
        list1, list2, expect_answer = read_testcases(6)
        answer = merge(list1, list2)
        self.assertTrue(check_answer(answer, expect_answer))



if __name__ == "__main__":
    unittest.main()
