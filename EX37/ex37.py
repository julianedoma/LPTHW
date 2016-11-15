#example from real world: choose winner randomly
import random
potential_winners = ["Julia", "Caro", "Maxim", "Marc", "Thorben", "Enrico", "Lea", "Callee", "Sam", "Gitta"]
winners = []

while len(winners) == 2:
    winner = random.choice(potential_winners)
    potential_winners.remove(winner)
    winners.append(winner)
    print winners
