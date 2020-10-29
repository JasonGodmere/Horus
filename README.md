# Horus

Horus is a SaaS application for monitoring system information on remote servers

The "Horus" application is meant to run as a server node that hosts the website and houses the database.
Server information is routed through the site via websocket and forwarded to the appropriate clients in
real time.

Each server a client wishes to track will need to have an instance of [Eye-Of-Horus](https://github.com/JasonGodmere/Eye-Of-Horus) running in order to
communicate with the site.

All sensitive client information stored in the Horus database will be encrypted using a key only the client
has access to. This prevents anyone unauthorized from seeing the data but unfortunately makes recovering a lost
key impossible as the host does not store passwords and all sensitive information is encrypted to the lost key.

## Installation

#### Clone Repo

```bash
git clone https://github.com/JasonGodmere/Horus.git
```
>The settings.py file in the "hserver" directory has a default encryption and sqlite3 database. Please change these
>if you plan on deploying this server and set debug=False.

#### Python Packages

```bash
pip install -r requirements.txt
```

#### Redis

```bash
docker run -p 6379:6379 -d redis:2.8
```
>You can use docker or run redis natively by downloading it here: [https://redis.io/download](https://redis.io/download) \
>If you would like to run redis on a port other than 6379 please specify it in the settings.py file under CHANNEL_LAYERS