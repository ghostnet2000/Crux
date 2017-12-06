pip install -r requirements/dev.txt
python ./manage.py collectstatic --noinput
python ./manage.py migrate --noinput
