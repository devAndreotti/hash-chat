# deixar apenas a mensagem em si no enviar_mensagem (não incluir o usuário)
# editar o enviar_mensagem para virar enviar_mensagem_tunel e criar um evniar msg no botao
# adicionar o pubsubsend all no enviar msg e editar o enviar_mensagem_tunel para renderizar a mensagem
        # import flet as ft

        # def main(page):
            
        #     chat = ft.Column()
        #     def enviar_mensagem_tunel(mensagem):
        #         chat.controls.append(ft.Text(mensagem))
        #         page.update()

        #     page.pubsub.subscribe(enviar_mensagem_tunel)

        #     def enviar_mensagem(e):
        #         page.pubsub.send_all(campo_mensagem.value)
        #         campo_mensagem.value = ""
        #         page.update()

        #     campo_mensagem = ft.TextField(label="Digite uma mensagem")
        #     botao_enviarmensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

        #     def entrar_chat(e):
        #         page.add(chat)
        #         page.add(ft.Row([campo_mensagem, botao_enviarmensagem]))
        #         popup.open = False
        #         page.remove(botao_iniciar)
        #         page.update()

        #     nome_usuario = ft.TextField(label="Escreva seu nome no chat")
        #     popup = ft.AlertDialog(
        #         open=False,
        #         modal=True,
        #         title=ft.Text("Bem vindo ao Hashzap"),
        #         content=nome_usuario,
        #         actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)])

        #     def abrir_popup(e):
        #         page.dialog = popup
        #         popup.open = True
        #         page.update()

        #     botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

        #     page.add(botao_iniciar)

        # ft.app(target=main, view=ft.WEB_BROWSER, port=8000)


import flet as ft

def main(page):
    # Cria a coluna que vai conter as mensagens do chat
    chat_content = ft.Column(
        scroll="auto",  # Permite a rolagem automática
        width=500,       # Largura do conteúdo do chat
        height=400       # Altura do conteúdo do chat
    )

    # Cria um contêiner para o chat, definindo largura, altura, cor de fundo e padding
    chat = ft.Container(
        content=chat_content,
        width=500,
        height=400,
        bgcolor=ft.colors.BLUE_GREY_900,  # Cor de fundo do chat
        padding=10                        # Padding interno para separar o texto das bordas
    )

    # Função para processar e adicionar mensagens ao chat
    def enviar_mensagem_tunel(infos):
        usuario = infos["usuario"]
        if infos["tipo"] == "entrada":
            # Mensagem de entrada (usuário entrou no chat)
            chat_content.controls.append(ft.Text(
                f"{usuario} entrou no chat",
                size=12,
                color=ft.colors.AMBER_400,
                italic=True
            ))
        else:
            # Mensagem normal (usuário enviou uma mensagem)
            mensagem = infos["mensagem"]
            chat_content.controls.append(ft.Text(
                f"{usuario}: {mensagem}",
                size=14,
                color=ft.colors.WHITE
            ))
        page.update()  # Atualiza a página para mostrar a nova mensagem
        chat_content.scroll_to_bottom()  # Rola para a parte inferior automaticamente
        page.update()  # Força uma atualização adicional da página

    # Inscreve a função para receber atualizações de mensagens
    page.pubsub.subscribe(enviar_mensagem_tunel)

    # Função para enviar uma mensagem quando o botão é clicado ou o campo de texto é submetido
    def enviar_mensagem(e):
        if campo_mensagem.value:
            # Envia a mensagem para todos os usuários
            page.pubsub.send_all({
                "usuario": nome_usuario.value,
                "mensagem": campo_mensagem.value,
                "tipo": "mensagem"
            })
            campo_mensagem.value = ""  # Limpa o campo de mensagem
            page.update()  # Atualiza a página

    # Campo de texto para digitar a mensagem
    campo_mensagem = ft.TextField(
        label="Digite uma mensagem",
        on_submit=enviar_mensagem,  # Envia a mensagem ao pressionar Enter
        width=300,                  # Largura do campo de texto
        text_size=14,
        bgcolor=ft.colors.BLUE_GREY_900,
        color=ft.colors.WHITE
    )
    
    # Botão para enviar a mensagem
    botao_enviarmensagem = ft.ElevatedButton(
        "Enviar", 
        on_click=enviar_mensagem,  # Envia a mensagem ao clicar
        width=90  # Largura do botão
    )

    # Função para lidar com a entrada no chat
    def entrar_chat(e):
        page.add(cabecalho)  # Adiciona o cabeçalho à página
        page.add(chat)      # Adiciona o contêiner do chat à página
        page.add(ft.Row([
            campo_mensagem,
            botao_enviarmensagem
        ], alignment=ft.MainAxisAlignment.START, spacing=10))  # Adiciona o campo de mensagem e o botão
        popup.open = False  # Fecha o popup
        page.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})  # Notifica todos que o usuário entrou
        page.remove(botao_iniciar)  # Remove o botão de iniciar chat
        page.update()  # Atualiza a página

    # Campo de texto para o nome do usuário
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    
    # Popup para o usuário inserir o nome antes de entrar no chat
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem-vindo ao Chat!"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)]  # Botão para entrar no chat
    )

    # Função para abrir o popup de entrada
    def abrir_popup(e):
        page.dialog = popup  # Define o popup como o diálogo da página
        popup.open = True  # Abre o popup
        page.update()  # Atualiza a página

    # Botão para iniciar o chat e abrir o popup
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # Cabeçalho do chat
    cabecalho = ft.Container(
        ft.Text("Real Time - Chat", size=20, color=ft.colors.WHITE),
        padding=10,  # Padding interno para o cabeçalho
        bgcolor=ft.colors.BLUE_GREY_800,  # Cor de fundo do cabeçalho
    )

    # Adiciona o botão de iniciar chat à página
    page.add(botao_iniciar)

# Executa a aplicação web
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)