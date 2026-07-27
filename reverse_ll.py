from typing import Optional


class Node:
    def __init__(self, val: int=0, next: Optional['Node'] = None):
        self.val = val
        self.next = next


def reverseList(head: Optional[Node]) -> Optional[Node]:
    dummy = Node()
    current = head
    while current:
        # 4 -> 5
        # dummy -> 3 -> 2 -> 1
        next_node = current.next
        current.next = dummy.next
        dummy.next = current
        current = next_node
    return dummy.next


def reverseListRecursive(head: Optional[Node]) -> Optional[Node]:
    # 1
    if head is None or head.next is None:
        return head
    # 5 -> 4 -> 3 -> 2
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


def _createLinkedList(length: int) -> Optional[Node]:
    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    dummy = Node()
    current = dummy

    for i in range(length):
        new_node = Node(i)
        current.next = new_node
        current = current.next
    
    return dummy.next


def _printLinkedList(head: Optional[Node]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    # Reversing the linked list iteratively
    reversed_head_iterative = reverseList(_createLinkedList(6))
    
    # Reversing the linked list recursively
    reversed_head_recursive = reverseListRecursive(_createLinkedList(6))
    
    # Printing the reversed lists
    print("Iteratively reversed list:")
    _printLinkedList(reversed_head_iterative)

    print("Recursively reversed list:")
    _printLinkedList(reversed_head_recursive)