import ctypes
import json
import locale
import random
import time
import uuid
from urllib.parse import urlencode

import requests
import wmi

from ok.config.Config import Config
from ok.logging.Logger import get_logger
from ok.util.Handler import Handler

FIREBASE_ENDPOINT = 'https://www.google-analytics.com/mp/collect'

GTAG_ENDPOINT = "https://www.google-analytics.com/g/collect"

logger = get_logger(__name__)


class FireBaseAnalytics:
    def __init__(self, app_config, exit_event):
        self.measurement_id = app_config.get('firebase').get('measurement_id')
        self.api_secret = app_config.get('firebase').get('api_secret')
        self.app_config = app_config
        self._config = None
        self._handler = Handler(exit_event, __name__)
        self._handler.post(self.send_gtag, 0)
        self._user_properties = None
        self._fv = 1

    @property
    def user_properties(self):
        if self._user_properties is None:
            c = wmi.WMI()

            # Get OS information
            os_info = c.Win32_OperatingSystem()[0]
            os_version = os_info.Version.split(".")[0]
            os_build = int(os_info.BuildNumber)

            if os_version == "10" and os_build >= 22000:  # Windows 11 starts from build 22000
                os_version = "11"

            # Get CPU information
            cpu_info = c.Win32_Processor()[0]
            cpu_name = cpu_info.Name.strip()

            # Get total memory (in GB)
            total_memory = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

            # Get graphics card information
            gpu_info = c.Win32_VideoController()
            gpu_name = None
            for gpu in reversed(gpu_info):
                if "intel" not in gpu.Name.lower() and "microsoft" not in gpu.Name.lower():
                    gpu_name = gpu.Name
                    break
            if not gpu_name and gpu_info:
                gpu_name = gpu_info[0].Name

            # Put the information into a dictionary
            self._user_properties = {
                "os": 'windows',
                "os_version": os_version,
                "os_build": os_build,
                "cpu": cpu_name,
                "memory": int(total_memory),
                "gpu": gpu_name
            }
        return self._user_properties

    #
    # def report_open(self):
    #     self._handler.post(self.send_gtag, 5)
    #     # self.send_event('app_open', {'version': self.app_config.get('version'), 'debug': self.app_config.get('debug')})

    @property
    def client_id(self):
        if self._config is None:
            self._config = Config({'client_id': ''}, self.app_config.get("config_folder") or "config", 'statistics')
        if not self._config.get('client_id'):
            self._config['client_id'] = get_unique_client_id()
        else:
            self._fv = 0
        return self._config.get('client_id')

    def send_gtag(self):
        # Define the parameters in a dictionary
        params = {
            'v': '2',
            'tid': self.measurement_id,
            'gtm': '45je4630v9186643593za200',
            '_p': random_number(),
            # 'gcd': '13l3l3l3l1',
            'npa': '0',
            'dma': '0',
            'tag_exp': '0',
            'cid': self.client_id,
            'ul': locale.getdefaultlocale()[0],
            'sr': get_screen_resolution(),
            'uaa': 'x86',
            'uab': '64',
            # 'uafvl': 'Microsoft Edge;125.0.2535.85|Chromium;125.0.6422.142|Not.A/Brand;24.0.0.0',
            'uamb': '0',
            'uam': '',
            'uap': 'Windows',
            'uapv': '15.0.0',
            'uaw': '0',
            'are': '1',
            'frm': '0',
            'pscdl': 'noapi',
            '_s': '1',
            'sid': int(time.time()),
            'sct': '1',
            'seg': '1',
            'dl': 'https://ok-script.com/',
            'dt': 'AppStartGTAG2',
            'en': 'page_view',
            '_ee': '1',
            'ep.version': self.app_config.get('version')
            # 'tfd': '5133'
        }
        if self._fv:
            params['_fv'] = self._fv

        # Send the GET request

        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://ok-script.com',
            'Referer': 'https://ok-script.com/'
        }
        query_string = urlencode(params)

        response = requests.post(f'{GTAG_ENDPOINT}', data=params)

        logger.debug(f'send gtag {GTAG_ENDPOINT}?{query_string}')
        if response.status_code == 204:
            logger.debug(f'Successfully sent gtag')
        else:
            logger.debug(f'Failed to send event: {response.status_code} - {response.text}')

    def send_event(self, event_name, params=None):
        if params is None:
            params = dict()
        payload = {
            'client_id': self.client_id,
            'events': [
                {
                    'name': event_name,
                    'params': params
                }
            ],
            'user_properties': self.user_properties
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            f'{FIREBASE_ENDPOINT}?measurement_id={self.measurement_id}&api_secret={self.api_secret}',
            data=json.dumps(payload),
            headers=headers
        )

        logger.debug(f'send {event_name} {payload}')
        if response.status_code == 204:
            logger.debug(f'Successfully sent event: {event_name}')
        else:
            logger.debug(f'Failed to send event: {response.status_code} - {response.text}')


def get_unique_client_id():
    return f'{random_number()}.{random_number()}'


def random_number():
    return random.randint(0, 2147483647)


def get_screen_resolution():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return f"{screensize[0]}x{screensize[1]}"


if __name__ == '__main__':
    # Generate a unique client ID (UUID)
    client_id = str(uuid.uuid4())
    analytics = FireBaseAnalytics('G-9W3F3EQ19G', api_secret='eAkNmhrERiGg8Q3Riuxerw')
    # Send a test event
    analytics.send_event('app_open')
    analytics.send_event('test1')
    analytics.send_event('test2')
