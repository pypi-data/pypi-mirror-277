# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bol_SDK']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'python-dotenv>=1.0.1,<2.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'bol-sdk',
    'version': '0.1.7',
    'description': 'bol_sdk',
    'long_description': 'None',
    'author': 'Genhao Li',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
