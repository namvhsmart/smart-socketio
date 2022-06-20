To deploy, config supervisor using 
```
[program:smart_socketio]
environment=FLASK_ENV=production
user = ubuntu
directory = /home/ubuntu/smart-socketio
command = /home/ubuntu/smart-socketio/.venv/bin/gunicorn --bind 0.0.0.0:5001 --worker-class eventlet -w 1 app:app
priority = 900
autostart = true
autorestart = true
stopsignal = TERM
redirect_stderr = true
```
```
gunicorn --bind 0.0.0.0:5001 --worker-class eventlet -w 1 app:app
```