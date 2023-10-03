# Fork Monitor
Ethereum Classic Hard-Fork Monitor

- Live: https://fork-monitor.etc-network.info
- Testnet: https://fork-monitor-mordor.etc-network.info
- Testnet: https://kotti.fork.fault.dev Will be decommisioned !

### Install

```bash
pip install -r requirements.txt
```

### Dockerfile
```bash
docker build -t fork-monitor:latest .
docker run -p 5000:5000 fork-monitor:latest
```

You can now see the webinterface under localhost:5000

### Run

```bash
FLASK_APP="./app/main.py" FLASK_RUN_PORT=15674 flask run
```
