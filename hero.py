class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print("Hero's name:", self.name)

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Arthas Menethil", "Lich King", "Necromancy", 25000, "Your desperate screams will serve as proof of my infinite power. I will let you live to see the end. I cannot allow the greatest servant of the Light to miss the birth of MY world.")
hero.display_name()
print("Initial health:", hero.health_points)
hero.double_health()
print("Doubled health:", hero.health_points)
print(hero)
print("Length of catchphrase:", len(hero.catchphrase))