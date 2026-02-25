class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def damage(self, amount):
        self.health -= amount
        print(f"{self.name} lost {amount} health!")
        print(f"Current health: {self.health}")

    def is_alive(self):
        return self.health > 0