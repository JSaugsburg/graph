import msal
import configparser

config = configparser.ConfigParser()
config.read("cfg.ini")
config = config["graph"]

app = msal.ConfidentialClientApplication(
    config["client_id"], authority=config["authority"],
    client_credential=config["secret"])

print("get token")
result = app.acquire_token_for_client(scopes=[config["scope"]])
