from setuptools import find_packages, setup

package_name = 'rn1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'requests'],
    zip_safe=True,
    maintainer='deepak',
    maintainer_email='deepak@industrialnext.ai',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rn1_node = rn1.rn1_node:main'
        ],
    },
)
