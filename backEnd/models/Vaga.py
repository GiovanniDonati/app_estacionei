class Vaga:
    def __init__(self, numero, tipo_vaga):
        self.numero = numero
        self.tipo_vaga = tipo_vaga
        self.ocupada = False
        self.veiculo = None
        
    def ocupar_vaga(self, veiculo):
        if not self.ocupada:
            self.ocupada = True
            self.veiculo = veiculo
            return True
        else:
            return False
        
    def liberar_vaga(self):
        if self.ocupada:
            self.ocupada = False
            self.veiculo = None
            return True
        else:
            return False
        
    def verificar_disponibilidade(self):
        return not self.ocupada
        
    def __str__(self):
        return f"Vaga {self.numero} ({self.tipo_vaga})"