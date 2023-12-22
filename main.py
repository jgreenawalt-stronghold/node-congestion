import aiohttp
import asyncio
from node import Node
from etl import ETL
from dotenv import load_dotenv

load_dotenv()


async def main():
    async with aiohttp.ClientSession() as session:
        etl = ETL()
        nodes = [Node(**obj) for obj in Node.node_data]
    
        extract_tasks = [etl.extract_lmp(f"{etl.url_prefix}{node.pnode_id}{etl.get_pjm_params()}", session) for node in nodes]
        extracted_prices = await asyncio.gather(*extract_tasks)

        load_tasks = [etl.load_pi(node, data, session) for node, data in zip(nodes, extracted_prices)]
        loaded_price = await asyncio.gather(*load_tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

