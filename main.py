import os
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Handler for file
file_handler = logging.FileHandler('chat.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Logging messages
from datetime import datetime

current_time = datetime.now()
query = f"Currently it is {current_time} over here and I am getting bored, tell me some ironic joke."
logger.info(f"QUERY: {query}")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "user", "content": query},
  ]
)
logger.info(f"REPLY: {response.choices[0].message.content}")