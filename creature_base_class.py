from random import random
class Creature:
    def __init__(self, name:str, health:int, attack_power:int, defense:int, speed:int, crit_chance:float):

        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
        self.crit_chance = crit_chance
        self.inventory = []
        self.buffs = []
        
        
    def is_alive(self):
        return self.health > 0


    def get_status(self):
        print(f"{self.name} — HP: {self.health}/{self.max_health}")


    def is_critic(self):
        roll = random()
        return roll <= self.crit_chance


    def calculate_damage(self, target):
        base_damage = self.attack_power

        final_damage = max(1, base_damage - target.defense)

        if self.is_critic():
            final_damage *= 2
            return final_damage, True
        else:
            return final_damage, False

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


    def attack(self, target):
        damage, critical = self.calculate_damage(target)
        
        target.take_damage(damage)

        if critical:
            print(f"💥 {self.name} acertou um CRÍTICO em {target.name} causando {damage} de dano!")
        else:
            print(f"{self.name} atacou {target.name} causando {damage} de dano.")
    

    def list_skills(self):
        for i in range(len(self.skills)):
            print(f"{i + 1}. {self.skills[i]}\n")
    
    def list_items(self):
        for i in range(len(self.inventory)):
            print(f"{i + 1}. {self.inventory[i].name}\n")