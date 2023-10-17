class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



head= ListNode(0)

curr_node = head

curr_node.next = ListNode(1)
curr_node=curr_node.next

curr_node.next = ListNode(2)
curr_node=curr_node.next

curr_node.next = ListNode(3)
curr_node=curr_node.next

curr_node.next = ListNode(4)
curr_node=curr_node.next

node = head

def find_add(node,target,value):
    while node:
        if node.val == target:
            location = node.next
            node.next = ListNode(value)
            node = node.next
            node.next = location

        node=node.next

find_add(node,3,11)

while node:
    print(node.val)
    node=node.next

# val 이 target 인 연결 리스트 뒤에 value 가 new_value 인 노드를 추가하고 싶다면

