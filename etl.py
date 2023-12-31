import aiohttp
import datetime as dt
import urllib.parse
import urllib3
import os

class ETL:

    def __init__(self):
        
        self.pi_headers = {"Content-type": "application/json", "X-Requested-With": "XmlHttpRequest"}
        self.pi_url = "https://sg-piintegrator.scrubgrass.com/piwebapi/points?path=\\SCRPIP01\\"
        self.pi_user = os.getenv("PI_USER")
        self.pi_password = os.getenv("PI_PASSWORD")
        self.pjm_api_key = os.getenv("PJM_API_KEY")
        self.pjm_headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "ACCEPT-ENCODING": "gzip, deflate, br","Ocp-Apim-Subscription-Key": self.pjm_api_key}
        self.pjm_url_prefix = "https://api.pjm.com/api/v1/rt_unverified_fivemin_lmps?pnode_id="
    
    def get_timestamp(self):
        return dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def get_pjm_params(self):
        timestamp = self.get_timestamp()
        return urllib.parse.urlencode({"download": True,"rowCount": 1,"startRow": 1,"datetime_beginning_ept": timestamp})

    async def extract_lmp(self, url, session):
        try:
            async with session.get(url, headers=self.pjm_headers) as response:
                if response.status == 200:
                    r = await response.json(content_type="application/octet-stream")
                    return r[0]["total_lmp_rt"]
        except Exception as e:
            print(e)

    async def load_pi(self, path, data, session):
        try:
            async with session.get(path,auth=aiohttp.BasicAuth(self.pi_user, self.pi_password),ssl=False,headers=self.pi_headers) as response:
                if response.status == 200:
                    r = await response.json()
                    await session.post(r["Links"]["Value"],auth=aiohttp.BasicAuth(self.pi_user, self.pi_password),ssl=False,json={"Value": data},headers=self.pi_headers)
        except Exception as e:
                    print(e)
