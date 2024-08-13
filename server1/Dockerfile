
FROM python:3.11.4

WORKDIR /server1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000


CMD ["python", "server1.py"]
