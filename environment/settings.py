
# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), os.getenv(
    "DASH_ENV_FILE", default =".env.development")
                   )

load_dotenv(dotenv_path=dotenv_path, override=True)

APP_HOST = os.environ.get("HOST")
APP_PORT = int(os.environ.get("PORT"))
APP_DEBUG = bool(os.environ.get("DEBUG"))
DEV_TOOLS_PROPS_CHECK = bool(os.environ.get("DEV_TOOLS_PROPS_CHECK"))
BACKEND = str(os.environ.get("BACKEND"))
