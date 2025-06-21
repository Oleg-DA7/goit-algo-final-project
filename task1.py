# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# 1. написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# 2. розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# 3. написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            if cur is None:
                return
            prev.next = cur.next
            cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def merge_sort(self):
        self.head = self._merge_sort(self.head)
    
    def _merge_sort(self, head):
        if (not head) or (not head.next):
            return head

        middle = self._get_middle(head)
        next_from_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_from_middle)

        return self._merge(left, right)

    def _get_middle(self, head):
        if head is None:
            return head

        n = head
        s = head
        while s.next and s.next.next:
            n = n.next
            s = s.next.next
        return n

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else: 
            result = right
            result.next = self._merge(left, right.next)

        return result
    
    def reverse_list(self):
        cur = self.head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
        return None
    
    def merge_sorted_list(self, list_to_add):
        tmpNode = Node(0)
        tmpStartNode = tmpNode
        l1 = self.head
        l2 = list_to_add.head
        
        while l1 and l2:
            if l1.data <= l2.data:
                tmpNode.next = l1
                l1 = l1.next
            else: 
                tmpNode.next = l2
                l2 = l2.next
            tmpNode = tmpNode.next
        
        if l1:
            tmpNode.next = l1

        if l2:
            tmpNode.next = l2

        resultList = LinkedList()
        resultList.head = tmpStartNode.next
        return resultList
        

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

print("Реверсування однозв'язного списку:")
llist.reverse_list()
llist.print_list()

print("Сортування однозв'язного списку:")
llist.merge_sort()
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

llist2 = LinkedList()
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(4)
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(2)
llist2.merge_sort()

merged_sorted_lists = llist.merge_sorted_list(llist2)
merged_sorted_lists.print_list()
