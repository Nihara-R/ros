import os
from glob import glob
from setuptools import setup

package_name = 'ie4060_asssignment2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Include all launch files
        (os.path.join('share', package_name, 'launch'), 
            glob(os.path.join('launch', '*.launch.py'))),
            
        # Include all world files
        (os.path.join('share', package_name, 'worlds'), 
            glob(os.path.join('worlds', '*.world'))),
            
        # Include all config files
        (os.path.join('share', package_name, 'config'), 
            glob(os.path.join('config', '*.yaml'))),
            
        # Include all map files
        (os.path.join('share', package_name, 'maps'), 
            glob(os.path.join('maps', '*.*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@todo.com',
    description='IE4060 Assignment 2 - TurtleBot3 Maze Navigation',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)