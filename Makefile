python = python3
pip = pip3


test_fixtures = */fixtures/*.test.json
static_fixtures = */fixtures/*.static.json 

backend-server-start:
	$(python) -u manage.py runserver localhost:8050

install:
	$(pip) install -r requirements.txt 

static:
	$(python) manage.py loaddata $(static_fixtures)

testing:
	$(python) manage.py loaddata $(test_fixtures)

setup:
	$(python) manage.py makemigrations && $(python) manage.py migrate

backend-db-refresh:
	rm -rf db.sqlite3 2>/dev/null
	find . -type d -name migrations | xargs -I {} find {} -type f -name "*.py" | grep -v '__init__.py' | grep -v 'postgres-dev' | xargs rm -f 2>/dev/null
	
