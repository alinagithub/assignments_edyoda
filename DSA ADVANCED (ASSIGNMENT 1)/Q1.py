
#Q1:Delete the elements in an linked list whose sum is equal to zero
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_zero_sum_nodes(head):
    dummy = ListNode(0)  # Create a dummy node to simplify the deletion process
    dummy.next = head
    prefix_sum = 0  # Initialize a variable to store the prefix sum
    prefix_sums = {}  # Use a dictionary to store the prefix sums and their corresponding node

    # Traverse the linked list and calculate the prefix sum
    current = dummy
    while current is not None:
        prefix_sum += current.val

        # If the prefix sum already exists in the dictionary, delete the nodes between the same prefix sums
        if prefix_sum in prefix_sums:
            prev = prefix_sums[prefix_sum]
            prev.next = current.next

        else:
            prefix_sums[prefix_sum] = current

        current = current.next

    return dummy.next

# Example usage
# Create a linked list: 1 -> 2 -> -3 -> 3 -> -2 -> None
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(-3)
node3 = ListNode(3)
node4 = ListNode(-2)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

print("Original linked list:")
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")

head = delete_zero_sum_nodes(head)

print("Linked list after deleting zero sum nodes:")
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")