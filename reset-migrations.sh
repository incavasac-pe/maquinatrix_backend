find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find . -path "*/migrations/*.py" -not -name "*/venv/*/migrations/*.py" -delete
find . -path "*/migrations/*.pyc"  -delete

pip uninstall django
pip install -r requirements.txt
