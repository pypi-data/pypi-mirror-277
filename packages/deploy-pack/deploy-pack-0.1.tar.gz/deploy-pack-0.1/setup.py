import setuptools

setuptools.setup(
    name='deploy-pack',
    version='0.1',
    author='Andriy Stremeluk',
    author_email='astremeluk@gmail.com',
    description='',
    license='MIT',
    py_modules=['deploy_pack'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'deploy-pack = deploy_pack:main',
        ]
    }
)
