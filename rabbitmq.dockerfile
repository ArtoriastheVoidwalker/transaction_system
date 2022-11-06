FROM rabbitmq:3.7

RUN apt-get update && apt-get install tzdata -y && rm -rf /var/lib/apt/lists/*

ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq
ENV TZ=Asia/Bishkek

COPY ./scripts/init-rabbitmq.sh /init.sh
RUN chmod +x /init.sh
EXPOSE 15672

CMD ["/init.sh"]