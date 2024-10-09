
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    senha VARCHAR(200) NOT NULL,
    cnpj VARCHAR(20) UNIQUE NOT NULL,
    dados_bancarios VARCHAR(200)
);

CREATE TABLE jogos (
    id SERIAL PRIMARY KEY,
    nome_jogo VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    descricao TEXT
);


CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    rede_social VARCHAR(100),
    telefone VARCHAR(15)
);
