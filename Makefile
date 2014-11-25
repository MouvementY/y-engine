# These targets are not files
.PHONY: contribute travis test lint coverage prepare_assets

fs:
	foreman start -f Procfile.local

install:
	pip install -r reqs/dev.txt

upgrade:
	pip install --upgrade -r reqs/dev.txt

sync:
	python manage.py migrate

clean:
	# Remove files not in source control
	find . -type f -name "*.pyc" -delete
	rm -rf nosetests.xml coverage.xml htmlcov violations.txt

todo:
	# Look for areas of the code that need updating when some event has taken place
	grep --exclude-dir=components -rnH TODO reqs
	grep --exclude-dir=components -rnH TODO accountant
	grep --exclude-dir=components -rnH TODO tests
