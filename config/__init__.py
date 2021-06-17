"""
Describe: 根据yml文件自动加载配置
Author: Grancis
"""

import os
import sys
import warnings

import yaml

PATH_ROOT = os.path.abspath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
)

def _load_yml(name:str) -> dict:
    """load .yml to python dict

    Args:
        name (str): file name in 'PATH_ROOT/config/yml', **.yml

    Returns:
        dict: python dict
    """
    fp = 'config/yml/' + name
    path = os.path.join(PATH_ROOT, fp)
    with open(path, 'r', encoding='utf-8') as f:
        conf = yaml.load(f, Loader=yaml.Loader)  # yaml.FullLoader

    if conf is None:
        conf = {}

    return conf

class Config(object):
    PATH_ROOT = PATH_ROOT

    def __init__(self):
        super().__init__()
        self._set_default()
        self._set_local()

    def _set_default(self):
        """
        根据 default.yml 载入默认配置
        """
        default_config = _load_yml('default.yml')
        self.parse(default_config)

    def _set_local(self):
        """
        local.yml 中的配置会覆盖 local.yml
        """
        local_config = _load_yml('local.yml')
        self.parse(local_config)

    def parse(self, kw):
        """根据字典kwargs 更新 config参数

        Args:
            kw (dict): set atrr according to dict config
        """
        # 更新配置参数
        for k, v in kw.items():
            # if not hasattr(self, k):
            #     # 警告还是报错，取决于你个人的喜好
            #     warnings.warn("Warning: opt has not attribut %s" %k)
            setattr(self, k, v)
            
        # # 打印配置信息	
        # print('user config:')
        # for k, v in self.__class__.__dict__.items():
        #     if not k.startswith('__'):
        #         print(k, getattr(self, k))

config = Config()