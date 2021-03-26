import json

USER= PASS= HOST= DATABASE=''

def init():
    global USER, PASS, HOST, DATABASE
    data = None
    with open('Configs/settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    USER = obj['db_prod']['user']
    HOST = obj['db_prod']['host']
    PASS = obj['db_prod']['pass']
    DATABASE = obj['db_prod']['database']


def get_agent(logger):
    # Using readlines()
    try:
        file = open('Configs/config_struct.txt', 'r')
        Lines = file.readlines()
        file.close()
        for line in Lines:
            if "AGENT" in line:
                value = line.split(">")[1].replace("\n", "")
                if value == "":
                    logger.error("Insira um Agent válido por meio do link: https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html")
                else:
                    agent = value

        return (agent)

    except:
        logger.error("Erro ao obter Agent para o navegador!")