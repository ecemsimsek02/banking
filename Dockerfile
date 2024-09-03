FROM python:3.9-slim


WORKDIR /home/sysadmin/bank/bank


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python3", "manage.py", "runserver", "0.0.0.0:${DJANGO_PORT}"]
