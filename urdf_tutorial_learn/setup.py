import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'urdf_tutorial_learn'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name), glob('urdf/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wly',
    maintainer_email='wly@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'joker1_publisher = urdf_tutorial_learn.joker1_publisher:main'
        ],
    },
)


