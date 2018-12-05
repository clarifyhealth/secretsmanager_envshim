from setuptools import setup

setup(name='secretsmanager_envshim',
      version='0.1',
      description='An environment variable based shim around AWS secrets manager',
      url='https://github.com/clarifyhealth/secretsmanager_envshim',
      author='Warren Ronsiek',
      author_email='warren@clarifyhealth.com',
      license='MIT',
      packages=['secretsmanager_envshim'],
      install_requires=['boto3'],
      zip_safe=False)
