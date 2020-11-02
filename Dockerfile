FROM python:3.7

ADD ./ /opt/server_stat_bot
WORKDIR /opt/server_stat_bot

RUN chmod +x bin/manage \
  && pip install -r requirements/app.txt

ENTRYPOINT ["bin/manage", "start", "--daemon-off"]
