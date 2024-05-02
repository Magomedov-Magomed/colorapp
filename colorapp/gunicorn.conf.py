import os

bind = "0.0.0.0:8000"

default_workers = 1

env_workers = os.environ.get("GUNICORN_WORKERS", None)

workers = {
    0: 0,
    None: default_workers,
}.get(env_workers, env_workers)

errorlog = "-"

reuse_port = True

graceful_timeout = 240
max_requests = 10000  # The maximum number of requests a worker will process before restarting.
timeout = 300

reload = False  # Default
if os.environ.get("SERVER_ROLE") == "dev":
    reload = True  # It will cause workers to be restarted whenever application code changes.
    reload_extra_files = ["templates/"]

worker_connections = 2000
