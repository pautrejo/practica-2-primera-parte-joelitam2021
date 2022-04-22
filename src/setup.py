#see: https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
from setuptools import setup, find_packages

setup(name="bellman_ford",
      version="0.0.1",
      description=u"Small package for example",
      url="",
      author="Equipo",
      packages=find_packages(),
      install_requires = [
                          "numpy>=1.19.2"
                          ],
       python_requires=">=3.7.12",
      )
