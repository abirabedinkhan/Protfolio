# Portfolio

This is a Flask and MySQL-powered Portfolio website, combining the flexibility of Flask with the robustness of MySQL for data management. It serves as a dynamic platform for showcasing personal or professional achievements.

## Run the App
```bash
git clone https://github.com/abirabedinkhan/Protfolio
```
### Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate # linux & mac only
```

### Setup the project by running the script
Run this script
```bash
python3 setup_conf.py
```
You will be prompted to set various configurations:
```log
[+] Welcome to Portfolio configuration!!!

[+] Installing requirements
...

[+] Set Debug (Default: False) :
[+] Set Secret Key (Default: *RANDOM*) :

[+] Set server host (Default: 0.0.0.0) :
[+] Set server port (Default: 80) : 9090

[+] Set mysql host (Default: localhost) :
[+] Set mysql user : root
[+] Set mysql password : root # Don't use this as mysql password
[+] Set mysql db (Default: portfolio) :
```
After completing the configuration, a `config.json` file will be generated in your project directory:
```json
{
    "env": {
        "debug": true,
        "secret_key": "203e39a47b5b57ebf24fc3bfdd68bc3652ee88cbe02a76f3badf2094616a958e"
    },
    "server": {
        "host": "0.0.0.0",
        "port": "9090"
    },
    "db": {
        "MYSQL_HOST": "localhost",
        "MYSQL_USER": "root",
        "MYSQL_PASSWORD": "root",
        "MYSQL_DB": "protfolio"
    }
}
```
Feel free to modify the configurations in the `config.json` file as needed.

### Finally, run the application
```bash
python3 app.py
```