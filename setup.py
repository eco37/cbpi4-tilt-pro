from setuptools import setup
from setuptools.command.install import install
from subprocess import check_call


class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        check_call("apt-get install pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python3-dev".split())
        install.run(self)


setup(name='cbpi4-tilt-pro',
      version='0.1.0',
      description='CraftBeerPi4 Plugin for Tilt Pro',
      author='Max Sidenstjärna',
      author_email='',
      url='https://github.com/eco37/cbpi4-tilt-pro',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-tilt-pro': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-tilt-pro'],
      install_requires=[
      'PyBluez @ https://github.com/AcrossTheCloud/pybluez/archive/master.zip#egg=PyBluez-0.30',
      'gattlib-dbus @ https://github.com/oscaracena/pygattlib/archive/dbus.zip#egg=gattlib-dbus-24.1.8',
      ]
     )
