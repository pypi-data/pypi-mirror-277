import requests
import requests.packages.urllib3.exceptions as urllib3_exceptions
import ssl
import warnings
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

warnings.simplefilter("ignore", urllib3_exceptions.InsecureRequestWarning)


class UnsafeRenegotiationAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        """
            允许不安全的旧版重新协商
            """
        context = ssl.create_default_context()
        # context.options |= ssl.OP_LEGACY_SERVER_CONNECT
        context.check_hostname = False
        context.set_ciphers("DEFAULT@SECLEVEL=1")
        context.options |= 0x4
        kwargs["ssl_context"] = context
        return super().init_poolmanager(*args, **kwargs)
