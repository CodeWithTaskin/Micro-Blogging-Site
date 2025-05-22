from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_CONNECTION_URL: str = os.getenv('DATABASE_CONNECTION_URL')