import yaml 
import os
from box import Box
from src.logging import logger


def read_yaml_file(filepath:str)->Box:
    """
    Read yaml files 
    """
    try:
        with open(filepath,'r') as f:
            content = yaml.safe_load(f)
        logger.debug('Yaml File Successfully Extracted')
        return Box(content)
    except Exception as e:
        logger.debug('Yaml file Extraction Issue',e)

def createdir(dirpath:list):
    try:
        for dir in dirpath:
            os.makedirs(dir,exist_ok=True)
        logger.debug(f'Dir Successfully Created on {dir}')
    except Exception as e:
        logger.debug('Directry creation Issue',e)