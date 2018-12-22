# paxos
Coding Challenge

Requires a self signed certificate

```openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt```

```docker-compose up -d && python /path/to/test.py --domain localhost --port 5000 --cert-path /path/to/localhost.crt```