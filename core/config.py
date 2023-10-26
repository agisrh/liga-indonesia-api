import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

env_files = ["dev.env", "prod.env"]

config = Config()
for env_file in env_files:
    if os.path.exists(env_file):
        config = Config(env_file)

# Base
API_VERSION = config("API_VERSION", cast=str)
DEBUG = config("DEBUG", cast=bool)
PROJECT_NAME = config("PROJECT_NAME", cast=str)
PROJECT_AUTHOR = config("PROJECT_AUTHOR", cast=str)
VERSION = config("VERSION", cast=str, default="1.0.0")

# Scrapers settings
SITE_ENTRYPOINT = config("SITE_ENTRYPOINT", cast=str)
SITE_INDEX = config("SITE_INDEX", cast=str)

SITE_NEWS = config("SITE_NEWS", cast=str)
PLAYLIST = config("PLAYLIST", cast=str)

