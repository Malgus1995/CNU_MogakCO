From ubuntu:16.04

RUN apt update
RUN apt install -y cron

COPY cronjob/task.sh /usr/local/bin/
COPY cron-example /tc/cron.d/
RUN chmod 0644 /etc/cron.d/cron-example

CMD ["cron","-f"]
