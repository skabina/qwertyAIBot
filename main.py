import os
from ollama import ChatResponse, chat 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Завантажте токен з змінної середовища
BOTTOKEN = "Your token"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text  
    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': user_message,
        },
    ])
    
    await update.message.reply_text(response.message.content)

app = ApplicationBuilder().token(BOTTOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
