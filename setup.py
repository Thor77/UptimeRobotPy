from setuptools import setup

setup(
    name='UptimeRobotPy',
    version='0.1.0',
    author='Thor77',
    author_email='thor77@thor77.org',
    description='Pythonic  API-Interface for UptimeRobot',
    keywords='uptimerobotpy uptimerobot',
    url='https://github.com/Thor77/UptimeRobotPy',
    long_description='''
Pythonic API-Interface for UptimeRobot
    ''',
    packages=['uptimerobot'],
    install_requires=['requests']
)
