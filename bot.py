import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Welcome the user and explain what the starter bot can do."""
    if update.message:
        await update.message.reply_text(
            "Hi! I'm your portfolio bot 👋\n\n"
            "I'm just getting started. Try /help to see what I can do."
        )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Show the available commands."""
    if update.message:
        await update.message.reply_text(
            "Here are my commands:\n"
            "/start — say hello\n"
            "/help — show this help message\n"
            "/ping — check that I'm online"
        )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirm that the bot is running."""
    if update.message:
        await update.message.reply_text("Pong! I'm online ✅")


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is missing. Add your bot token as an "
            "environment variable before starting the bot."
        )

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping))

    logger.info("Bot is starting. Press Ctrl+C to stop.")
    application.run_polling()


if __name__ == "__main__":
    main()
