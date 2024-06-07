""""Даны 2 кольцевых списка с фамилиями шахматистов 2-х команд.
Произвести жеребьевку. В первой команде выбирается каждый n-й игрок, а во
второй - каждый k-й."""


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

    def select_every_nth(self, n):
        selected = []
        if not self.head:
            return selected

        current = self.head
        prev = None

        while True:
            count = 1
            while count < n:
                prev = current
                current = current.next
                count += 1

            selected.append(current.data)
            prev.next = current.next  # Remove the selected node from the circle
            current = current.next  # Move to the next node

            if current == self.head:  # If we have completed a full circle, break
                break

        return selected


# Создание двух кольцевых списков с фамилиями шахматистов двух команд
team1 = CircularLinkedList()
team1.append("Player1_Team1")
team1.append("Player2_Team1")
team1.append("Player3_Team1")
team1.append("Player4_Team1")

team2 = CircularLinkedList()
team2.append("Player1_Team2")
team2.append("Player2_Team2")
team2.append("Player3_Team2")
team2.append("Player4_Team2")

print("Team 1:")
team1.display()

print("Team 2:")
team2.display()

# Ввод значений n и k
n = int(input("Enter the value of n for Team 1: "))
k = int(input("Enter the value of k for Team 2: "))

# Жеребьевка
selected_team1 = team1.select_every_nth(n)
selected_team2 = team2.select_every_nth(k)

print(f"Selected players from Team 1 (every {n}-th): {selected_team1}")
print(f"Selected players from Team 2 (every {k}-th): {selected_team2}")