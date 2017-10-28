set -e
python manage.py prep --noinput --traceback
python manage.py garble_persons --distribution=ee



