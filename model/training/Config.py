import yaml


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.read_config()

    def read_config(self):
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config

    def get_config(self):
        return self.config

    def get(self, key):
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value[k]
        return value