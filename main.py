from mastodon import *

#ログイン
mastodon = Mastodon(
        client_id = "",
        client_secret = "",
        access_token = "",
        api_base_url = "https://インスタンスのURL"
)

user_id = ""
#user_idは http://xxx.xx/web/accounts/hhh ←hhhのところ

list = mastodon.account_followers(user_id)
for id in list:
    mastodon.account_follow(id["id"])
