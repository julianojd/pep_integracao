# Integração com Serviço de PEP (API RESTful)

Microserviço desenvolvido em Python que permite requisições POST para API de barramento de integração, contendo informações clínicas (evoluções médicas, anamneses, receituários).

## Índice
1. [Processo de Integração](#processo-de-integração)
2. [Como executar o microserviço localmente](#como-executar-o-microserviço-localmente)
3. [Como testar os endpoints](#como-testar-os-endpoints)
4. [Como executar os testes unitários](#como-executar-os-testes-unitários)
5. [Documentação da API](#documentação-api)
6. [Descrição dos Endpoints](#descrição-dos-endpoints)
   - [POST /evolucoes](#post-evolucoes)
   - [POST /anamneses](#post-anamneses)
   - [POST /receituarios](#post-receituarios)

---

### Processo de Integração

1. **Validação de Dados**: Cada requisição é validada usando Pydantic. Campos obrigatórios são verificados, e tipos incorretos ou faltantes resultam em erro.
2. **Publicação na Fila**: Após validação, os dados são serializados em JSON e publicados na fila RabbitMQ correspondente.
3. **Filas no RabbitMQ**: Cada tipo de dado (evolução médica, anamnese, receituário) é enviado para uma fila específica no RabbitMQ, configurada com persistência de mensagens para garantir durabilidade.

#### Observações

- Caso a validação de dados falhe, uma exceção é levantada, e o microserviço retorna um erro apropriado.
- As mensagens publicadas no RabbitMQ utilizam `delivery_mode=2`, o que garante que as mensagens sejam persistentes e sobrevivam a reinicializações do servidor RabbitMQ.

---

### Como Executar o Microserviço Localmente

#### Pré-requisitos
- `Docker` e `Docker Compose` instalados no sistema.
- `RabbitMQ` rodando localmente ou acessível através da rede.

#### Passos

1. Clone o repositório para máquina local:
   ```bash
   git clone git@github.com:julianojd/pep_integracao.git
   ```

2. Entre no diretório `clinical_data`:
   ```bash
   cd pep_integracao/clinical_data
   ```

3. Construa e execute o microserviço com Docker Compose:
   ```bash
   docker compose up --build
   ```

3. O serviço estará rodando em `http://localhost:8000`.

#### Configurações
O arquivo `docker-compose.yml` define o ambiente do microserviço, incluindo a comunicação com o RabbitMQ.

---

### Como Testar os Endpoints

Os endpoints podem ser testados com ferramentas como **Postman** ou **cURL**.

Exemplos de uso de cURL para cada endpoint estão descritos abaixo, na seção de [Descrição dos Endpoints](#descrição-dos-endpoints).

Além disso, os endpoints também podem ser testados através da documentação interativa da API, acessando `http://localhost:8000/docs`

---

### Como Executar os Testes Unitários

Os testes unitários cobrem validações de schemas, simulação de publicação de mensagens no RabbitMQ, e comportamentos esperados dos endpoints.

O arquivo `docker-compose-tests.yml` pode ser usado para rodar os testes unitários dentro do container Docker.

Execute:
   ```bash
   docker compose -f docker-compose-tests.yml run --rm tests
   ```

---

### Documentação API

Documentações automáticas da API:

- Documentação interativa: http://localhost:8000/docs

- Documentação alternativa: http://localhost:8000/redoc

- OpenAPI schema:  http://localhost:8000/openapi.json

---

### Descrição dos Endpoints

#### POST /evolucoes

**Descrição**: Recebe informações de uma evolução médica, valida os dados e os publica em uma fila RabbitMQ.

- **URL**: `/evolucoes`
- **Método HTTP**: `POST`
- **Corpo da Requisição**:
  ```json
  {
    "id_evolucao": "12345",
    "id_paciente": "54321",
    "data_evolucao": "2024-09-18T12:00:00",
    "id_profissional": "98765",
    "descricao_evolucao": "Paciente apresentou melhora significativa.",
    "sinais_vitais": {
      "pressao_arterial": "120/80",
      "frequencia_cardiaca": 75
    },
    "status_clinico": "melhora"
  }
  ```

- **Exemplo cURL**:
  ```bash
  curl -X POST http://localhost:8000/evolucoes -H "Content-Type: application/json" -d @evolucao.json
  ```

- **Resposta de Sucesso**:
  ```json
  {
    "message": "Evolução médica enviada com sucesso."
  }
  ```

---

#### POST /anamneses

**Descrição**: Recebe informações de uma anamnese, valida os dados e os publica em uma fila RabbitMQ.

- **URL**: `/anamneses`
- **Método HTTP**: `POST`
- **Corpo da Requisição**:
  ```json
  {
    "id_anamnese": "123",
    "id_paciente": "54321",
    "data_anamnese": "2024-09-18T12:00:00",
    "id_profissional": "98765",
    "historico_clinico": "Histórico de doenças pregressas...",
    "queixas_principais": "Dor de cabeça e febre."
  }
  ```

- **Exemplo cURL**:
  ```bash
  curl -X POST http://localhost:8000/anamneses -H "Content-Type: application/json" -d @anamnese.json
  ```

- **Resposta de Sucesso**:
  ```json
  {
    "message": "Anamnese enviada com sucesso."
  }
  ```

---

#### POST /receituarios

**Descrição**: Recebe informações de um receituário médico, valida os dados e os publica em uma fila RabbitMQ.

- **URL**: `/receituarios`
- **Método HTTP**: `POST`
- **Corpo da Requisição**:
  ```json
  {
    "id_receituario": "123",
    "id_paciente": "54321",
    "data_prescricao": "2024-09-18T12:00:00",
    "id_profissional": "98765",
    "medicamento": "Paracetamol",
    "dosagem": "500mg",
    "frequencia_administracao": "8 horas",
    "duracao_tratamento": "7 dias"
  }
  ```

- **Exemplo cURL**:
  ```bash
  curl -X POST http://localhost:8000/receituarios -H "Content-Type: application/json" -d @receituario.json
  ```

- **Resposta de Sucesso**:
  ```json
  {
    "message": "Receituário enviado com sucesso."
  }
  ```

---