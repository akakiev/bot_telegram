import asyncio
import logging
import sys
from app import main

# Main function
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    