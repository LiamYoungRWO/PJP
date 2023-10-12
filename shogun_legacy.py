import random

class Warrior:
    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack(self, opponent):
        damage = self.strength - opponent.defense
        opponent.health -= max(0, damage)  # Ensure health does not go negative

    def is_alive(self):
        return self.health > 0


def battle(warrior1, warrior2):
    turn = random.choice([warrior1, warrior2])  # Randomly choose who goes first
    
    while warrior1.is_alive() and warrior2.is_alive():
        if turn == warrior1:
            warrior1.attack(warrior2)
            turn = warrior2
        else:
            warrior2.attack(warrior1)
            turn = warrior1
    
    # Determine and print the battle outcome
    if warrior1.is_alive():
        print(f"{warrior1.name} emerges victorious with {warrior1.health} health remaining!")
    else:
        print(f"{warrior2.name} emerges victorious with {warrior2.health} health remaining!")


if __name__ == "__main__":
    samurai = Warrior("Samurai", strength=15, defense=5, health=100)
    ninja = Warrior("Ninja", strength=12, defense=8, health=100)
    
    print("Battle Commences: Samurai vs Ninja")
    battle(samurai, ninja)
