from setuptools import setup, find_packages

setup(
    name='my_flask_app',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requries=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'run-api=my_flask_api.api:run',
        ],
    },
)