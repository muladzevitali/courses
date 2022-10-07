import asyncio
from enum import Enum


class ConnectionState(Enum):
    WAIT_INIT = 0
    INITIALIZING = 1
    INITIALIZED = 2


class Connection:
    def __init__(self):
        self._state = ConnectionState.WAIT_INIT
        self._condition = asyncio.Condition()

    async def initialize(self):
        await self._change_state(ConnectionState.INITIALIZING)
        print("initialize: initializing connection...")
        await asyncio.sleep(5)
        print("initialize: finished initializing connection")
        await self._change_state(ConnectionState.INITIALIZED)

    async def _change_state(self, state: ConnectionState):
        async with self._condition:
            print(f"change_state: state changing from {self._state} to {state}")
            self._state = state
            self._condition.notify_all()

    async def execute(self, query: str):
        async with self._condition:
            print("execute: waiting for connection initialize")
            await self._condition.wait_for(self._is_initialized)
            print(f"execute: running {query}")
            await asyncio.sleep(3)

    def _is_initialized(self):
        if self._state is not ConnectionState.INITIALIZED:
            print(f"is initialized: connection not finished initializing, state is {self._state}")
            return False
        return True


async def main():
    connection = Connection()
    query_one = asyncio.create_task(connection.execute("select * from table"))
    query_two = asyncio.create_task(connection.execute("select * from other_table"))

    asyncio.create_task(connection.initialize())
    await query_one
    await query_two


if __name__ == "__main__":
    asyncio.run(main())
