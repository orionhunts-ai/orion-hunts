#Python implementation of OrionHunts
import os
from dotenv import load_dotenv


load_dotenv()

db_uri = os.getenv("DB_URI")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")
wandb_project = os.getenv("WANDB_PROJECT")
wandb_entity = os.getenv("WANDB_ENTITY")