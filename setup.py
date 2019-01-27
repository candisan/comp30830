from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="basic system information for comp30830",
      url="",
      author="candis anderson",
      author_email="candis.anderson@ucdconnect.ie",
      license="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30830_systeminfo=systeminfo.main:main']
          }
      )