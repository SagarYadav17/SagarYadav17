from os import environ
from dotenv import load_dotenv

load_dotenv()

# Django Config
SECRET_KEY = environ.get("SECRET_KEY")

# News API https://newsapi.org/
NEWS_API_KEY = environ.get("NEWS_API_KEY")
COUNTRIES = ["us", "in", "gb"]
BASE_NEWS_URL = f"https://newsapi.org/v2/top-headlines?apiKey={NEWS_API_KEY}"
CATEGORIES = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology",
]

# Database
# DATABASE_URL = environ.get("DATABASE_URL")

# Sendgrid E-mail
SENDGRID_API = environ.get("SENDGRID_API")
SENDGRID_FROM_MAIL = environ.get("SENDGRID_FROM_MAIL")

# Redis Server
REDIS_URL = environ.get("REDIS_URL")
