from os import getenv
from typing import Optional

HEALTH_CHECK_TIMEOUT = int(getenv("EDRI_HEALTH_CHECK_TIMEOUT", 10))
TOKEN_LENGTH = int(getenv("EDRI_TOKEN_LENGTH", 64))
REST_RESPONSE_TIMEOUT = int(getenv("EDRI_REST_RESPONSE_TIMEOUT", 60))

SWITCH_KEY_LENGTH = int(getenv("EDRI_SWITCH_KEY_LENGTH ", 8))
SWITCH_HOST = getenv("EDRI_SWITCH_HOST")
SWITCH_PORT = getenv("EDRI_SWITCH_POST")

UPLOAD_FILES_PREFIX = getenv("EDRI_UPLOAD_FILES_PREFIX", "edri_")
UPLOAD_FILES_KEEP_DAYS = int(getenv("EDRI_FILES_KEEP_DAYS", 0))
UPLOAD_FILES_PATH = getenv("EDRI_FILES_PATH", "/tmp/edri")

CACHE_TIMEOUT = int(getenv("EDRI_CACHE_TIMEOUT", 30))
CACHE_INFO_MESSAGE = int(getenv("EDRI_CACHE_INFO_MESSAGE", 60))

HOST = getenv("EDRI_HOST", "localhost")
ws_port_temp = getenv("EDRI_WS_PORT")
WS_PORT: Optional[int] = None
if ws_port_temp:
    WS_PORT = int(ws_port_temp)
else:
    WS_PORT = 8877

rest_port_temp = getenv("EDRI_REST_PORT")
REST_PORT: Optional[int] = None
if rest_port_temp:
    REST_PORT = int(rest_port_temp)
else:
    REST_PORT = 8878
