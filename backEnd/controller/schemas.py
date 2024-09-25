from models.Vaga import Vaga
from models.Veiculo import Veiculo
from models.Client import Cliente
from pydantic import BaseModel

#Criar as BaseModel
class VagaModel(BaseModel):
    vaga: str
    tipo_vaga: str

class Veiculo(BaseModel):
    placa: str
    modelo: str
    dono: str
    tipo_veiculo: str

class Cliente(BaseModel):
    nome: str
    cpf: str
    telefone: str