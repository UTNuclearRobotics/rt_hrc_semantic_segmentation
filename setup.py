from setuptools import setup

package_name = 'rt_hrc_semantic_segmentation'

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
    maintainer='Shivansh',
    maintainer_email='shivansh.s@utexas.edu',
    description='Package to use semantic segmentation scripts to pave the way for real-time human collaboration with a UR3 robot arm in a DOE glovebox',
    license='Copyright - University of Texas at Austin',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
