from lib.client import Client
import os
import pathlib	
import json

def get_latest_client() -> Client:
        client_latest = Client("")
        client_latest.major = client_latest.build = client_latest.revision = 0
        client_latest.connect("game.brawlstarsgame.com")
        return client_latest

def main():
    dir_path = pathlib.Path(__file__).parent
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".json"):
                filechange(os.path.join(root, file))


def filechange(address):
    with open(address) as f:
        fl = f.read()
        fl = json.loads(fl)
    client = get_latest_client()
    version = client.content_version
    fl["version"] = version[0]
    fl["minor"] = version[1]
    fl["build"] = version[2]
    fl["hash"] = client.content_hash
    with open(address,"w") as f:
        f.write(json.dumps(fl))
        
if __name__ == "__main__":
    main()
