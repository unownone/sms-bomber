import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config(object):
    
    MONGO_URI = os.getenv('mongo_uri')
    GOOGLE_CHROME_BIN = os.getenv('chrome_bin')
    CHROMEDRIVER_PATH = os.getenv('chromedriver_path')