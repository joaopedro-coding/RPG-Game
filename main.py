from creatures import Dragon, Wizard, Wolf
from buff_base_class import Buff
from gaming_system import Battle

# Supondo que você já tenha a classe Creature
player = Dragon()
atk_buff = Buff(name="Buff de Ataque", duration=3, effect="attack", amount=5)
def_buff = Buff(name="Buff de Defesa", duration=2, effect="defense", amount=3)
player.buffs.append(atk_buff)
player.buffs.append(def_buff)

enemy = Dragon()
# Testando o uso
battle = Battle(player, enemy)
battle.start_battle()