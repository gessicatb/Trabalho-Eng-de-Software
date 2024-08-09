# Distribuidora de Jogos
Sistema para cadastro e distribuição de jogos. Os usuários da nossa plataforma são desenvolvedores de jogos e estúdios de desenvolvimento, são aqueles que detêm os direitos de um ou mais jogos.

## Descrição

Nosso sistema é projetado para facilitar o cadastro, gerenciamento e distribuição de jogos desenvolvidos por estúdios e desenvolvedores independentes. Ele oferece uma interface intuitiva e funcionalidades abrangentes para garantir que os jogos sejam cadastrados corretamente e estejam prontos para distribuição nas plataformas de venda e distribuição.

1. **Tela de Cadastro e Login de Usuários**
    - Os usuários são os desenvolvedores e estúdios de desenvolvimento. É de responsabilidade deles cadastrar os jogos e também as pessoas que participam no desenvolvimento desses jogos.
    - Para cadastro do usuário guardamos o seguinte:
        - Nome
        - Email
        - Senha
        - CNPJ/CPF
        - Dados Bancários

2. **Tela de Cadastro de Pessoas**
    - Todo usuário do sistema pode cadastrar uma pessoa se ela ainda não estiver no banco. As pessoas assumem papel no desenvolvimento dos jogos. Guardamos as seguintes informações:
        - Nome
        - Email
        - CPF
        - Rede Social
        - Telefone

3. **Cadastro de Jogos**
    - Código de barras (ou SKU) deve ser único por jogo.
    - Um jogo pode ser um título único ou parte de uma série/franquia. Cada jogo deve conter as seguintes informações:
        - Título do Jogo
        - Plataforma (PC, console, mobile)
        - Gênero
        - Data de Lançamento
        - ISRC (International Standard Recording Code) único
        - Informações sobre desenvolvedores, designers, artistas, etc.

4. **Visualização dos Ganhos Recebidos por Jogo**
    - Relatórios detalhados sobre os ganhos recebidos por cada jogo ou franquia, incluindo estatísticas de vendas e receitas.

5. **Capacidade de Deletar**
    - Possibilidade de deletar registros de jogos e pessoas cadastradas, com as devidas verificações de segurança para evitar exclusões acidentais.

## Backlog do Produto

1. **Cadastro de Usuário**
    - Tela de cadastro de novos usuários
    - Tela de login de usuários existentes

2. **Cadastro de Pessoas**
    - Tela para adicionar novas pessoas ao sistema
    - Tela para visualizar e editar informações de pessoas cadastradas

3. **Cadastro de Jogos**
    - Tela para adicionar novos jogos ao sistema
    - Tela para editar informações de jogos existentes

4. **Visualização de Ganhos**
    - Tela para visualizar os ganhos por jogo
    - Tela para visualizar relatórios detalhados de vendas e receitas

5. **Deletar Registros**
    - Funcionalidade para deletar jogos cadastrados
    - Funcionalidade para deletar pessoas cadastradas

6. **Notificações**
    - Sistema de notificações para informar sobre novas vendas e ganhos
    - Notificações sobre atualizações importantes no sistema

7. **Pesquisa Avançada**
    - Funcionalidade de busca avançada para jogos e pessoas
    - Filtros para refinar os resultados de busca

8. **Integração com Plataformas de Vendas**
    - Integração com plataformas de venda de jogos (Steam, PlayStation Store, etc.)
    - Sincronização automática de vendas e ganhos

9. **Segurança**
    - Implementação de autenticação e autorização robustas
    - Criptografia de dados sensíveis

10. **Suporte ao Cliente**
    - Sistema de suporte integrado para ajudar os usuários
    - Base de conhecimento e FAQs

## Backlog do Sprint

1. **CRUD de Usuários**
    - Implementação das funcionalidades de Create, Read, Update e Delete para usuários

2. **CRUD de Pessoas**
    - Implementação das funcionalidades de Create, Read, Update e Delete para pessoas

3. **CRUD de Jogos**
    - Implementação das funcionalidades de Create, Read, Update e Delete para jogos

4. **Visualização de Ganhos**
    - Desenvolvimento da tela de visualização dos ganhos por jogo

5. **Notificações**
    - Implementação do sistema de notificações para novas vendas e ganhos


## Membros da Equipe e Papel

-**Gessica Teixeira Bomfim** - *Full-Stack Developer* - [GitHub Gessica](https://github.com/linkParaPerfil)

-**Alexssander Fernandes Candido**

-**Gabriel Abreu Miller Godoi**

-**Gabriel Henrique Silva**
