class Item:
    def __init__(self, name:str, quantity: int):
        self.name = name
        self.quantity = quantity


    def use(self, target):
        """Método que aplica certos efeitos dependendo do item"""
        raise NotImplementedError("Implemente o método em subclasses")
        