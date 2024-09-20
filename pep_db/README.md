# Integração com PEP (via Banco de Dados)

Scripts SQL para ler dados a partir de Views em banco de dados PostgreSQL de PEP, e validar a consistência e integridade dos dados.

- `create_views.sql`: script de criação das views.

- `validate.sql`: script de validações.

- `prepare_database.sql`: script auxiliar para preparar o banco para teste.


## Como executar os scripts

Utilize a ferramenta `psql` para banco de dados PostgresSQL.

Crie um banco de dados para simular o PEP para executar os scripts do desafio:
```bash
psql -U usuario -c 'CREATE DATABASE pep_db;'
```

Crie algumas tabelas e insira dados fictícios para testar os scripts:
```bash
psql -U usuario -d pep_db -f /caminho/para/prepare_database.sql
```

Execute o script para a criação das views:

```bash
psql -U usuario -d pep_db -f /caminho/para/create_views.sql
```

Execute o script de validação:

```bash
psql -U usuario -d pep_db -f /caminho/para/validate.sql
```

Se houver inconsistências, as consultas retornarão os registros detectados.


## Organização dos Dados nas Views

Os dados estão organizados em três views:

- `vw_evolucoes`: Armazena informações relacionadas ao acompanhamento clínico do paciente (evoluções médicas), com informações sobre profissionais de saúde e detalhes clínicos.

- `vw_anamneses`: Armazena o histórico clínico, hábitos de vida, queixas e outros dados sobre a saúde do paciente coletados durante a consulta.

- `vw_receituarios`: Contém informações sobre prescrições médicas, incluindo medicamento, dosagem e duração do tratamento.


## Verificações de Integridade

No script, as consultas exemplificam cenários de validação que verificam:

*Chaves primárias não duplicadas*
- Não deve haver registros duplicados nas chaves primárias.

*Referências cruzadas para profissionais*
- Verificar se as referências entre as tabelas estão consistentes.

*Dado obrigatório*
- Checagem de campo obrigatório de datas de registro.

*Pacientes com Evoluções sem Profissionais de Saúde*
- Verifica se há registros de evoluções que não possuem profissionais de saúde associados, o que seria um problema de consistência.

*Anamneses sem Informações Críticas*
- Verifica se há anamneses sem informações importantes como histórico clínico ou queixas principais, o que pode comprometer a qualidade dos dados.

*Prescrições Duplicadas para o Mesmo Paciente no Mesmo Dia*
- Valida se há prescrições duplicadas para o mesmo paciente e medicamento, no mesmo dia, o que pode indicar problemas de duplicidade de dados.

*Evoluções Médicas com Datas Futuras*
- Valida se há evoluções médicas que possuem datas no futuro, o que pode indicar erro de entrada de dados.

*Pacientes Sem Evoluções ou Anamneses*
- Valida se há pacientes que não têm nenhuma evolução médica ou anamnese registrada, o que pode sinalizar dados incompletos.

*Medicamentos com Duração de Tratamento Inconsistente*
- Certifica-se de que a duração do tratamento nas prescrições não seja excessiva (como por exemplo, mais de um ano).
