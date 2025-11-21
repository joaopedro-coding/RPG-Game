from creatures import Dragon, Wizard, Wolf
from items import HealingPotion, AttackBuff
from gaming_system import Battle

# Supondo que você já tenha a classe Creature
player = Dragon()
potion = AttackBuff(amount=10, quantity=2)
player.inventory.append(potion)


enemy = Wizard()
# Testando o uso
battle = Battle(player, enemy)
battle.start_battle()