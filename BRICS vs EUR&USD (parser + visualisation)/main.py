import asyncio
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn

from queries.core import SyncCore


async def main():
    # ========== SYNC ==========
    # CORE
    if "--core" in sys.argv and "--sync" in sys.argv:
        SyncCore.create_tables()
        SyncCore.full_parsing_to_table()

        SyncCore.get_csv('currencies_parser/data.csv')


if __name__ == "__main__":
    asyncio.run(main())
