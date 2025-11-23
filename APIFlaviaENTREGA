from fastapi import FastAPI,from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI(
    title="API de Tarefas",
    description="API para realizar consultas de tarefaa.",
    version="1.0.0"
)

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False


db_tarefa: Dict[str, Tarefa] = { str(uuid.uuid4()): Tarefa(titulo="Estudar para a prova.", descricao="Ler o conteúdo para a prova e fazer exercícios."),
                                 str(uuid.uuid4()): Tarefa(titulo="Ir ao mercado", descricao="Ir ao supermercado e comprar itens essenciais."),
                                 str(uuid.uuid4()): Tarefa(titulo="Fazer exercícios físicos", descricao="Ir à academia ou fazer exercícios em casa.")}


@app.get("/") 
def read_root():
    return {"message": "Bem-vindo à API de cadastro de tarefas! Acesse /docs para a documentação interativa."}

@app.post("/Tarefas/", status_code=status.HTTP_201_CREATED) #Cadastrando uma nova tarefa.
def criar_tarefa(tarefa: Tarefa):
    newid = str(uuid.uuid4())
    if newid in db_tarefa or len(tarefa.titulo) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Esse cadastro está invalido.")
    
    db_tarefa[newid] = tarefa
    return {"message": "A tarefa foi cadastrada com sucesso!", "Tarefa": newid, "titulo": tarefa.titulo, "descricao": tarefa.descricao}

@app.get("/Tarefas", status_code=status.HTTP_200_OK) #Listando todas as tarefas cadastradas.
def todos_as_tarefas():
    return db_tarefa

@app.get("/Tarefas/{id}") #Listando uma tarefa cadastrada.
def buscar_uma_tarefa(id: str):
    tarefa = db_tarefa[id]
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada.")
    else:
        raise HTTPException(status_code=status.HTTP_200_OK, detail=f"A tarefa pesquisada foi: {tarefa.titulo}, {tarefa.descricao}, {tarefa.concluida}")

@app.delete("/Tarefas/{id}") #Deletando uma tarefa cadastrada.
def deletar_tarefa(id: str):
    if id not in db_tarefa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada.")
    del db_tarefa[id]
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
   
@app.put("/Tarefas/{id}") #Atualizando uma tarefa cadastrada.
def atualizar_tarefa(id: str, tarefa: Tarefa):
    if id not in db_tarefa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada.")
    
    if id in db_tarefa and len(tarefa.titulo) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Título inválido.")
    
    db_tarefa[id] = tarefa
    raise HTTPException(status_code=status.HTTP_200_OK, detail=f"Tarefa atualizada com sucesso. Sua tarefa é: {tarefa.titulo}")
    if id in db_tarefa and len(tarefa.titulo) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Título inválido.")
    
    db_tarefa[id] = tarefa
    raise HTTPException(status_code=status.HTTP_200_OK, detail=f"Tarefa atualizada com sucesso. Sua tarefa é: {tarefa.titulo}")
