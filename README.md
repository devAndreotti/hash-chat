# Chat em Tempo Real

<div align="center">
  <img src="https://example.com/chat-image.jpg" alt="Imagem do Chat" width="800" height="500"/>
</div>

## Objetivo do Projeto

Este projeto é um **chat em tempo real** que permite que os usuários entrem em um chat, enviem mensagens e vejam atualizações em tempo real.

- **Desenvolver um chat interativo** com Flet, onde os usuários podem se comunicar instantaneamente.
- **Utilizar Pub/Sub** para gerenciar a comunicação entre os usuários.
- **Renderizar mensagens em tempo real** no chat.

## Tecnologias Empregadas

- **Flet**: Biblioteca utilizada para a criação da interface do chat e gerenciamento do estado da aplicação.
- **JavaScript**: Linguagem de programação usada para lógica do chat.

## Guia de Implementação

1. **Certifique-se que Flet Está Instalado**
   - Execute `pip install flet` para instalar a biblioteca Flet, se necessário.

2. **Inicialize o Projeto**
   - No terminal, execute `python nome_do_arquivo.py` para iniciar o projeto.

3. **Inscreva-se para Receber Mensagens**
   - A função `enviar_mensagem_tunel` processa e adiciona mensagens ao chat quando publicadas.

4. **Envie Mensagens**
   - A função `enviar_mensagem` envia uma mensagem para todos os usuários quando o botão é clicado ou o campo de texto é submetido.

## Funcionalidades

- **Campo de Mensagem**: Permite que os usuários digitem e enviem mensagens.
- **Botão de Enviar**: Envia a mensagem digitada para o chat.
- **Popup de Entrada**: Solicita o nome do usuário antes de entrar no chat.

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma nova branch para sua feature `git checkout -b feature/nome-feature`.
3. Commit suas mudanças `git commit -m 'Adiciona nova feature'`.
4. Envie para a branch `git push origin feature/nome-feature`.
5. Abra um Pull Request.

## Nota

Este projeto é para fins educacionais. Sinta-se livre para explorar e adaptar.
