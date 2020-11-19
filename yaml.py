import yaml
import os

filePath = os.path.dirname(__file__)
print(filePath)
yamlPath = os.path.join(filePath,'config.yaml')
print(yamlPath)

f = open(yamlPath,'r',encoding='utf-8')
conf = f.read()

config = yaml.load(conf,Loader=yaml.FullLoader)

print(config[ENV])