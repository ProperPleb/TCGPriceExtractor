import yaml

DEFAULT_PATH = "../resources/"
CONFIG_FILE = "config.yml"

with open(DEFAULT_PATH + CONFIG_FILE, 'r') as file:
    conf = yaml.safe_load(file)


def config(path: str):
    path_list = path.split('.')
    depth = conf[path_list.pop(0)]
    for p in path_list:
        depth = depth[p]
    return depth
