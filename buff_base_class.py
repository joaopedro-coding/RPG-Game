class Buff:
    def __init__(self, name:str, duration:int, effect: str, amount:int=0):
        self.name = name
        self.duration = duration
        self.effect = effect
        self.amount = amount

    # def use(self, target):
    #     """Método que aplica certos efeitos dependendo do item"""
    #     raise NotImplementedError("Implemente o método em subclasses")


# class BuffAtack(Buff):
#     def __init__(self, amount, duration=3):
#         super().__init__(name="Buff de Ataque", duration=duration, effect="attack", amount=amount)
    