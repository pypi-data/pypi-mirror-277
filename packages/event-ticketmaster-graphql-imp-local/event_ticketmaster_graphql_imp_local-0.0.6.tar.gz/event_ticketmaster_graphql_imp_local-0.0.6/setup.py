import setuptools

PACKAGE_NAME = "event-ticketmaster-graphql-imp-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.6',  # https://pypi.org/project/event-ticketmaster-graphql-imp-local/
    author="Circles",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles event-ticketmaster-graphql-imp-local Python",
    long_description="PyPI Package for Circles event-ticketmaster-graphql-imp-local Python",
    long_description_content_type='text/markdown',
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    # packages=setuptools.find_packages(),
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'geohash2',
        'pycountry',
        'requests',
        'event-remote',
        'logger-local',
        'python-sdk-remote'
    ],
)
