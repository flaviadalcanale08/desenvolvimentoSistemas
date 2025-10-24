from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI(
    title="API de Tarefas",
    description="API para realizar consultas de tarefas.",
    version="1.0.0"
)

class Tarefa(BaseModel):
    id: str = uuid.uuid4()
    titulo: str
    descricao: str
    concluida: bool = False


db_tarefa: Dict[int, Tarefa] = { 1: Tarefa(titulo="Estudar para a prova.", descricao="Ler o conteúdo para a prova e fazer exercícios."),
                                 2: Tarefa(titulo="Ir ao mercado", descricao="Ir ao supermercado e comprar itens essenciais."),
                                 3: Tarefa(titulo="Fazer exercícios físicos", descricao="Ir à academia ou fazer exercícios em casa.")}


@app.get("/") 
def read_root():
    return {"message": "Bem-vindo à API de cadastro de tarefas! Acesse /docs para a documentação interativa."}

@app.post("/Tarefas/{id}", status_code=status.HTTP_201_CREATED) #Cadastrando uma nova tarefa.
def criar_tarefa(tarefa: Tarefa, id: int):
    if id in db_tarefa or len(tarefa.titulo) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Esse cadastro está invalido.")
    
    db_tarefa[id] = Tarefa
    return {"message": "A tarefa foi cadastrado com sucesso!", "Tarefa": id, "titulo": Tarefa}

@app.get("/Tarefas", status_code=status.HTTP_200_OK) #Listando todas as tarefas cadastradas.
def todos_as_tarefas():
    return db_tarefa

@app.get("/Tarefas/{id}") #Listando todas as tarefas cadastradas.
def pesquisar_as_tarefas(id: int):
    if id not in db_tarefa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro de tarefa não encontrado.")
    if id in db_tarefa:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Cadastro de tarefa pesquisado foi: {tarefa.titulo}{tarefa.tdescricao}{tarefa.concluida}")

@app.delete("/Tarefas/{id}") #Deletando uma tarefa cadastrada.
def deletar_cadastro(id: int):
    if id not in db_tarefa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro de tarefa não encontrado.")
    del db_tarefa[id]
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
   
@app.put("/Tarefas/{id}") #Atualizando uma tarefa cadastrada.
def atualizar_tarefa(id: int, tarefa: Tarefa):
    if id not in db_tarefa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro de tarefa não encontrado.")
    
    if id in db_tarefa and len(tarefa.titulo) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Título inválido.")
    
    db_tarefa[id] = tarefa
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Cadastro de tarefa atualizado com sucesso. Sua tarefa é: {tarefa.titulo}")
