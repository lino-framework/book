python manage_a.py prep --noinput
python manage_a.py dump2py a --overwrite
python manage_b.py prep --noinput
python manage_b.py dump2py b --overwrite
python manage_b.py dump2py c --overwrite -m 2
