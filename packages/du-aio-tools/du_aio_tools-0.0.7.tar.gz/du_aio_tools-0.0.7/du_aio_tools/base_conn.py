# -*- coding: utf-8 -*-
# @time: 2024/2/18 9:49
# @author: Dyz
# @file: base_conn.py
# @software: PyCharm
import functools
import warnings
from typing import Optional

from loguru import logger
from tortoise import BaseDBAsyncClient, models, fields, Tortoise


async def init_db(tortoise_orm, create: bool = False):
    """
    >>> {
        "connections": {
            "conn": {
                "engine": f"tortoise.backends.mysql",  # mysql/asyncpg/sqlite
                "credentials": {
                    'host': 'localhost',
                    'port': 3306,
                    'user': 'root',
                    'password': 'xxx',
                    'database': 'db_name',
                    'charset': 'utf8mb4'
                }
            }
        },
        "apps": {
            "jour": {"models": ["__main__"], "default_connection": "conn"},
        },
        'use_tz': False,
        'timezone': 'Asia/Shanghai',
    }
    """
    await Tortoise.init(
        config=tortoise_orm
    )
    if create:
        await Tortoise.generate_schemas()


async def close_db():
    """关闭数据库连接"""
    await Tortoise.close_connections()


def load_db(tortoise_orm, create: bool = False):
    """
    tortoise_orm: 数据库链接配置
    create: 创建表
    """

    def _load_db(func):
        """加载数据库"""

        @functools.wraps(func)
        async def wrap(*args, **kwargs):
            await init_db(tortoise_orm, create)

            result = await func(*args, **kwargs)

            await close_db()
            return result

        return wrap

    return _load_db


class BaseModel(models.Model):
    """基础模型类，包含创建时间和更新时间"""
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True  # 标记为抽象类，不直接创建表

    @classmethod
    async def truncate_model(cls, using_db: Optional[BaseDBAsyncClient] = None):
        """截断表"""
        db = using_db or cls._choose_db(True)
        data = await cls.all().limit(1)
        if data:
            logger.info(f'截断表[{cls._meta.db_table}]')
            return await db.execute_query(f'TRUNCATE TABLE {cls._meta.db_table}')
        logger.warning(f'TABLE {cls._meta.db_table} 不存在数据!')

    @classmethod
    async def copy_old(cls, using_db: Optional[BaseDBAsyncClient] = None, name='_old'):
        """复制表"""
        db = using_db or cls._choose_db(True)
        _table = cls._meta.db_table
        old_table = _table + name
        data = await cls.all().limit(1)
        if data:
            await db.execute_query(f'DROP TABLE IF EXISTS {old_table}')
            return await db.execute_query(f'CREATE TABLE {old_table} SELECT * FROM {_table}')
