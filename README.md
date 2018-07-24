# Teste de código SenseData

# Install GNU/Linux
``` console
python3 -m venv .venv
source .venv/bin/activate
pip install -r requeriments.txt
FLASK_APP=todo_list.py flask db init
FLASK_APP=todo_list.py flask db migrate
FLASK_APP=todo_list.py flask db upgrade
```
# Tests
# Full Tests 
``` console
pytest todo_list/__
```
# Unittest
``` console
pytest todo_list/tests_unit.py
```
# Functionals
``` console
pytest todo_list/tests_functional.py
```