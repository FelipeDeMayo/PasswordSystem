# Gerador e Validador de Senhas

Este projeto é um programa simples em Python para gerar senhas aleatórias e validar senhas personalizadas. Ele oferece as seguintes funcionalidades:

- **Gerar uma senha aleatória**: Cria uma senha que inclui letras maiúsculas, minúsculas, números e caracteres especiais, com um comprimento variável entre 8 e 16 caracteres.
- **Validar uma senha personalizada**: Permite que o usuário insira sua própria senha, e o programa valida se ela atende aos requisitos de segurança (mínimo de 8 e máximo de 16 caracteres, com pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial).
- **Limpar a tela**: Limpa o terminal para melhorar a experiência visual do usuário.
- **Menu interativo**: O programa oferece um menu para escolher entre as opções disponíveis.

## Funcionalidades

1. **Gerar senha aleatória**: O programa gera uma senha forte e segura utilizando as bibliotecas `secrets` e `string` para garantir a aleatoriedade e a segurança.
2. **Validar senha personalizada**: O usuário pode criar sua própria senha, e o programa verifica se ela atende aos seguintes critérios:
   - Ter entre 8 e 16 caracteres.
   - Incluir pelo menos uma letra maiúscula.
   - Incluir pelo menos uma letra minúscula.
   - Incluir pelo menos um número.
   - Incluir pelo menos um caractere especial.
3. **Limpar a tela**: Função de limpar a tela, que varia de acordo com o sistema operacional.
4. **Sair do programa**: O usuário pode optar por sair do programa a qualquer momento.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação usada para desenvolver o programa.
- **Biblioteca `os`**: Usada para limpar a tela do terminal, com suporte para Windows e Unix-based.
- **Biblioteca `secrets`**: Usada para gerar senhas seguras e aleatórias, garantindo criptografia forte.
- **Biblioteca `string`**: Fornece acesso a conjuntos de caracteres, como letras e números, usados na criação de senhas.
- **Biblioteca `random`**: Usada para embaralhar as senhas geradas, garantindo que elas sejam imprevisíveis.