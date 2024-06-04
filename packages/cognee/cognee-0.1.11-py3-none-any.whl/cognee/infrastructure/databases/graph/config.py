""" This module contains the configuration for the graph database. """

import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from cognee.infrastructure.databases.relational.config import get_relationaldb_config
from cognee.shared.data_models import GraphDBType, KnowledgeGraph


class GraphConfig(BaseSettings):
    graph_filename: str = "cognee_graph.pkl"
    graph_database_provider: str = "NETWORKX"
    graph_database_url: str = ""
    graph_database_username: str = ""
    graph_database_password: str = ""
    graph_database_port: int = 123
    graph_file_path: str = os.path.join(
        get_relationaldb_config().db_path, graph_filename
    )
    graph_engine: object = GraphDBType.NETWORKX
    graph_model: object = KnowledgeGraph

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    def to_dict(self) -> dict:
        return {
            "graph_filename": self.graph_filename,
            "graph_database_provider": self.graph_database_provider,
            "graph_file_path": self.graph_file_path,
            "graph_database_url": self.graph_database_url,
            "graph_database_username": self.graph_database_username,
            "graph_database_password": self.graph_database_password,
            "graph_database_port": self.graph_database_port,
            "graph_engine": self.graph_engine,
        }


@lru_cache
def get_graph_config():
    return GraphConfig()
