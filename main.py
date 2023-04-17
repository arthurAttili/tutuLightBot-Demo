from configs import *
from utils import *
from funcoesYeelight import *


    
#Ações que devem ser realizadas pelos comandos
#####################################################################
#Luzes
#############################
def hora_do_cafe(call):
    bot.send_message(call.message.chat.id,horaDoCafe_yeelight())
def hora_do_jogo(call):
    bot.send_message(call.message.chat.id,horaDoJogo_yeelight())
def hora_do_dino(call):
    bot.send_message(call.message.chat.id,horaDoDino_yeelight())
def hora_do_trabalho(call):
    bot.send_message(call.message.chat.id,horaDoTrabalho_yeelight())

def boa_noite(call):
    bot.send_message(call.message.chat.id,boaNoite_yeelight())
def arthur_dormir(call):
    bot.send_message(call.message.chat.id,arthurDormir_yeelight())
def trabalho_escritorio(call):
    bot.send_message(call.message.chat.id,trabalhoEscritorio_yeelight())
#############################
#####################################################################

#Acionador Inicial
#####################################################################
@bot.message_handler(content_types=["text"])
def responder(message):
    #print(message) #Útil para debugar
    if message.chat.id == USER_ID_1 or message.chat.id == USER_ID_2:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        textoEntrada = f'Olá, <b>{first_name} {last_name}</b>! Tudo bom? Escolha um comando para continuar!'
        bot.reply_to(message,textoEntrada,parse_mode='html')
        
        envia_menu(message)
    else:
        texto = "Você não é o Tutu ou a Carol!! Saia já daqui!"
        bot.reply_to(message,texto)
#####################################################################

#Acionador Funções
#####################################################################
@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "horaDoTrabalho":
        bot.answer_callback_query(call.id, "Hora do Trabalho Ativado!")
        hora_do_trabalho(call)
    if call.data == "horaDoCafe":
        bot.answer_callback_query(call.id, "Hora do Café Ativado!")
        hora_do_cafe(call)
    if call.data == "horaDoJogo":
        bot.answer_callback_query(call.id, "Hora do Jogo Ativado!")
        hora_do_jogo(call)
    if call.data == "horaDoDino":
        bot.answer_callback_query(call.id, "Hora do Dino Ativado!")
        hora_do_dino(call)
    if call.data == "boaNoite":
        bot.answer_callback_query(call.id, "Boa Noite Ativado!")
        boa_noite(call)
    if call.data == "oArthurVaiDormir":
        bot.answer_callback_query(call.id, "Arthur Dormir Ativado!")
        arthur_dormir(call)
    if call.data == "trabalhoEscritorio":
        bot.answer_callback_query(call.id, "Trabalho Escritório Ativado!")
        trabalho_escritorio(call)
#####################################################################

#Ativa o bot.
bot.infinity_polling(timeout=10, long_polling_timeout = 5)