class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_element = Node(new_data)
        if self.head is None:
            self.head = new_element
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_element

    def delete(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        present = self.head
        while present is not None:
            if present.item == key:
                return True
            present = present.next
        return False

    def print(self):
        temp = self.head
        while temp:
            print(str(temp.item), end=" ")
            temp = temp.next

    def task_one(self, key):
        # Знаходження позиції ключа
        count = 0
        present = self.head
        while present is not None:
            if present.item != key:  # може бути декілька однакових значень
                count += 1
                present = present.next
            else:
                break
        # Видалення елемента за ключем
        position = count
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            return
        for i in range(position - 1):  # 2
            temp = temp.next  # temp.next = 3, temp -> 3
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next  # next -> temp.next.next (5)
        temp.next = next    # наступний за temp(temp.next) -> 5. 4 вилітає

        # Заміна елементів
        position = count
        buf_0 = self.head
        for i in range(position - 1):
            buf_0 = buf_0.next
        if buf_0.next is None:
            return
        buf_0.next.item, buf_0.item = buf_0.item, buf_0.next.item

if __name__ == '__main__':
    list_1 = LinkedList()
    list_1.add(0)
    list_1.add(1)
    list_1.add(2)
    list_1.add(3)
    list_1.add(4)
    list_1.add(5)
    list_1.add(6)
    list_1.add(7)
    list_1.print()
    print("\nTASK1:")
    list_1.task_one(4)
    list_1.print()
    print("\n...")
