# coding: UTF-8
import config.py
from mastodon import *

# ログイン
mastodon = Mastodon(
    client_id = config.MSTDN_CLIENT.get("key"),
    client_secret = config.MSTDN_CLIENT.get("secret"),
    access_token = config.MSTDN_CLIENT.get("token"),
    api_base_url = config.MSTDN_CLIENT.get("base_url"),
)

user_id = config.USER_ID

list = mastodon.account_followers(user_id)
for id in list:
    mastodon.account_follow(id["id"])
