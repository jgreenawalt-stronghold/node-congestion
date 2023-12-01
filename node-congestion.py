import json
import datetime
import asyncio
import aiohttp
import nodes

async def extract_lmp(rt_lmp_url, session):
    async with session.get(rt_lmp_url, headers=pjm_headers) as response:
        data = []
        if response.status == 200:
            r = await response.json(content_type="application/octet-stream")
        return data

async def load_pi(path, data, session):
    async with session.get(
        path,
        auth=aiohttp.BasicAuth(pi_user, pi_password),
        ssl=False,
        headers=pi_headers,
    ) as response:
        if response.status == 200:
            r = await response.json()
            await session.post(
                r["Links"]["Value"],
                auth=aiohttp.BasicAuth(pi_user, pi_password),
                ssl=False,
                json=data,
                headers=pi_headers,
            )

async def main():
    async with aiohttp.ClientSession() as session:
        sg_lmp_data = await extract_lmp(sg_lmp_url, session)
        tasks = []
        data_list = sg_lmp_data
        print(data_list)
        #for tag, value in zip(tags, data_list):
            #path = pi_url + tag
            #data = {"Value": value}
            #task = asyncio.ensure_future(load_pi(path, data, session))
            #tasks.append(task)
        #await asyncio.gather(*tasks) 

pjm_url = "https://api.pjm.com/api/v1/rt_unverified_fivemin_lmps?pnode_id={pnode_id}&{pjm_parameters}"

pi_user = "piwebapi_write"
pi_password = "nNRf7USFQ6ca&1"

#if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())
print(nodes.nodes["pnode_id"])





