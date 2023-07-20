import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'd3$4jg^k=9^7k!w$zi&w0h4f_pjc45s-^y@i*8gf7#i7d$sgx')
DJANGO_DEBUG = os.getenv('DEBUG', 0)
