from configs import *

#Gera o menuzinho maroto
#####################################################################
def gerar_botoes(categoria_menu):

    if categoria_menu == "automacoes_lampada":
        markup = InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(
            InlineKeyboardButton("Hora do Trabalho", callback_data="horaDoTrabalho"),
            InlineKeyboardButton("Hora do Café", callback_data="horaDoCafe"),
            InlineKeyboardButton("Hora do Jogo", callback_data="horaDoJonas"),
            InlineKeyboardButton("Hora do Dino", callback_data="horaDoDino"),
            InlineKeyboardButton("Boa Noite", callback_data="boaNoite"),
            InlineKeyboardButton("Arthur Dormir", callback_data="oArthurVaiDormir"),
            InlineKeyboardButton("Trabalho Escritório", callback_data="trabalhoEscritorio")
        )

    return markup
#####################################################################

#Funcao para fazer query em tabelas do BQ
#####################################################################
def envia_menu(message):
    bot.send_message(message.chat.id,"💡 Automações Yeelight 💡",reply_markup=gerar_botoes("automacoes_lampada"))
#####################################################################