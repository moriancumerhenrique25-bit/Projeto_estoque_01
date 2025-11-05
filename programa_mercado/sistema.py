# CLASSE SISTEMA
class Sistema:

    # METODO CONSTRUTOR
    def __init__(self):
        self.ativo = True
        self.produto = {
            1: {"nome": "morango", "quantidade": 20, "valor": 15, "kilo": 150},
            2: {"nome": "manga", "quantidade": 15, "valor": 10, "kilo": 5},
            3: {"nome": "limao", "quantidade": 30, "valor": 5, "kilo": 3},
            4: {"nome": "maracuja", "quantidade": 50, "valor": 10, "kilo": 6},
            5: {"nome": "kiwi", "quantidade": 20, "valor": 20, "kilo": 10},
            6: {"nome": "abacate", "quantidade": 40, "valor": 12, "kilo": 10},
            7: {"nome": "abacaxi", "quantidade": 30, "valor": 35, "kilo": 10},
            8: {"nome": "mamao", "quantidade": 20, "valor": 10, "kilo": 20},
            9: {"nome": "laranja", "quantidade": 60, "valor": 10, "kilo": 30},
            10: {"nome": "ameixa", "quantidade": 10, "valor": 15, "kilo": 6},
        }

    #METODO DE AÇÃO
    def somar(self, kilo, quantidade):
        return kilo * quantidade