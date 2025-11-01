from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        node_map = {}
        node_list = []

        c = 0
        node = head
        while node:
            node_map[node] = c
            
            node_list.append(Node(node.val))
            if c > 0:
                node_list[-2].next = node_list[-1]

            c += 1
            node = node.next

        c = 0
        node = head
        while node:
            if node.random:
                index_random = node_map[node.random]
                node_list[c].random = node_list[index_random]

            c += 1
            node = node.next

        return node_list[0]


head = Node(2, random=None)
head.next = Node(3, random=head)
head.next.next = Node(4, random=None)

# ____<___       ___>___
# |      |      |       |
# 2 ---> 3 ---> 4 ---> null
# |_________>___________| 
 
s = Solution()
print(s.copyRandomList(head))

