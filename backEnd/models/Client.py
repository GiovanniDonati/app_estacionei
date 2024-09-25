from database.config import conn, cursor

class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        
    def cadastrar_cliente(self):
        try:
            cursor.execute("INSERT INTO cliente (nome, cpf, telefone) VALUES (?, ?, ?)", (self.nome, self.cpf, self.telefone))
            conn.commit()
            return True
        except:
            return False
        
    def remover_cliente(self):
        try:
            cursor.execute("DELETE FROM cliente WHERE cpf = ?", (self.cpf,))
            conn.commit()
            return True
        except:
            return False
    
    def atualizar_cliente(self):
        try:
            cursor.execute("UPDATE cliente SET nome = ?, telefone = ? WHERE cpf = ?", (self.nome, self.telefone, self.cpf))
            conn.commit()
            return True
        except:
            return False
    
    def listar_clientes(self):
        try:
            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()
            return clientes
        except:
            return None
    
    def buscar_cliente(self):
        try:
            cursor.execute("SELECT * FROM cliente WHERE cpf = ?", (self.cpf,))
            cliente = cursor.fetchone()
            return cliente
        except:
            return None
    
    def __str__(self):
        return f"Cliente {self.nome} com CPF {self.cpf}"