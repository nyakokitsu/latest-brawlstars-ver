import posixpath
from typing import Any
from lib.client import Client, HelloServerResponse
from lib.config import Config
from lib.downloader import Downloader, DownloaderWorker
from lib.item_chain import ItemChain, Item
import os
from shutil import move as fmove
from shutil import copyfile as fcopy
import asyncio

async def get_latest_client() -> Client:
        """
        The function `get_latest_client` returns client with the latest data.
        :return: an instance of the Client class.
        """
        client_latest = Client("")
        client_latest.major = client_latest.build = client_latest.revision = 0
        hui = client_latest.connect("game.brawlstarsgame.com")
        """
        if client_latest == HelloServerResponse.Success:
            print(f"Successfully connected to {self.active_server.short_name}")
        elif client_latest == HelloServerResponse.NeedUpdate:
            print(client_latest.major, client_latest.revision, client_latest.build)
        """
        print(client_latest.content_version, client_latest.content_hash)
        return client_latest


client = asyncio.run(get_latest_client())


