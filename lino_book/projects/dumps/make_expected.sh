#
echo "This will overwrite the database dumps in a and b."
echo "Are you sure?"

python manage_a.py initdb_demo --noinput
python manage_a.py dump2py a --overwrite

python manage_b.py initdb_demo --noinput
python manage_b.py dump2py b --overwrite

