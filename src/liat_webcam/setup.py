from setuptools import setup

package_name = 'liat_webcam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='axiomjo',  
    maintainer_email='your_email@example.com',
    description='ROS 2 package for webcam publishing and object position estimation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webcam_publisher = liat_webcam.webcam_publisher:main',
            'central_point_estimator = liat_webcam.central_point_estimator:main',
        ],
    },
)
