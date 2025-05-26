[![MIT License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)
[![Docker Hub](https://img.shields.io/docker/pulls/bobwallan/empacotador-api?style=flat-square)](https://hub.docker.com/r/bobwallan/empacotador-api)
[![Java](https://img.shields.io/badge/built%20with-Java%2017-blue?style=flat-square)](https://openjdk.org/projects/jdk/17/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.0-brightgreen?style=flat-square)](https://spring.io/projects/spring-boot)

# 📦 Empacotador API – Otimizador de Pedidos em Caixas

API REST desenvolvida em **Java com Spring Boot**, que empacota pedidos de produtos em caixas disponíveis da forma mais otimizada possível. Containerizada com Docker e segura com autenticação via JWT.

---

## 📚 Documentação

A documentação completa está neste README. Futuramente, poderá ser migrada para uma wiki ou pasta `docs/`.

---

## 🚀 Como Executar Localmente com Docker

### ✅ Requisitos
- Docker instalado
- Porta `8080` livre

### ▶️ Passo a Passo

1. Build da imagem:
   docker build -t bobwallan/empacotador-api:1.0 .

2. Execute a aplicação:
   docker run -p 8080:8080 bobwallan/empacotador-api:1.0

3. Acesse a API:
   http://localhost:8080

---

## 🔐 Autenticação JWT

1. Faça login:
POST /auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "senha123"
}

2. No retorno, você receberá um token JWT.

3. Para acessar endpoints protegidos:
Authorization: Bearer <seu-token-aqui>

---

## 📦 Endpoint Principal

POST /api/pedidos

Recebe uma lista de produtos em um pedido e retorna a alocação otimizada nas caixas.

Exemplo de requisição:
[
  {
    "id": "pedido1",
    "produtos": [
      {"id": "produto1", "altura": 10, "largura": 20, "comprimento": 15},
      {"id": "produto2", "altura": 5, "largura": 10, "comprimento": 8}
    ]
  }
]

Exemplo de resposta:
[
  {
    "id": "pedido1",
    "caixas": [
      {
        "caixa": "Caixa 1",
        "produtos": ["produto1", "produto2"]
      }
    ]
  }
]

---

## 🔁 Atualização do Projeto

Sempre que fizer alterações no código:

1. Compile com Maven:
   mvn clean package

2. Gere uma nova imagem:
   docker build -t bobwallan/empacotador-api:<versao> .

3. Envie para o Docker Hub:
   docker push bobwallan/empacotador-api:<versao>

---

## 🙋 Contribuindo

Contribuições são muito bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar PRs.

---

## 💼 Histórico de Versões

As alterações são listadas na seção de releases do repositório.

---

## 📫 Contato

Desenvolvedor: Wallan Peixoto  
Email: bobwallan2@gmail.com  
WhatsApp: (27) 99256-7995
