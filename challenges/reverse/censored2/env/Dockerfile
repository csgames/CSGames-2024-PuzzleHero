FROM python:3.13.0a4-alpine3.19
LABEL maintainer='Nicolas Hurtubise'

COPY ./server.py /server.py
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 9090

ENV CENSORED_INDEX 2
ENV FLAG_CENSORED_1 FLAG{iasudY*YHUnr0fewq78ydgbu2i098haxjcjmi}

CMD ["/entrypoint.sh"]