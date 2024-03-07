FROM python:3.11.6-alpine
LABEL maintainer="Mehdi Benouhoud"

COPY ./*.html /app/
COPY ./requirements.txt /app/
COPY server.py /app/

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install uvicorn

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]