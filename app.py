# settings.py
import logging
from dotenv import load_dotenv
env = load_dotenv(".env.local")
from twk_backend.router import app


# Set up root logger to write messages with level INFO or higher to stdout.
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', filename="app.log")

if __name__ == "main":
    app.run(port=5000)  #
