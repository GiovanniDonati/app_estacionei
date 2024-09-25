from fastapi import FastAPI
from models.Vaga import Vaga
from models.Veiculo import Veiculo
from models.Client import Cliente
from controller.schemas import VagaModel, Veiculo, Cliente

app = FastAPI()

# Rotas para vagas
@app.get("/vagas", tags=["Vagas"])
def listar_vagas(): return Vaga.listar_vagas()

@app.get("/vagas/{vaga}", tags=["Vagas"])
def buscar_vaga(Vaga: VagaModel): return Vaga.verificar_disponibilidade()

@app.post("/vagas", tags=["Vagas"])
def adicionar_vaga(Vaga: VagaModel): return Vaga.adicionar_vaga()

@app.delete("/vagas/{vaga}", tags=["Vagas"])
def remover_vaga(Vaga: VagaModel): return Vaga.remover_vaga()