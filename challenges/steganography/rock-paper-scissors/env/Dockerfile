FROM gcc:latest

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY app app
COPY run.sh /

RUN chmod +x /run.sh

RUN g++ -O2 -o /app/a.out /app/main.cpp

ENTRYPOINT ["./run.sh"]