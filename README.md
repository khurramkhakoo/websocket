### Server
Run this websocket server using the following command:
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

You may need to install uvicorn first:
```
pip install 'uvicorn[standard]'
```


### Client
Connect a client to this server using the following command on a terminal:
```
wscat -c ws://localhost:8000/ws
```

You may need to install wscat first:
```
npm install -g wscat
```