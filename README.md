## walkthrough

1. install & start redis broker

```sh
brew install redis
redis-server
```

2. install deps

```sh
uv sync
```

3. run worker

```sh
uv run --env-file=.env celery --app=tasks worker --loglevel=DEBUG
```

4. run test

```sh
uv run --env-file=.env python -m pytest
```

5. open flower web ui

```sh
uv run --env-file=.env celery flower
open http://0.0.0.0:5555
```
