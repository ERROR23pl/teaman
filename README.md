# TeaMan
this is a secure team management app. It's aim is to make work in small teams easier and more organized.


### Python Setup
#### using pip
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Setup node.js environment if not defined
```bash
pip install nodeenv
nodeenv -p nenv
```

### Run server
in order to start the server run the [tmp.py](./src/server/datasource/tmp.py)

### Run client
ensure node.js has been set up, 
navigate to the [client-app](./src/client-app), 
and type following the prompt
```bash
ng serve
```