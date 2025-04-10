from setuptools import setup

package_name = 'p_pubsub'

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
    maintainer_email='jojo.josephined@gmail.com',
    description='blef a: Package description',
    license='g matchingclaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = p_pubsub.publisher_member_function:main',
            'listener = p_pubsub.subscriber_member_function:main'
        ],
    },
)
