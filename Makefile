# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'

help:           									## Show this help.
	@fgrep -h '##' $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

todo:											## Show all comments started with `# TODO:`
	grep '# TODO:' src/slink/ -r --exclude Makefile --exclude README.md --exclude-dir db

install: install-pip install-migrate install-createsuperuser  		## Install and config project.

install-pip:  										## Install deps and whole project as a package.
	pip install -r requirements.txt -e .

install-migrate:  									## Apply migrations.
	slink migrate

install-createsuperuser:  								## Create superuser.
	slink shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" 2> /dev/null || true

run: 									## Run server.
	slink runserver 0.0.0.0:8000
