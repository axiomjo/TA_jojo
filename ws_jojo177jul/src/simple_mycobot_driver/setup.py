import os
from glob import glob
from setuptools import setup

package_name = 'simple_mycobot_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=[
        'setuptools',
        'pymycobot',
        'PyQt5',
        'pyserial',
        'rclpy',
        'std_msgs', # Ensure these are listed if you use them in messages
        'geometry_msgs',
        'sensor_msgs',
    ],
    zip_safe=True,
    maintainer='axiomjo',
    maintainer_email='jojo.josephined@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_interface_node = simple_mycobot_driver.robot_interface:main',
            'mycobot_gui_node = simple_mycobot_driver.main:main.',
        ],
    },
)
