from bpx.base.base_public import BasePublic
from bpx.http_client.async_http_client import AsyncHttpClient

default_http_client = AsyncHttpClient()


class Public(BasePublic):

    def __init__(self, proxy: str = None, http_client: AsyncHttpClient = default_http_client):
        self.http_client = http_client
        self.http_client.proxy = proxy

    async def get_assets(self):
        return await self.http_client.get(self.get_assets_url())

    async def get_markets(self):
        return await self.http_client.get(self.get_markets_url())

    async def get_ticker(self, symbol: str):
        return await self.http_client.get(self.get_ticker_url(symbol))

    async def get_depth(self, symbol: str):
        return await self.http_client.get(self.get_depth_url(symbol))

    async def get_klines(self, symbol: str, interval: str, start_time: int, end_time=0):
        return await self.http_client.get(self.get_klines_url(symbol, interval, start_time, end_time))

    async def get_status(self):
        return await self.http_client.get(self.get_status_url())

    async def get_ping(self):
        return await self.http_client.get(self.get_ping_url())

    async def get_time(self):
        return await self.http_client.get(self.get_time_url())

    async def get_recent_trades(self, symbol: str, limit=100):
        return await self.http_client.get(self.get_recent_trades_url(symbol, limit))

    async def get_history_trades(self, symbol: str, limit=100, offset=0):
        return await self.http_client.get(self.get_history_trades_url(symbol, limit, offset))
