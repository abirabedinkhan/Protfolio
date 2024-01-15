import json

with open('config.json') as config_file:
    config = json.load(config_file)

    """
        This is the config file for the app.
    """
    debug:bool = config['env']['debug']
    secret_key:str = config['env']['secret_key']  
    
    """
        Host and port for the server.
    """
    host:str = config['server']['host']
    port:str = config['server']['port']

    """
        MySQL connection information.
    """
    MYSQL_HOST:str = config['db']['MYSQL_HOST']
    MYSQL_USER:str = config['db']['MYSQL_USER']
    MYSQL_PASSWORD:str = config['db']['MYSQL_PASSWORD']
    MYSQL_DB:str = config['db']['MYSQL_DB']