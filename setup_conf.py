import re
import json
import hashlib
import binascii, os

def check_host(host, illegal_char, type):
    host_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|localhost"
    if host in illegal_char: 
        if type == "mysql": host = "localhost"
        elif type == "server": host = "0.0.0.0"
    else:
        host = host.strip()
        if host in illegal_char: 
            if type == "mysql": host = "localhost"
            elif type == "server": host = "0.0.0.0"
        else:
            try: host = re.findall(host_regex, host)[0]
            except: 
                if type == "mysql": host = "localhost"
                elif type == "server": host = "0.0.0.0"
    return host

def main():
    print("[+] Welcome to Portfolio configuration!!!")

    # Env
    debug = input("[+] Set Debug (Default: False) : ")
    secret_key = input("[+] Set Secret Key (Default: *RANDOM*) : ")

    # Server Info
    host = input("[+] Set server host (Default: 0.0.0.0) : ")
    port = input("[+] Set server port (Default: 80) : ")

    # Mysql DB Info
    MYSQL_HOST = input("[+] Set mysql host (Default: localhost) : ")
    MYSQL_USER = input("[+] Set mysql user : ")
    MYSQL_PASSWORD = input("[+] Set mysql password : ")
    MYSQL_DB = input("[+] Set mysql db (Default: portfolio) : ")


    illegal_char = [None, '']

    if debug in illegal_char: debug = False
    else:
        debug = debug.strip()
        try: debug = bool(eval(f"{debug.title()}"))
        except: debug = False

    if secret_key in illegal_char: secret_key = hashlib.sha256(binascii.b2a_hex(os.urandom(15))).hexdigest()
    else:
        secret_key = secret_key.strip()
        if secret_key in illegal_char : hashlib.sha256(binascii.b2a_hex(os.urandom(15))).hexdigest()

    host = check_host(host, illegal_char, "server")

    port_regex = r"\d{1,5}"
    if port in illegal_char: port = "80"
    else:
        port = port.strip()
        if port in illegal_char: port = "80"
        else:
            try: port = re.findall(port_regex, port)[0]
            except: port = "80"

    MYSQL_HOST = check_host(MYSQL_HOST, illegal_char, "mysql")

    if MYSQL_DB in illegal_char: MYSQL_DB = "portfolio"
    else:
        MYSQL_DB = MYSQL_DB.strip()
        if MYSQL_DB in illegal_char: MYSQL_DB = "portfolio"

    
    data = {
        "env": {
            "debug": debug,
            "secret_key": secret_key
        },
        "server": {
            "host": host,
            "port": port
        },
        "db": {
            "MYSQL_HOST": MYSQL_HOST,
            "MYSQL_USER": MYSQL_USER,
            "MYSQL_PASSWORD": MYSQL_PASSWORD,
            "MYSQL_DB": MYSQL_DB
        }
    }

    return data

if __name__ == "__main__":
    json_object = json.dumps(main(), indent=4)
 
    with open("config.json", "w") as outfile:
        outfile.write(json_object)