from database.config import conn, cursor

class Vaga:
    def __init__(self, vaga, tipo_vaga):
        self.vaga = vaga
        self.tipo_vaga = tipo_vaga
        self.ocupada = False
        self.veiculo = None
        
    def adicionar_vaga(self):
        try:
            cursor.execute("INSERT INTO estacionamento (vaga, tipo_vaga) VALUES (?, ?)", (self.vaga, self.tipo_vaga))
            conn.commit()
            return True
        except Exception as e:
            return e
            
    
    def remover_vaga(self):
        try:
            cursor.execute("DELETE FROM estacionamento WHERE vaga = ?", (self.vaga))
            conn.commit()
            return True
        except Exception as e:
            return e
        
    def atualizar_vaga(self):
        try:
            cursor.execute("UPDATE estacionamento SET vaga = ? WHERE vaga = ?",
                (self.vaga, self.vaga))
        except Exception as e:
            return e
        
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