# timeproject25

# Time project system (timeproject25)

Useful tools for timetable management

## Install the dependencies
```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```


### Lint the files
```bash
yarn lint
# or
npm run lint
```


### Format the files
```bash
yarn format
# or
npm run format
```


### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).

# timeproject25 drf backend

`.\venv\Scripts\activate`

`pip install -r requirements.txt`

`python manage.py runserver`

`python manage.py update_admin -u hello -p pepa`

`python manage.py migrate`

`docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:17.4-alpine3.21`

`docker run --name some-redis -p 6379:6379 -d redis:7.4.2-alpine`



### docker run

* `--name` Assign a name to the container
* `-e`, `--env` Set environment variables
* `-d`, `--detach` Run container in background and print container ID


### Celery

`celery -A timeproject25 worker -l INFO`


