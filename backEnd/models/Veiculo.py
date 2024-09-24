class Veiculo:
    def __init__(self, placa, modelo, dono, tipo_veiculo):
        self.placa = placa
        self.modelo = modelo
        self.dono = dono
        self.tipo_veiculo = tipo_veiculo
    
    def adicionar_veiculo(self):
        pass
    
    def remover_veiculo(self):
        pass
    
    def atualizar_veiculo(self):
        pass
    
    def listar_veiculos(self):
        pass
    
    def buscar_veiculo(self):
        pass
    
    def __str__(self):
        return f"Veículo {self.modelo} de placa {self.placa}"