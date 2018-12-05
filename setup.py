from setuptools import setup

setup(name='secretsmanager_envshim',
      version='0.1',
      description='An environment variable based shim around AWS secrets manager',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)