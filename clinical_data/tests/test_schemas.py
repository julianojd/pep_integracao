from pydantic import ValidationError
from app.schemas import EvolucaoMedica, Anamnese, Receituario
from datetime import datetime


# Testes para EvolucaoMedica

def test_evolucao_medica_valid_data():
    evolucao = EvolucaoMedica(
        id_evolucao="12345",
        id_paciente="54321",
        data_evolucao=datetime.now(),
        id_profissional="98765",
        descricao_evolucao="Paciente apresentou melhora significativa.",
        sinais_vitais={"pressao_arterial": "120/80", "frequencia_cardiaca": 75},
        status_clinico="melhora"
    )
    assert evolucao.id_evolucao == 12345
    assert evolucao.sinais_vitais.pressao_arterial == "120/80"

def test_evolucao_medica_missing_required_field():
    try:
        EvolucaoMedica(
            id_paciente="54321",
            data_evolucao=datetime.now(),
            id_profissional="98765",
            descricao_evolucao="Paciente apresentou melhora significativa."
        )
    except ValidationError as e:
        assert "id_evolucao" in str(e)  # Valida que o campo id_evolucao está faltando

def test_evolucao_medica_invalid_field():
    try:
        EvolucaoMedica(
            id_evolucao="12345",
            id_paciente="54321",
            data_evolucao="invalid_date",  # Data inválida
            id_profissional="98765",
            descricao_evolucao="Paciente apresentou melhora significativa."
        )
    except ValidationError as e:
        assert "data_evolucao" in str(e)


# Testes para Anamnese

def test_anamnese_valid_data():
    anamnese = Anamnese(
        id_anamnese="123",
        id_paciente="543",
        data_anamnese=datetime.now(),
        id_profissional="456",
        historico_clinico="Histórico clínico detalhado.",
        queixas_principais="Dor de cabeça e febre.",
        habitos_vida="Não fuma, não bebe.",
        historico_familiar="Diabetes na família.",
        alergias="Nenhuma alergia conhecida."
    )
    assert anamnese.id_anamnese == 123
    assert anamnese.queixas_principais == "Dor de cabeça e febre."

def test_anamnese_missing_required_field():
    try:
        Anamnese(
            id_paciente="543",
            data_anamnese=datetime.now(),
            id_profissional="456",
            historico_clinico="Histórico clínico detalhado."
        )
    except ValidationError as e:
        assert "id_anamnese" in str(e)  # Valida que o campo id_anamnese está faltando

def test_anamnese_invalid_field():
    try:
        Anamnese(
            id_anamnese="A123",
            id_paciente="P543",
            data_anamnese="invalid_date",  # Data inválida
            id_profissional="PR456",
            historico_clinico="Histórico clínico detalhado.",
            queixas_principais="Dor de cabeça e febre."
        )
    except ValidationError as e:
        assert "data_anamnese" in str(e)


# Testes para Receituario

def test_receituario_valid_data():
    receituario = Receituario(
        id_receituario="123",
        id_paciente="543",
        data_prescricao=datetime.now(),
        id_profissional="456",
        medicamento="Paracetamol",
        dosagem="500mg",
        frequencia_administracao="8 em 8 horas",
        duracao_tratamento="7 dias",
        observacoes="Tomar após as refeições."
    )
    assert receituario.id_receituario == 123
    assert receituario.medicamento == "Paracetamol"

def test_receituario_missing_required_field():
    try:
        Receituario(
            id_paciente="543",
            data_prescricao=datetime.now(),
            id_profissional="456",
            medicamento="Paracetamol",
            dosagem="500mg",
            frequencia_administracao="8 em 8 horas"
        )
    except ValidationError as e:
        assert "id_receituario" in str(e)  # Valida que o campo id_receituario está faltando

def test_receituario_invalid_field():
    try:
        Receituario(
            id_receituario="123",
            id_paciente="543",
            data_prescricao="invalid_date",  # Data inválida
            id_profissional="456",
            medicamento="Paracetamol",
            dosagem="500mg",
            frequencia_administracao="8 em 8 horas",
            duracao_tratamento="7 dias"
        )
    except ValidationError as e:
        assert "data_prescricao" in str(e)
