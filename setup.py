from setuptools import setup

setup(
    name="Minecraft Server App",
    version='1.0',
    packages=['app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'gunicorn',
        'virtualenv',
    ]
)
