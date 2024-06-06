import asyncio

from asyncio import AbstractEventLoop
from abc import ABCMeta, abstractmethod

from project_utils.conf import ConfigTemplate


class BaseScript(metaclass=ABCMeta):
    config: ConfigTemplate
    loop: AbstractEventLoop

    def __init__(self, config: ConfigTemplate, loop: AbstractEventLoop = asyncio.get_event_loop()):
        self.config = config
        self.loop = loop

    def async_start(self, *args, **kwargs):
        self.loop.run_until_complete(self.handler(*args, **kwargs))

    @abstractmethod
    async def handler(self, *args, **kwargs):
        ...

    @classmethod
    def run(cls, config: ConfigTemplate, *args, **kwargs):
        this: cls = cls(config)
        return this.async_start(*args, **kwargs)

    @classmethod
    def get_instance(cls, config: ConfigTemplate):
        return cls(config)
