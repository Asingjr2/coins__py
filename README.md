# COINS

Cryptocurrency data display using coinbase api.

## DJANGO Installation
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations prices
python manage.py makemigrations --empty prices
replace migration file with data_load.py langauage
python manage.py migrate
python manage.py runserver

*Update price information using admin management command: 'python manage.py price_update'
```
