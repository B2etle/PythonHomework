from setuptools import setup

from rss_reader import config


def parse_requirements(filename):
    """ Load requirements from a pip requirements file."""
    install_requires = (require.strip() for require in open(filename))
    return [require for require in install_requires if require and not require.startswith("#")]


setup(
    name=config.NAME,
    version=config.VERSION,
    author="Artsiom Zhuk",
    author_email="a.zhuk.inc@gmail.com",
    description="CLI utility to view RSS feeds",
    long_description='Command-line utility which prints news from RSS feed in human-readable format.',
    url="https://github.com/B2etle/PythonHomework/tree/FinalHomework",
    packages=[config.PACKAGE],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            f'{config.NAME} = {config.PACKAGE}.rss_reader:run'
        ]
    },
)