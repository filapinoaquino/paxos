FROM amazonlinux:latest

USER root
WORKDIR /app
ADD . /app 

RUN yum -y update && \
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
	python get-pip.py && \
	pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]