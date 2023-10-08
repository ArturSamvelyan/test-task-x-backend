import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_KEY = os.getenv("OPENAI_KEY")

DATASET_FOLDER = "./static/"
DB_PATH = os.path.join(DATASET_FOLDER, "database.chroma")
