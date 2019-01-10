from wxpy import *

api_key = "注册图灵机器人获取的APIkey"
bot = Bot()
tuling = Tuling(api_key=api_key)

my_group = ensure_one(bot.groups.search("微信群名"))
my_friend = ensure_one(bot.friends.search("微信好友备注"))

@bot.register(my_group)
def auto_replay_group(msg):
    tuling.do_reply(msg)

@bot.register(my_friend)
def auto_replay_person(msg):
    tuling.do_reply(msg)

bot.join()