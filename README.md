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
uv run celery --app=tasks worker --loglevel=DEBUG
```

4. run test

```sh
uv run python -m pytest
```
