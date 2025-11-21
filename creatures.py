from creature_base_class import Creature

class Dragon(Creature):

    def __init__(self):
        super().__init__(
            name="Dragão", 
            health=80,  
            attack_power=15, 
            defense=5, 
            speed=3, 
            crit_chance=0.15,
            )
        self.skills = ["fire_breath"] 
    
    def fire_breath(self, target):
        """Ignora a defesa do oponente"""
        base_damage = self.attack_power
        target.take_damage(base_damage)
        print(f"🔥 {self.name} usou Sopro de Fogo em {target.name} causando {base_damage} de dano!")

class Wolf(Creature):

    def __init__(self):
        super().__init__(
            name="Lobo", 
            health=50,  
            attack_power=10, 
            defense=2, 
            speed=14, 
            crit_chance=0.10, 
            )
        self.skills = ["quick_bite"] 
    def quick_bite(self, target):
        """Dá duas mordidas rápidas"""
        print(f"🐾 {self.name} usou Mordida Rápida!")
        for _ in range(2):
            super().attack(target)
        
class Wizard(Creature):

    def __init__(self):
        super().__init__(
            name="Mago", 
            health=35,  
            attack_power=12, 
            defense=1, 
            speed=6, 
            crit_chance=0.25, 
            )
        self.skills = ["fireball"] 
    
    def fireball(self, target):
        """Magia que ignora a defesa e pode critar separadamente"""
        base_damage = self.attack_power

        if self.is_critic():
            base_damage *= 2
            print(f"💥 {self.name} lançou uma Bola de Fogo CRÍTICA!")

        target.take_damage(base_damage)
        print(f"🔥 {self.name} lançou Bola de Fogo causando {base_damage} de dano!")