from collections.abc import Callable
import logging

#
# This class is borrowed from: https://github.com/natekspencer/vivintpy/blob/main/vivintpy/entity.py
#
UPDATE = "update"
_LOGGER = logging.getLogger(__name__)


class Entity:
    """
    A class representing an entity.
    """

    def __init__(self, data: dict):
        self.__data = data
        self._listeners: dict[str, list[Callable]] = {}

    @property
    def data(self) -> dict:
        """
        Returns the raw data of the entity.
        :return: The raw data of the entity.
        """
        return self.__data

    async def update_data(self, data: dict, override: bool = False):
        self.__data = data
        _LOGGER.debug(f"Updated data: {data}")
        await self.emit(UPDATE, {"data": data})

    def on(self, event_name: str, callback: Callable) -> Callable:
        listeners = self._listeners.get(event_name, [])
        listeners.append(callback)

        def unsubscribe():
            if callback in listeners:
                listeners.remove(callback)

        return unsubscribe

    async def emit(self, event_name: str, data: dict) -> None:
        for listener in self._listeners.get(event_name, []):
            try:
                await listener(data)
            except:
                pass

