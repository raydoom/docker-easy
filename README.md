# docker-easy

## Manage docker servers in webui

This tool is developed to manage distributed docker server centrally.
The module used are:
- python3.6
- Flask  web server
- bootstrap + jquery UI

## Usage

- git clone https://github.com/raydoom/docker-easy.git
- edit config.py

```
from Server import Server

SERVERS = [
    Server(
        name='docker1',
        host='192.168.0.10',
        port=2375,
    ),
    Server(
        name='docker2',
        host='192.168.0.11',
        port=2375,
    )
]

GROUPS = []
```

The docker host must open the Remote API, to do this ,just modify `/etc/docker/daemon.json` on the docker host like:

```
{
	"hosts":["192.168.0.10","unix:///var/run/docker.sock"]
}
```

## Run
run this program  `python webui.py` 
open http://ip:8896/all_servers/

## Todos