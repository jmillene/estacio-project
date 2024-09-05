# Documentação do Projeto de E-commerce

## 1. Introdução
Este projeto foi desenvolvido para criar uma aplicação de e-commerce com funcionalidades básicas, como gestão de usuários, produtos, pedidos e itens de pedidos. A aplicação utiliza SQLAlchemy para gerenciar o banco de dados PostgreSQL, com uma estrutura que facilita a expansão e manutenção.

## 2. Objetivo
O objetivo deste projeto é criar um sistema de backend para um e-commerce, que possa gerir de forma eficaz as operações básicas, como criação e gerenciamento de usuários, produtos e pedidos. A solução visa fornecer uma base sólida para um sistema de e-commerce, permitindo operações CRUD essenciais e fácil integração com outras funcionalidades no futuro.

## 3. Estrutura do Projeto
O projeto está estruturado em quatro principais classes de modelo:

- **User**: Representa os usuários do sistema. Um usuário pode realizar pedidos.
- **Product**: Representa os produtos disponíveis no e-commerce. Contém informações como nome, descrição, preço e quantidade em estoque.
- **Order**: Representa um pedido feito por um usuário. Um pedido contém múltiplos itens.
- **OrderItem**: Representa os itens dentro de um pedido, associando produtos e suas quantidades a um pedido específico.

## 4. Criação do Banco de Dados
O banco de dados é criado utilizando o SQLAlchemy:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@localhost/mydatabase')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

```

## 5. CRUD do Usuário
Foi implementado um CRUD básico para a classe User, permitindo criar, ler, atualizar e deletar usuários. O CRUD inclui:

## Criação de usuário: Adiciona um novo usuário ao sistema.
## Leitura de usuários: Lista todos os usuários ou um usuário específico.
## Atualização de usuário: Permite a atualização das informações de um usuário.
## Deleção de usuário: Remove um usuário do sistema.

## 6. Uso do Docker

Para garantir a portabilidade e a consistência do ambiente de desenvolvimento, a aplicação foi containerizada utilizando Docker. Foram criados containers separados para a aplicação e para o banco de dados PostgreSQL, configurados para se comunicarem entre si. O Docker Compose foi utilizado para orquestrar a execução dos containers.

## Os principais arquivos relacionados são:

Dockerfile: Define a imagem Docker para a aplicação, incluindo a instalação das dependências necessárias.
docker-compose.yml: Configura e gerencia os serviços do Docker, incluindo a aplicação e o banco de dados.
Com o uso do Docker, foi possível garantir que o ambiente de desenvolvimento seja reproduzível em qualquer máquina, facilitando o processo de desenvolvimento e testes.

## 7. Testes com Thunder Client
Os testes das APIs foram realizados utilizando a extensão Thunder Client no Visual Studio Code. Esta ferramenta permitiu a simulação de requisições HTTP para verificar o funcionamento correto dos endpoints implementados, como os CRUDs para User e Order.

## Os testes incluíram:

Verificação da criação, leitura, atualização e deleção de usuários.
Testes de integração para pedidos, assegurando que os relacionamentos entre usuários, pedidos e itens de pedidos funcionem corretamente.


## 8. Como a Solução Resolve o Problema

Este projeto resolve o problema de gerenciamento de um sistema de e-commerce ao fornecer uma base sólida para as operações principais de um backend de e-commerce. A estrutura é escalável e pode ser expandida para incluir funcionalidades adicionais, como métodos de pagamento, relatórios de vendas e integração com front-end. Com a configuração atual, já é possível registrar usuários, gerenciar produtos e processar pedidos.

## 9. Conclusão

O sistema desenvolvido cumpre o propósito de gerir um e-commerce básico. Com a implementação do CRUD para todas as entidades, o projeto fornece uma estrutura que pode ser facilmente expandida para atender às necessidades de um e-commerce completo. O desenvolvimento contínuo do CRUD para produtos será um passo importante para a conclusão das funcionalidades essenciais do sistema.