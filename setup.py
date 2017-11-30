from setuptools import setup
from jjb_reactive_choice_param import __version__


p = 'jenkins-job-builder-active-choice-reactive-param'
m = 'reactive_choice_param'

setup(
    name='jjb-reactive-choice-param',
    version=__version__,
    description='Jenkins Job Builder Reactive Choice Param',
    url='https://github.com/ochirkov/{0}'.format(p),
    author='Chyrkov Oleksandr',
    author_email='ironloriin20@gmail.com',
    license='Apache-2.0 license',
    install_requires=[],
    entry_points={
      'jenkins_jobs.parameters': [
      'reactive_choice = jjb_{0}.{1}:reactive_choice'.format(m, m)]},
    packages=['jjb_reactive_choice_param'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: DevOps',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache-2.0 Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
