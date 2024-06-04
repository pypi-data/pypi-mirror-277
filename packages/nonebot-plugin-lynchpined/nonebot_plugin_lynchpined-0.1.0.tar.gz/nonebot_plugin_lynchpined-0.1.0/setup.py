# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_lynchpined']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-plugin-apscheduler>=0.4.0,<0.5.0', 'requests>=2.32.3,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-lynchpined',
    'version': '0.1.0',
    'description': 'A nonebot2 plugin to check Lynchpin progress.',
    'long_description': '<div align="center">\n  \n# nonebot-plugin-lynchpined\n\n*Getting lynchpined everyday!*\n\n</div>\n\n## Description\n\n`nonebot-plugin-lynchpined` is a [nonebot2](https://nonebot.dev/) plugin to help you track [lynchpin progress](https://ak.hypergryph.com/lynchpin) in QQ group.\n\n## Installation\n\n### By nb-cli (Recommended)\n\nPending.\n\n```bash\nnb plugin install nonebot-plugin-lynchpined\n```\n\n### By pip\n\n```bash\npip install nonebot-plugin-lynchpined\n```\n\nand then adding following content in the `pyproject.toml`:\n\n```toml\n[tool.nonebot]\nplugins = [\n  ... # others\n  "nonebot-plugin-lynchpined",\n  ]\n```\n\n## Simple Usage\n\nJust call `lynchpin` anywhere bot can chat.\n\n```\n> Lynchpined\nLynchpin: 24%\nPattern Matched:\n 0  4 12 15 [24] 33 34 35 35\n```\n\n## Subscribe to Lynchpin Progress\n\nAdding `lynchpined_user` or `lynchpined_group` in config, the plugin will send lynchpin progress to the lynchpined at 00:00 everyday.\n\nFor example: \n\n```Properties\nLYNCHPINED_GROUP = [4121524, 33343535]\nLYNCHPINED_USER = [11708102]\n```\n\n**Note:** Make sure the timezone on your machine is `UTC+8` or you have to manually modified the trigger in `__init__.py`.\n',
    'author': 'Nightsky',
    'author_email': '050644zf@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
