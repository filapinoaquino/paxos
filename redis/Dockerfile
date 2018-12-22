FROM amazonlinux:latest

RUN yum -y update && \
 	yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
	yum -y install redis
COPY redis.conf /etc/

EXPOSE 6379

CMD ["/usr/bin/redis-server", "/etc/redis.conf"]