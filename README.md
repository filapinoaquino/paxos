# paxos
Coding Challenge

Requires a self signed certificate

Add localhost.key and localhost.crt inside of the flask server folder (use localhost for the Common Name)

```openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt```

Run docker compose in the project root

```docker-compose up -d && python /path/to/test.py --domain localhost --port 5000 --cert-path /path/to/localhost.crt```