# timeproject25

[CHANGELOG](CHANGELOG.md)

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

# Rust build

`cargo build` - `--debug` is the default for `cargo build`;

`cargo build --release`

`cargo clean`

# Docker build

`docker build . -t test`

`docker build . -t test --progress=plain --no-cache`

`docker run --rm --name test -p 8080:8080 test`

`docker run --rm --name test -it test sh`

`docker kill test`

`docker rm test`

`docker image rm test`

https://github.com/Luchanso/docker-rust-test/tree/321f4440e50ce3ece32c3f837ec0405eb7731514

`docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:17.4-alpine3.21`

`docker run --name some-redis -p 6379:6379 -d redis:7.4.2-alpine`

### docker run

* `--name` Assign a name to the container
* `-e`, `--env` Set environment variables
* `-d`, `--detach` Run container in background and print container ID
