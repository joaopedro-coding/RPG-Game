from random import random, randint
class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_turn = 0


    def start_battle(self):
        # determinar quem começa
        if self.player.speed == self.enemy.speed:
            self.current_turn = 0 if random() < 0.5 else 1
        else:    
            self.current_turn = 0 if self.player.speed > self.enemy.speed else 1
        
        while self.player.is_alive() and self.enemy.is_alive():
            self.print_status()

            # Começando os turnos
            if self.current_turn == 0:
                self.player_turn()
            else:
                self.enemy_turn()
            
            self.current_turn = 1 - self.current_turn
            print("\n" + "="*40 + "\n")


        self.print_status()
        print("Batalha encerrada!")


    def print_status(self):
        self.player.get_status()
        self.enemy.get_status()  
    

    def player_turn(self):
        print("=== Sua vez, escolha uma ação ===")
        print("1. Atacar\n2. Habilidade\n3. Item")
        choice = input("O que o usuário gostaria de fazer?")
        
        while choice not in ["1", "2", "3"]:
            print("Por favor escolha uma ação do menu.")
            print("1. Atacar\n2. Habilidade\n3. Item")
            choice = input("O que o usuário gostaria de fazer?")
                           
        if choice == "1":
            self.player.attack(self.enemy)
        elif choice == "2":
            print("=== Lista de Habilidades ===")
            self.player.list_skills()
            while True:
                try:
                    skill_choice = self.player.skills[int(input("=== Escolha qual habilidade deseja usar ===")) - 1]
                    break
                except (ValueError, IndexError):
                    print("Por favor escolha um número dentro do intervalo descrito")
                    self.player.list_skills()
            player_skill = getattr(self.player, skill_choice)
            player_skill(self.enemy)
        elif choice == "3":
            if self.player.inventory == []:
                print("O jogador não possui itens em seu inventario.")
            else:
                print("=== Lista de Itens ===")
                self.player.list_items()
                while True:
                    try:
                        item_choice = int(input("Escolha um item para ser usado!"))
                        if 1 <= item_choice <= len(self.player.inventory):
                            break
                        else:
                            print("Escolha um item do menu!")
                    except ValueError:
                        print("Digite apenas números!")
                
                item = self.player.inventory[item_choice - 1]
                item.use(self.player)

        self.check_victory()
    

    def enemy_turn(self):
        print(f"=== Turno do {self.enemy.name} ===")
        random_prob = random()
        if random_prob < 0.7:
            self.enemy.attack(self.player)
        else:
            random_special_skill = self.enemy.skills[randint(0, len(self.enemy.skills) - 1)]
            skill_method = getattr(self.enemy, random_special_skill)
            skill_method(self.player)
    
        self.check_victory()


    def check_victory(self):
        if not self.player.is_alive():
            print(f"Vitória para {self.enemy.name}!")
        elif not self.enemy.is_alive():
            print(f"Vitória para {self.player.name}!")
