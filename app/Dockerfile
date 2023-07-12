FROM python:3.8.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9527
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9527"]