FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pydantic paho-mqtt
EXPOSE 8000
CMD ["python", "main.py"]