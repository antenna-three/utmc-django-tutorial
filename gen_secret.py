from django.core.management.utils import get_random_secret_key

with open('gasshuku/local_settings.py', 'w', encoding='utf-8') as f:
    f.write(f"SECRET_KEY = '{get_random_secret_key()}'")
