-- Script de criação de Views

-- View de evoluções médicas
CREATE VIEW vw_evolucoes AS
SELECT 
    e.id_evolucao,
    e.id_paciente,
    e.data_evolucao,
    e.id_profissional,
    e.descricao_evolucao,
    e.sinais_vitais,
    e.status_clinico,
    e.observacoes,
    p.nome AS nome_paciente,
    pr.nome AS nome_profissional
FROM 
    evolucoes e
JOIN 
    pacientes p ON e.id_paciente = p.id_paciente
JOIN 
    profissionais pr ON e.id_profissional = pr.id_profissional;

-- View de anamneses
CREATE VIEW vw_anamneses AS
SELECT 
    a.id_anamnese,
    a.id_paciente,
    a.data_anamnese,
    a.id_profissional,
    a.historico_clinico,
    a.queixas_principais,
    a.habitos_vida,
    a.historico_familiar,
    a.alergias,
    p.nome AS nome_paciente,
    pr.nome AS nome_profissional
FROM 
    anamneses a
JOIN 
    pacientes p ON a.id_paciente = p.id_paciente
JOIN 
    profissionais pr ON a.id_profissional = pr.id_profissional;

-- View de receituarios
CREATE VIEW vw_receituarios AS
SELECT 
    r.id_receituario,
    r.id_paciente,
    r.data_prescricao,
    r.id_profissional,
    r.medicamento,
    r.dosagem,
    r.frequencia_administracao,
    r.duracao_tratamento,
    r.observacoes,
    p.nome AS nome_paciente,
    pr.nome AS nome_profissional
FROM 
    receituarios r
JOIN 
    pacientes p ON r.id_paciente = p.id_paciente
JOIN 
    profissionais pr ON r.id_profissional = pr.id_profissional;
