FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DB_PATH=/app/data/caselog.db
EXPOSE 8080
CMD ["gunicorn", "server:app", "--bind", "0.0.0.0:8080"]
