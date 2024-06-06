import logging
import yaml
from recursivenamespace import rns
from functools import reduce
import operator

logging.basicConfig(filename='../Polisher.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d :: %(name)s :: %(levelname)s :: %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger('Polisher')


def load_config():
    with open("../config.yaml", "r") as f:
        config = rns(yaml.load(f, Loader=yaml.SafeLoader))
    return config


def get_from_dict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

