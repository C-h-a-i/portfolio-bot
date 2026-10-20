# Portfolio Bot

A Telegram bot that will grow into a tool for tracking your stock portfolio. The first version says hello and responds to a few commands.

## What you need

- Python 3.10 or newer
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

## Run it on your computer

1. Install Python if you do not have it already.
2. Download or clone this repository, then open its folder in a code editor such as Visual Studio Code.
3. Open a terminal in that folder and install the bot's packages:

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

   On Windows, activate the environment with `.venv\\Scripts\\activate` instead.
4. Copy `.env.example` to a file named `.env`. Put the token from BotFather after `TELEGRAM_BOT_TOKEN=`.
5. Set the token in your terminal, then start the bot:

   macOS/Linux:
   ```sh
   export TELEGRAM_BOT_TOKEN="your-token-from-botfather"
   python bot.py
   ```

   Windows PowerShell:
   ```powershell
   $env:TELEGRAM_BOT_TOKEN="your-token-from-botfather"
   python bot.py
   ```

6. Open your bot in Telegram and send `/start`, `/help`, or `/ping`.

The bot stays online only while this program is running on your computer. Stop it with Ctrl+C.

## Keep your token private

Your Telegram bot token is like a password. Do not paste it into `bot.py`, commit it to GitHub, or share it in a chat. The real `.env` file is ignored by Git; only the placeholder `.env.example` belongs in the repository. If a real token is ever shared by mistake, ask BotFather to revoke it and create a new one.

## Current commands

- `/start` — welcome message
- `/help` — list commands
- `/ping` — check that the bot is online

The bot does not store portfolio data or make investment recommendations yet.
