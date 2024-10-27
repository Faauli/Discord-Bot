# Discord Bot

A simple Discord bot built with Python using the `py-cord` library.

## Features

- Examples for your own bot.
- Integrates with MongoDB for data storage
- Explanation of the code.

## Installation

1. Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the root directory of your project with the following content:
   ```env
   TOKEN=your_bot_token
   MONGO_URI=your_mongo_uri
   ```
   Replace `your_bot_token` with your actual Discord bot token and `your_mongo_uri` with your MongoDB connection string.

3. Run the bot by executing the following command:
   ```bash
   python main.py
   ```
   Replace `main.py` with the name of your main bot file if necessary.

## Usage

After starting the bot, it will be active in your Discord server. You can use the commands defined in your bot's code to interact with it.

