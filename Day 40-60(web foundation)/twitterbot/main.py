import os
import dotenv
from bot import InternetSpeedTwitterBot

TARGET_SPEED_UP = 150
TARGET_SPEED_DOWN = 80

dotenv.load_dotenv()

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
if bot.up < TARGET_SPEED_UP or bot.down < TARGET_SPEED_DOWN:
    bot.tweet_at_provider(username=os.getenv("USER_NAME"), passwd=os.getenv("PASSWORD"),
                          up=TARGET_SPEED_UP, down=TARGET_SPEED_DOWN)
