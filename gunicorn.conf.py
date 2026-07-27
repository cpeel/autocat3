import multiprocessing

wsgi_app = "wsgi:app"
bind = "0.0.0.0:8000"
worker_class = "gthread"
threads = 10
workers = multiprocessing.cpu_count()

# limit the total number of connections
backlog = 512
worker_connections = 1000

# where to write access and error logs
accesslog = "/var/lib/autocat/log/access.log"
errorlog = "/var/lib/autocat/log/error.log"

try:
    from .local_gunicorn import *
except ImportError:
    pass
