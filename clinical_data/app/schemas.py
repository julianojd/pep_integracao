"""Esquemas para validação dos dados"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SinaisVitais(BaseModel):
    pressao_arterial: Optional[str] = Field(None, examples=["120/80"])
    frequencia_cardiaca: Optional[int] = Field(None, examples=[75])
    temperatura: Optional[float] = Field(None, examples=[36.5])

class EvolucaoMedica(BaseModel):
    id_evolucao: int = Field(
        ...,
        description="Identificador único da evolução médica"
    )
    id_paciente: int = Field(
        ...,
        description="Identificador único do paciente"
    )
    data_evolucao: datetime = Field(
        ...,
        description="Data e hora em que a evolução foi registrada"
    )
    id_profissional: int = Field(
        ...,
        description="Identificador do profissional que registrou a evolução"
    )
    descricao_evolucao: str = Field(
        ...,
        description="Texto com detalhes sobre a evolução médica"
    )
    sinais_vitais: Optional[SinaisVitais] =  Field(
        None,
        description="Dados de pressão arterial, frequência cardíaca, temperatura"
    )
    status_clinico: Optional[str] = Field(
        None,
        description="Indicação do estado clínico do paciente",
        examples=["melhora", "piora", "estável"]
    )
    observacoes_adicionais: Optional[str] = Field(
        None,
        description="Outras informações que possam ser relevantes ao caso"
    )

class Anamnese(BaseModel):
    id_anamnese: int = Field(
        ..., description="Identificador único da anamnese"
    )
    id_paciente: int = Field(
        ..., description="Identificador único do paciente"
    )
    data_anamnese: datetime = Field(
        ..., description="Data e hora em que a anamnese foi registrada"
    )
    id_profissional: int = Field(
        ..., description="Identificador do profissional que realizou a anamnese"
    )
    historico_clinico: str = Field(
        ..., description="Texto com o histórico médico do paciente, incluindo doenças pregressas, cirurgias, alergias, etc"
    )
    queixas_principais: str = Field(
        ..., description="Motivo da consulta e principais sintomas relatados"
    )
    habitos_vida: Optional[str] = Field(
        None, description="Informações sobre alimentação, exercício, tabagismo, consumo de álcool, etc"
    )
    historico_familiar: Optional[str] = Field(
        None, description="Registro de doenças familiares relevantes, como doenças hereditárias"
    )
    alergias: Optional[str] = Field(
        None, description="Detalhes sobre alergias conhecidas do paciente"
    )

class Receituario(BaseModel):
    id_receituario: int = Field(
        ..., description="Identificador único do receituário"
    )
    id_paciente: int = Field(
        ..., description="Identificador único do paciente"
    )
    data_prescricao: datetime = Field(
        ..., description="Data e hora em que o receituário foi emitido"
    )
    id_profissional: int = Field(
        ..., description="Identificador do médico que prescreveu a receita"
    )
    medicamento: str = Field(
        ..., description="Nome do medicamento prescrito"
    )
    dosagem: str = Field(
        ..., description="Quantidade do medicamento a ser administrada"
    )
    frequencia_administracao: str = Field(
        ..., description="Intervalo de tempo entre as doses"
    )
    duracao_tratamento: str = Field(
        ..., description="Período de tempo em que o paciente deve tomar o medicamento"
    )
    observacoes: Optional[str] = Field(
        None,
        description="Instruções adicionais"
    )
