from database.config import conn, cursor

class Veiculo:
    def __init__(self, placa, modelo, dono, tipo_veiculo):
        self.placa = placa
        self.modelo = modelo
        self.dono = dono
        self.tipo_veiculo = tipo_veiculo
    
    def adicionar_veiculo(self):
        try:
            cursor.execute("INSERT INTO veiculo (placa, modelo, dono, tipo_veiculo) VALUES (?, ?, ?, ?)", (self.placa, self.modelo, self.dono, self.tipo_veiculo))
            conn.commit()
            return True
        except:
            return False
    
    def remover_veiculo(self):
        try:
            cursor.execute("DELETE FROM veiculo WHERE placa = ?", (self.placa,))
            conn.commit()
            return True
        except:
            return False
    
    def atualizar_veiculo(self):
        try:
            cursor.execute("UPDATE veiculo SET modelo = ?, dono = ?, tipo_veiculo = ? WHERE placa = ?", (self.modelo, self.dono, self.tipo_veiculo, self.placa))
            conn.commit()
            return True
        except:
            return False
    
    def listar_veiculos(self):
        try:
            cursor.execute("SELECT * FROM veiculo")
            veiculos = cursor.fetchall()
            return veiculos
        except:
            return None
    
    def buscar_veiculo(self):
        try:
            cursor.execute("SELECT * FROM veiculo WHERE placa = ?", (self.placa,))
            veiculo = cursor.fetchone()
            return veiculo
        except:
            return None
    
    def __str__(self):
        return f"Veículo {self.modelo} de placa {self.placa}"