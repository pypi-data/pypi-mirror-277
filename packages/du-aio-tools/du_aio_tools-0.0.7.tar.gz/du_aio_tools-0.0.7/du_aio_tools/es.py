# -*- coding: utf-8 -*-
# @Time: 2024/6/6 下午3:20
# @Author: dyz
# es 的一些使用
import asyncio
import functools
from loguru import logger
from typing import Union, List
from elasticsearch_dsl import AsyncIndex, Index
from elasticsearch_dsl import AsyncDocument, Document
from elasticsearch_dsl._async.document import AsyncIndexMeta
from elasticsearch_dsl._sync.document import IndexMeta


def __get_refresh(settings: dict, name) -> dict:
    return settings.get(name, {}).get("settings", {}).get("index", {}).get("refresh_interval", "")


async def aio_get_refresh(es_index: AsyncIndex, name):
    """异步关闭自动刷新"""
    settings = await es_index.get_settings()
    return __get_refresh(settings, name)


def get_refresh(es_index: Index, name):
    settings = es_index.get_settings()
    return __get_refresh(settings, name)


def auto_refresh(es_model: str):
    """
    临时关闭自动刷新
    批量操作结束后立刻刷新一次，并恢复自动刷新
    """

    def _load_refresh(func):
        """加载数据库"""

        if asyncio.iscoroutinefunction(func):
            @functools.wraps(func)
            async def wrap(*args, **kwargs):
                _temp_index = AsyncIndex(es_model)

                refresh_interval = await aio_get_refresh(_temp_index, es_model)
                if refresh_interval != '-1':
                    # 禁用自动刷新
                    _temp_index.settings(refresh_interval='-1')
                    await _temp_index.save()
                    logger.info(f'已禁用索引:{es_model} 的自动刷新')
                    try:
                        result = await func(*args, **kwargs)
                    finally:
                        await _temp_index.refresh()  # 立即刷新一次
                        logger.info(f'索引:{es_model} 已经刷新')
                        _temp_index.settings(refresh_interval=refresh_interval)  # 修改回原本的刷新频率
                        await _temp_index.save()
                        logger.info(f'已将索引:{es_model} 的自动刷新重新设置为:{refresh_interval}')
                return result

            return wrap
        else:
            @functools.wraps(func)
            def wrap(*args, **kwargs):
                _temp_index = Index(es_model)
                refresh_interval = get_refresh(_temp_index, es_model)
                if refresh_interval != '-1':
                    # 禁用自动刷新
                    _temp_index.settings(refresh_interval='-1')
                    _temp_index.save()
                    logger.info(f'已禁用索引:{es_model} 的自动刷新')

                    try:
                        result = func(*args, **kwargs)
                    finally:
                        _temp_index.refresh()  # 立即刷新一次
                        logger.info(f'索引:{es_model} 已经刷新')
                        _temp_index.settings(refresh_interval=refresh_interval)  # 修改回原本的刷新频率
                        _temp_index.save()
                        logger.info(f'已将索引:{es_model} 的自动刷新重新设置为:{refresh_interval}')
                return result

            return wrap

    return _load_refresh
