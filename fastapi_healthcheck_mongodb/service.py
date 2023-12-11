from fastapi_healthcheck.service import HealthCheckBase
from fastapi_healthcheck.enum import HealthCheckStatusEnum
from fastapi_healthcheck.domain import HealthCheckInterface
from typing import List, Optional
from pymongo import MongoClient


class HealthCheckMongoDB(HealthCheckBase, HealthCheckInterface):
    _connectionUri: str
    _database: str
    _message: str

    def __init__(
        self,
        connectionUri: str,
        database: str,
        alias: str,
        tags: Optional[List[str]] = None,
    ) -> None:
        self._connectionUri = connectionUri
        self._alias = alias
        self._database = database
        self._tags = tags

    def __checkHealth__(self) -> HealthCheckStatusEnum:
        res: HealthCheckStatusEnum = HealthCheckStatusEnum.UNHEALTHY
        try:
            client = MongoClient(self._connectionUri)
            if client.server_info():
                res = HealthCheckStatusEnum.HEALTHY
        except Exception as e:
            pass
        return res
