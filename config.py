# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MSTDN_CLIENT = {
  key: os.environ.get("API_KEY"),
  secret: os.environ.get("API_SECRET"),
  token: os.environ.get("API_TOKEN"),
  base_url: os.environ.get("BASE_URL")
}

USER_ID = os.environ.get("USER_ID")
