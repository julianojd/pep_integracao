-- Script para criação de tabelas e inserção de dados fictícios


-- TABELAS

-- Criação da tabela de Pacientes
CREATE TABLE pacientes (
    id_paciente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);

-- Criação da tabela de Profissionais de Saúde
CREATE TABLE profissionais (
    id_profissional SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(50) NOT NULL
);

-- Criação da tabela de Evoluções Médicas
CREATE TABLE evolucoes (
    id_evolucao SERIAL PRIMARY KEY,
    id_paciente INT REFERENCES pacientes(id_paciente),
    data_evolucao TIMESTAMP NOT NULL,
    id_profissional INT REFERENCES profissionais(id_profissional),
    descricao_evolucao TEXT NOT NULL,
    sinais_vitais TEXT,
    status_clinico VARCHAR(50),
    observacoes TEXT
);

-- Criação da tabela de Anamneses
CREATE TABLE anamneses (
    id_anamnese SERIAL PRIMARY KEY,
    id_paciente INT REFERENCES pacientes(id_paciente),
    data_anamnese TIMESTAMP NOT NULL,
    id_profissional INT REFERENCES profissionais(id_profissional),
    historico_clinico TEXT NOT NULL,
    queixas_principais TEXT NOT NULL,
    habitos_vida TEXT,
    historico_familiar TEXT,
    alergias TEXT
);

-- Criação da tabela de Receituários
CREATE TABLE receituarios (
    id_receituario SERIAL PRIMARY KEY,
    id_paciente INT REFERENCES pacientes(id_paciente),
    data_prescricao TIMESTAMP NOT NULL,
    id_profissional INT REFERENCES profissionais(id_profissional),
    medicamento VARCHAR(100) NOT NULL,
    dosagem VARCHAR(50) NOT NULL,
    frequencia_administracao VARCHAR(50) NOT NULL,
    duracao_tratamento INT NOT NULL,
    observacoes TEXT
);


-- INSERIR DADOS

-- Inserindo pacientes fictícios
INSERT INTO pacientes (nome, data_nascimento) VALUES
('Maria Silva', '1985-06-15'),
('João Pereira', '1978-03-22'),
('Ana Souza', '1990-12-05');

-- Inserindo profissionais fictícios
INSERT INTO profissionais (nome, especialidade) VALUES
('Dr. Carlos Andrade', 'Cardiologia'),
('Dra. Paula Lima', 'Pediatria'),
('Dr. Rafael Gomes', 'Clínica Geral');

-- Inserindo evoluções médicas fictícias
INSERT INTO evolucoes (id_paciente, data_evolucao, id_profissional, descricao_evolucao, sinais_vitais, status_clinico, observacoes) VALUES
(1, '2024-09-01 10:00:00', 1, 'Paciente apresentou melhora significativa.', '120/80, 70 bpm', 'Melhora', 'Paciente estável'),
(2, '2024-09-02 14:30:00', 2, 'Paciente ainda com febre.', '100/60, 80 bpm, 38°C', 'Estável', 'Recomendado repouso'),
(3, '2024-09-03 09:00:00', 3, 'Paciente com dores de cabeça.', '130/90, 75 bpm', 'Piora', 'Prescrito analgésico');

-- Inserindo anamneses fictícias
INSERT INTO anamneses (id_paciente, data_anamnese, id_profissional, historico_clinico, queixas_principais, habitos_vida, historico_familiar, alergias) VALUES
(1, '2024-08-30 08:00:00', 1, 'Histórico de hipertensão.', 'Dor no peito', 'Sedentária, fumante', 'Pai com hipertensão', 'Nenhuma'),
(2, '2024-08-28 11:15:00', 2, 'Histórico de asma.', 'Falta de ar', 'Pratica exercícios regularmente', 'Mãe asmática', 'Nenhuma'),
(3, '2024-08-29 16:20:00', 3, 'Histórico de enxaqueca.', 'Dor de cabeça', 'Bebe álcool ocasionalmente', 'Nenhum histórico relevante', 'Alergia a penicilina');

-- Inserindo receituários fictícios
INSERT INTO receituarios (id_paciente, data_prescricao, id_profissional, medicamento, dosagem, frequencia_administracao, duracao_tratamento, observacoes) VALUES
(1, '2024-09-01 10:10:00', 1, 'Atenolol', '50mg', '2x ao dia', '30', 'Reavaliar após o tratamento'),
(2, '2024-09-02 14:40:00', 2, 'Paracetamol', '500mg', '4x ao dia', '5', 'Tomar após as refeições'),
(3, '2024-09-03 09:15:00', 3, 'Ibuprofeno', '600mg', '3x ao dia', '7', 'Se os sintomas persistirem, retornar ao consultório');
