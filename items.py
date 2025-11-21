from item_base_class import Item

class HealingPotion(Item):
    def __init__(self, amount=20, duration=0, quantity=1):
        super().__init__(
            name="Poção de Cura", 
            quantity=quantity
            )
        self.amount = amount
        self.duration = duration
    
    
    def use(self, target):
        if self.quantity <= 0:
            print(f"Você não tem mais {self.name}!")
            return False
        elif target.health <= 0:
            print("Não é possível curar o jogador.")
        
        target.health = min(target.health + self.heal_amount, target.max_health)
        self.quantity -= 1
        print(f"{target.name} usou {self.name} e recuperou {self.heal_amount} de HP!")
        return True

class AttackBuff(Item):
    def __init__(self, amount=5, duration=3, quantity=1):
        super().__init__(name="Poção de Ataque", quantity=quantity)
        self.amount = amount
        self.duration = duration
    

    def use(self, target):
        if self.quantity <= 0:
            print(f"Você não tem mais {self.name}!")
            return False

        target.attack_power += self.amount
        self.quantity -= 1

        # Implementar futurante buffs ativos por aqui

        print(f"{target.name} usou {self.name} e aumentou o ataque em {self.amount} por {self.duration} turnos!")
        return True