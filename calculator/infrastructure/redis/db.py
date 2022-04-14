import redis 
import os 

DB_URL = os.get_env("DB_URL")
engine = redis.Redis(DB_URL)