from ticktick.oauth2 import OAuth2
from ticktick.api import TickTickClient
import configparser

config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="UTF-8")

# クライアントIDとかこの辺は環境変数にしたい
client_id = ""
#client_secret = config_ini["TICKTICK"]["secret"]
redirect_uri = "https://api.ticktick.com/"

oauth = OAuth2(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

# a_token = get_access_token(self, check_cache=True, check_env=None)
# print(a_token)

# client = TickTickClient(username, password, auth_client)