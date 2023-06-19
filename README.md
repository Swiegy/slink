# SLink

Link shortener.

## Requirements

* Python 3.11+
* virtualenv 20.23.0+

We **highly recommend** using `virtualenv` :)
```bash
virtualenv --python=/usr/bin/python3.11 env
source env/bin/activate
```

## Installation

Use `Makefile` command.

```bash
make install
```
or manually

```bash
# Install python dependencies and whole project as a python package
pip install -r requirements.txt -e .

# Apply migrations
slink migrate

# Create superuser
slink shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
```

## Usage

Use `Makefile` command.

```bash
make run
```
or manually

```bash
slink runserver
```

## API
```bash
POST: http://127.0.0.1:8000/ < {"url": "<target_url>"}
RESPONSE: {"url": "<target_url>", "short": "<shorted_url>"}
```
```bash
GET: http://127.0.0.1:8000/<shorted_url_hash>  # shorted_url_hash == pk
RESPONSE: {"url": "<target_url>", "short": "<short_url>"}
```

## DOCKER
```bash
docker-compose up
```