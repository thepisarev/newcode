#!/usr/bin/env python3
"""
Telegram бот для игр Нового кода НЛП
Запускает Web Apps по командам
"""

from telegram import Update, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ТВОЙ ТОКЕН ОТ @BotFather (замени на свой!)
BOT_TOKEN = "8543122393:AAE3criDfc51Wd_mW6gVet5pkS8DSrBS6vo"

# URL твоих игр
ALPHABET_URL = "https://thepisarev.github.io/newcode/alphabet.html"
RAINBOW_URL = "https://thepisarev.github.io/newcode/rainbow.html"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start"""
    keyboard = [
        [
            InlineKeyboardButton("🔤 Алфавит", web_app=WebAppInfo(url=ALPHABET_URL)),
            InlineKeyboardButton("🌈 Радуга", web_app=WebAppInfo(url=RAINBOW_URL))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🧠 *Добро пожаловать в Игры Нового кода НЛП!*\n\n"
        "Входите в состояние мастерства, активируйте оба полушария мозга "
        "и восстановите связь с бессознательным.\n\n"
        "🔤 *Алфавит* — игра с буквами и руками\n"
        "🌈 *Радуга* — тренировка через эффект Струпа\n\n"
        "Выберите игру:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def alphabet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /alphabet"""
    keyboard = [[InlineKeyboardButton("🔤 Играть в Алфавит", web_app=WebAppInfo(url=ALPHABET_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🔤 *Игра Алфавит*\n\n"
        "Читай буквы вслух и поднимай руки согласно подсказкам:\n"
        "• Л — левая рука\n"
        "• П — правая рука\n"
        "• О — обе руки\n\n"
        "Войдите в высокопродуктивное состояние!",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def rainbow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /rainbow"""
    keyboard = [[InlineKeyboardButton("🌈 Играть в Радугу", web_app=WebAppInfo(url=RAINBOW_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🌈 *Игра Радуга (Светофор)*\n\n"
        "Называй ЦВЕТ текста, а не само слово!\n\n"
        "Это эффект Струпа — когда мозг хочет прочитать слово, "
        "но нужно назвать цвет букв. Отличная тренировка когнитивной гибкости!",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /help"""
    await update.message.reply_text(
        "ℹ️ *Помощь*\n\n"
        "*Доступные команды:*\n"
        "/start — Главное меню\n"
        "/alphabet — 🔤 Игра Алфавит\n"
        "/rainbow — 🌈 Игра Радуга\n"
        "/help — Эта справка\n\n"
        "*Как играть:*\n"
        "1. Поставьте цель для бессознательного\n"
        "2. Запустите игру (минимум 15 минут)\n"
        "3. Войдите в транс и практикуйте\n"
        "4. После завершения прочувствуйте результат\n\n"
        "*Методология:*\n"
        "Игры основаны на Новом коде НЛП — активируют оба полушария "
        "мозга одновременно, помогают войти во внешне ориентированный транс "
        "и восстановить связь с бессознательным.\n\n"
        "🧠 Приятной практики!",
        parse_mode='Markdown'
    )


def main():
    """Запуск бота"""
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("alphabet", alphabet))
    application.add_handler(CommandHandler("rainbow", rainbow))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    logger.info("Бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
