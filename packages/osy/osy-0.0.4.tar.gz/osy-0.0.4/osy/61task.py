"""Даны 2 кольцевых списка: фамилии участников розыгрыша и названия
призов. Выиграет n человек (каждый k-й). Число для пересчета призов - t."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        nodes = []
        temp = self.head
        if self.head:
            while True:
                nodes.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        print(" -> ".join(nodes))

    def select_every_kth(self, k, n):
        selected = []
        if not self.head:
            return selected

        current = self.head
        prev = None

        while len(selected) < n:
            count = 1
            while count < k:
                prev = current
                current = current.next
                count += 1

            selected.append(current.data)
            prev.next = current.next  # Remove the selected node from the circle
            current = current.next  # Move to the next node

            if current == self.head:  # If we have completed a full circle, update head
                self.head = current.next

        return selected


# Создание кольцевого списка с фамилиями участников и названиями призов
participants = CircularLinkedList()
participants.append("Participant1")
participants.append("Participant2")
participants.append("Participant3")
participants.append("Participant4")
participants.append("Participant5")

prizes = CircularLinkedList()
prizes.append("Prize1")
prizes.append("Prize2")
prizes.append("Prize3")
prizes.append("Prize4")
prizes.append("Prize5")

print("Participants:")
participants.display()

print("Prizes:")
prizes.display()

# Ввод значений k, n и t
k = int(input("Enter the value of k (every k-th participant wins): "))
n = int(input("Enter the number of winners (n): "))
t = int(input("Enter the value of t for prize distribution: "))

# Жеребьевка участников
winners = participants.select_every_kth(k, n)

# Распределение призов
prize_distribution = []
current_prize_node = prizes.head

for i in range(n):
    prize_distribution.append((winners[i], current_prize_node.data))
    count = 1
    while count < t:
        current_prize_node = current_prize_node.next
        count += 1

print("\nWinners and their prizes:")
for winner, prize in prize_distribution:
    print(f"{winner} wins {prize}")
