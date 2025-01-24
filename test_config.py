import configparser

def test_conf():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config.ini') 
    config.sections()

    prop = config["sectionA"].get("prop") #Строка
    prop_int = config["sectionA"].getint("prop_init") #Число

    print(prop_int / 1)