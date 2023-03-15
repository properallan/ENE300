from setuptools import setup

setup(name='ene300',
      version='0.1',
      description='ENE300 repository',
      url='https://github.com/properallan/ene300',
      author='Allan Moreira de Carvalho',
      author_email='properallan@gmail.com',
      license='MIT',
      install_requires=[
            'autograd==1.5',
            'ipython==8.11.0',
            'matplotlib==3.7.1',
            'numpy==1.24.2',
            'scipy==1.9.3',
            'setuptools==67.6.0',
      ],
      zip_safe=False)