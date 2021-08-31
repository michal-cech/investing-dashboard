from typing import List
from typing import Optional
import strawberry
from python_binance_graphql.binance_client import BinanceClient
from python_binance_graphql.models import SystemStatus, CoinInfo, OldTradeLookup, SavingsPosition, DepositHistory, Snapshot
from os import environ
from python_binance_graphql import BinanceClient, CoinInfo


@strawberry.type
class Query:
    @strawberry.field
    def get_system_status(self) -> SystemStatus:
        client = BinanceClient(api_key=environ.get(
            "BINANCE_API_KEY"), secret=environ.get("BINANCE_SECRET"))
        return client.get_system_status()

    @strawberry.field
    def check_binance_account(self) -> List[CoinInfo]:
        client = BinanceClient(api_key=environ.get(
            "BINANCE_API_KEY"), secret=environ.get("BINANCE_SECRET"))
        return client.get_account_info()

    @strawberry.field
    def check_old_trades(self, symbol: str, fromId: Optional[int] = None, limit: int = 5000) -> List[OldTradeLookup]:
        client = BinanceClient(api_key=environ.get(
            "BINANCE_API_KEY"), secret=environ.get("BINANCE_SECRET"))
        return client.get_old_trades(symbol=symbol, fromId=fromId, limit=limit)

    @strawberry.field
    def get_account_snapshot(self, type: str, startTime: Optional[int] = None, endTime: Optional[int] = None,
                             limit: Optional[int] = None) -> Snapshot:
        client = BinanceClient(api_key=environ.get(
            "BINANCE_API_KEY"), secret=environ.get("BINANCE_SECRET"))
        return client.get_daily_snapshot(type=type, startTime=startTime, endTime=endTime, limit=limit)

    @strawberry.field
    def check_deposit_history(self, coin: Optional[str] = None, status: Optional[int] = None, startTime: Optional[int] = None,
                              endTime: Optional[int] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> List[DepositHistory]:
        client = BinanceClient(api_key=environ.get(
            "BINANCE_API_KEY"), secret=environ.get("BINANCE_SECRET"))
        return client.get_desposit_history(coin=coin, status=status, startTime=startTime, endTime=endTime, offset=offset, limit=limit)

    @strawberry.field
    def get_flexible_savings_position(self, asset: Optional[str] = '') -> List[SavingsPosition]:
        client = BinanceClient(api_key=environ.get(
            "BINANCE_API_KEY"), secret=environ.get("BINANCE_SECRET"))
        return client.get_flexible_savings_positions(asset=asset)


schema = strawberry.Schema(query=Query, subscription=None)
