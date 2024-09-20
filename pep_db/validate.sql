-- Script com queries de validações

-- Verifica duplicação de chaves primárias
SELECT id_evolucao, COUNT(*)
FROM vw_evolucoes
GROUP BY id_evolucao
HAVING COUNT(*) > 1;

SELECT id_anamnese, COUNT(*)
FROM vw_anamneses
GROUP BY id_anamnese
HAVING COUNT(*) > 1;

SELECT id_receituario, COUNT(*)
FROM vw_receituarios
GROUP BY id_receituario
HAVING COUNT(*) > 1;

-- Verifica se há referências inválidas de profissionais
SELECT id_profissional
FROM vw_evolucoes
WHERE id_profissional NOT IN (SELECT id_profissional FROM profissionais);

SELECT id_profissional
FROM vw_anamneses
WHERE id_profissional NOT IN (SELECT id_profissional FROM profissionais);

SELECT id_profissional
FROM vw_receituarios
WHERE id_profissional NOT IN (SELECT id_profissional FROM profissionais);

-- Verifica se há registros sem campo obrigatório, exemplo: data
SELECT * 
FROM evolucoes
WHERE data_evolucao IS NULL;

SELECT * 
FROM anamneses
WHERE data_anamnese IS NULL;

SELECT * 
FROM receituarios
WHERE data_prescricao IS NULL;


-- Pacientes com Evoluções sem Profissionais de Saúde
SELECT *
FROM vw_evolucoes
WHERE nome_profissional IS NULL;

-- Anamneses sem Informações Críticas
SELECT *
FROM vw_anamneses
WHERE historico_clinico IS NULL OR queixas_principais IS NULL;

-- Prescrições Duplicadas para o Mesmo Paciente no Mesmo Dia
SELECT id_paciente, medicamento, data_prescricao, COUNT(*)
FROM vw_receituarios
GROUP BY id_paciente, medicamento, data_prescricao
HAVING COUNT(*) > 1;

-- Evoluções Médicas com Datas Futuras
SELECT *
FROM vw_evolucoes
WHERE data_evolucao > NOW();

-- Pacientes Sem Evoluções ou Anamneses
SELECT p.id_paciente, p.nome
FROM pacientes p
LEFT JOIN vw_evolucoes e ON p.id_paciente = e.id_paciente
LEFT JOIN vw_anamneses a ON p.id_paciente = a.id_paciente
WHERE e.id_paciente IS NULL AND a.id_paciente IS NULL;

-- Medicamentos com Duração de Tratamento Inconsistente
SELECT id_receituario, medicamento, duracao_tratamento
FROM vw_receituarios
WHERE duracao_tratamento > 365;
