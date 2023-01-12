"""
File: add2.py
Name:Jacky Wu
------------------------
The function of this program is to make a add digits from two independent listnode and make a new listnode
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # traversal and put listnode value into list
    cur1 = l1
    cur2 = l2
    lst1 = []
    lst2 = []
    while cur1 is not None:
        lst1.append(cur1.val)
        cur1 = cur1.next
    while cur2 is not None:
        lst2.append(cur2.val)
        cur2 = cur2.next

    # read list reversely and save them in a string
    s1 = ""
    s2 = ""
    for i in range(len(lst1)-1, -1, -1):
        s1 += str(lst1[i])
    for i in range(len(lst2)-1, -1, -1):
        s2 += str(lst2[i])
    # make string into integer and add them
    ans = int(s1) + int(s2)
    # make answer from integer to string and save single digit into answer list reversely
    ans = str(ans)
    ans_lst = []
    for i in range(len(ans)-1, -1, -1):
        ans_lst.append(int(ans[i]))

    # make new listnode
    new_head = None
    for i in range(len(ans_lst)):
        if new_head is None:
            new_head = ListNode(ans_lst[i])
            end = new_head
        else:
            end.next = ListNode(ans_lst[i])
            end = end.next
    return new_head


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
