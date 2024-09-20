from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

# Mocks para a publicação na fila RabbitMQ
def mock_publish_message(queue_name, message):
    assert queue_name in ["evolucoes_queue", "anamneses_queue", "receituarios_queue"]
    assert isinstance(message, dict)

# Testes para o endpoint de Evolução Médica
@patch("app.main.publish_message", side_effect=mock_publish_message)
def test_create_evolucao(mock_publish):
    response = client.post("/evolucao/", json={
        "id_evolucao": "12345",
        "id_paciente": "54321",
        "data_evolucao": "2024-09-17T10:00:00",
        "id_profissional": "98765",
        "descricao_evolucao": "Paciente apresentou melhora significativa.",
        "sinais_vitais": {"pressao_arterial": "120/80", "frequencia_cardiaca": 75},
        "status_clinico": "melhora"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Evolução médica enviada com sucesso."}
    mock_publish.assert_called_once()

@patch("app.main.publish_message", side_effect=mock_publish_message)
def test_create_evolucao_missing_required_fields(mock_publish):
    response = client.post("/evolucao/", json={
        "id_paciente": "54321",  # Faltando o campo obrigatório 'id_evolucao'
        "data_evolucao": "2024-09-17T10:00:00",
        "id_profissional": "98765",
        "descricao_evolucao": "Paciente apresentou melhora significativa."
    })
    assert response.status_code == 422  # Unprocessable Entity (erro de validação)
    mock_publish.assert_not_called()

# Testes para o endpoint de Anamnese
@patch("app.main.publish_message", side_effect=mock_publish_message)
def test_create_anamnese(mock_publish):
    response = client.post("/anamnese/", json={
        "id_anamnese": "123",
        "id_paciente": "543",
        "data_anamnese": "2024-09-17T10:00:00",
        "id_profissional": "456",
        "historico_clinico": "Histórico clínico detalhado.",
        "queixas_principais": "Dor de cabeça e febre.",
        "habitos_vida": "Não fuma, não bebe.",
        "historico_familiar": "Diabetes na família.",
        "alergias": "Nenhuma alergia conhecida."
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Anamnese enviada com sucesso."}
    mock_publish.assert_called_once()

@patch("app.main.publish_message", side_effect=mock_publish_message)
def test_create_anamnese_missing_required_fields(mock_publish):
    response = client.post("/anamnese/", json={
        "id_paciente": "543",  # Faltando o campo obrigatório 'id_anamnese'
        "data_anamnese": "2024-09-17T10:00:00",
        "id_profissional": "456",
        "historico_clinico": "Histórico clínico detalhado.",
        "queixas_principais": "Dor de cabeça e febre."
    })
    assert response.status_code == 422  # Unprocessable Entity (erro de validação)
    mock_publish.assert_not_called()

# Testes para o endpoint de Receituário
@patch("app.main.publish_message", side_effect=mock_publish_message)
def test_create_receituario(mock_publish):
    response = client.post("/receituario/", json={
        "id_receituario": "123",
        "id_paciente": "543",
        "data_prescricao": "2024-09-17T10:00:00",
        "id_profissional": "456",
        "medicamento": "Paracetamol",
        "dosagem": "500mg",
        "frequencia_administracao": "8 em 8 horas",
        "duracao_tratamento": "7 dias",
        "observacoes": "Tomar após as refeições."
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Receituário enviado com sucesso."}
    mock_publish.assert_called_once()

@patch("app.main.publish_message", side_effect=mock_publish_message)
def test_create_receituario_missing_required_fields(mock_publish):
    response = client.post("/receituario/", json={
        "id_paciente": "543",  # Faltando o campo obrigatório 'id_receituario'
        "data_prescricao": "2024-09-17T10:00:00",
        "id_profissional": "456",
        "medicamento": "Paracetamol",
        "dosagem": "500mg",
        "frequencia_administracao": "8 em 8 horas",
        "duracao_tratamento": "7 dias"
    })
    assert response.status_code == 422  # Unprocessable Entity (erro de validação)
    mock_publish.assert_not_called()
