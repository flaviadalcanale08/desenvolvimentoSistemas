from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="API de Cadastro de Alunos",
    description="API para realizar cadastro de alunos.",
    version="1.0.0"
)

class Cadastro(BaseModel):
    matricula: int  
    nome: str
    turma: str
    idade: int

db_cadastro: Dict[int, Cadastro] = {
    1: Cadastro(matricula=4553692090, nome="Flávia Moretto Dalcanale", turma="2° 03", idade=17),
    2: Cadastro(matricula=4541979666, nome="Anna Beatriz Girardi Borchardt", turma="2° 03", idade=16),
    3: Cadastro(matricula=4553683740, nome="Beatriz Borges de Lima", turma="2° 03", idade=16),
}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de cadastro de alunos! Acesse /docs para a documentação interativa."}

@app.post("/Cadastro/{id}", status_code=status.HTTP_201_CREATED)
def criar_cadastro(id: int, cadastro: Cadastro):
    if id in db_cadastro:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Esse cadastro já existe")
    db_cadastro[id] = cadastro
    return {"message": "Aluno cadastrado com sucesso!", "Matricula": id, "nome": cadastro}

@app.get("/Cadastro")
def todos_os_cadastros():
    return db_cadastro

@app.put("/Cadastro/{id}")
def atualizar_cadastro(id: int, cadastro: Cadastro):
    if id not in db_cadastro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro não encontrado")
    db_cadastro[id] = cadastro
    return {"message": "Cadastro do aluno atualizado com sucesso!", "Cadastro": cadastro}

@app.delete("/cadastro/{id}")
def deletar_cadastro(id: int):
    if id not in db_cadastro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro não encontrado")
    del db_cadastro[id]
    return {"message": "Cadastro deletado com sucesso!"}
