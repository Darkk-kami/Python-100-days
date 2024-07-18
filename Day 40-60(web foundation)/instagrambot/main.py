import os
import dotenv
from bot import InstagramFollowerBot

NAME_TO_FOLLOW =""

dotenv.load_dotenv()

bot = InstagramFollowerBot()

bot.login(os.getenv("user_name"), os.getenv("password"))
bot.find_followers(NAME_TO_FOLLOW)
bot.follow()

