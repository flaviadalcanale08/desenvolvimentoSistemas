import unittest
from fastapi.testclient import TestClient
from annaapi import app, db_tarefa  # importa sua API e o banco de tarefas

client = TestClient(app)

class TestAnnaAPI(unittest.TestCase):

    def setUp(self):
        db_tarefa.clear()  # garante que o banco está vazio antes de cada teste

    
    # TESTE 1 – Criar tarefa
    
    def test_criar_tarefa(self):
        nova_tarefa = {
            "id": "123",
            "titulo": "Estudar",
            "descricao": "Revisar conteúdo",
            "concluida": False
        }

        response = client.post("/Tarefas/", json=nova_tarefa)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["mensagem"], "Tarefa criada com sucesso")
        self.assertIn("123", db_tarefa)

    
    # TESTE 2 – Criar tarefa repetida
    
    def test_criar_tarefa_repetida(self):
        tarefa = {
            "id": "abc",
            "titulo": "Limpar",
            "descricao": "Limpar a casa",
            "concluida": False
        }

        client.post("/Tarefas/", json=tarefa)
        response = client.post("/Tarefas/", json=tarefa)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "ID já existente")

    
    # TESTE 3 – Listar todas as tarefas

    def test_listar_todas_as_tarefas(self):
        tarefa = {
            "id": "001",
            "titulo": "Dormir",
            "descricao": "Descansar bem",
            "concluida": False
        }

        client.post("/Tarefas/", json=tarefa)
        response = client.get("/Tarefas/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("001", response.json())

    # TESTE 4 – Buscar tarefa existente
   
    def test_buscar_tarefa_existente(self):
        tarefa = {
            "id": "x1",
            "titulo": "Academia",
            "descricao": "Treinar pernas",
            "concluida": False
        }

        client.post("/Tarefas/", json=tarefa)
        response = client.get("/Tarefas/x1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["titulo"], "Academia")

    
    # TESTE 5 – Buscar tarefa inexistente
    
    def test_buscar_tarefa_inexistente(self):
        response = client.get("/Tarefas/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Tarefa não encontrada.")

    
    # TESTE 6 – Atualizar tarefa existente
    
    def test_atualizar_tarefa(self):
        tarefa = {
            "id": "55",
            "titulo": "Ler",
            "descricao": "Ler um livro",
            "concluida": False
        }

        client.post("/Tarefas/", json=tarefa)

        tarefa_atualizada = {
            "id": "55",
            "titulo": "Ler Bíblia",
            "descricao": "Estudo espiritual",
            "concluida": True
        }

        response = client.put("/Tarefas/55", json=tarefa_atualizada)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["mensagem"], "Tarefa atualizada com sucesso")
        self.assertEqual(db_tarefa["55"]["titulo"], "Ler Bíblia")
        self.assertTrue(db_tarefa["55"]["concluida"])

    
    # TESTE 7 – Atualizar tarefa inexistente
    
    def test_atualizar_tarefa_inexistente(self):
        tarefa = {
            "id": "xyz",
            "titulo": "Aula",
            "descricao": "Ir para a aula",
            "concluida": False
        }

        response = client.put("/Tarefas/xyz", json=tarefa)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Tarefa não encontrada.")

    # TESTE 8 – Deletar tarefa existente
    def test_deletar_tarefa(self):
        tarefa = {
            "id": "del1",
            "titulo": "Passear",
            "descricao": "Ir ao parque",
            "concluida": False
        }

        client.post("/Tarefas/", json=tarefa)
        response = client.delete("/Tarefas/del1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["mensagem"], "Tarefa excluída com sucesso")
        self.assertNotIn("del1", db_tarefa)

    # TESTE 9 – Deletar tarefa inexistente
   
    def test_deletar_tarefa_inexistente(self):
        response = client.delete("/Tarefas/xxx")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Tarefa não encontrada.")


if __name__ == "__main__":
    unittest.main()
