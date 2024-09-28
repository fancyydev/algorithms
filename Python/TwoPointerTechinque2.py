# En este ejemplom a partir de dos listas normales cree una linked list 
# Utilizando 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: list[int], list2: list[int]):
        p1 = 0
        p2 = 0
        node_principal = None
        node_antiguo = None
        
        if not list1 and not list2:
            return None  

        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] < list2[p2]:
                if node_antiguo is None:
                    node_antiguo = ListNode(list1[p1])
                    node_principal = node_antiguo
                else:
                    node_actual = ListNode(list1[p1])
                    node_antiguo.next = node_actual
                    node_antiguo = node_actual
                p1 += 1
            else:
                if node_antiguo is None:
                    node_antiguo = ListNode(list2[p2])
                    node_principal = node_antiguo
                else:
                    node_actual = ListNode(list2[p2])
                    node_antiguo.next = node_actual
                    node_antiguo = node_actual
                p2 += 1
        
        while p1 < len(list1):
            node_actual = ListNode(list1[p1])
            if node_antiguo:
                node_antiguo.next = node_actual
            else:
                node_principal = node_actual 
            node_antiguo = node_actual
            p1 += 1

        while p2 < len(list2):
            node_actual = ListNode(list2[p2])
            if node_antiguo:
                node_antiguo.next = node_actual
            else:
                node_principal = node_actual  
            node_antiguo = node_actual
            p2 += 1

        return node_principal


# a = []
# b = []
# Respuesta esperada []

# a = []
# b = [0]
# Respuesta esperada [0]

# a = [0]
# b = []
# Respuesta esperada [0]

a = [1,2,4]
b = [1,3,4]

solution = Solution()
node = solution.mergeTwoLists(a,b)
print(node.val)

while node.next != None:
    node = node.next
    print(node.val)
