class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        
    def cadastrar_cliente(self):
        pass
    
    def remover_cliente(self):
        pass
    
    def atualizar_cliente(self):
        pass
    
    def listar_clientes(self):
        pass
    
    def buscar_cliente(self):
        pass
    
    def __str__(self):
        return f"Cliente {self.nome} com CPF {self.cpf}"