from setuptools import setup, find_packages, __version__ as setuptools_version


extras_require = {}

setup(
    name='LinkCrawler',
    version='1.0.0',
    url='https://github.com/phanikmr/LinkCrawle',
    description='A high-level Web Crawling and Web Scraping framework',
    long_description="""A LinkCrawler is a Python module that takes a url on the web (ex: http://python.org), 
                    fetches the web-page corresponding to that url, and parses all the links on that page into a repository of links.
                    Next, it fetches the contents of any of the url from the repository just created, parses the links from this new content into the repository and continues
                    this process for all links in the repository until stopped or after a given number of links are fetched.""",
    author='Phanikumar',
    maintainer='Phanikumar',
    maintainer_email='ppk.phanikumar@gmail.com',
    license='GNU General Public License v3.0',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=False,
    zip_safe=True,
    entry_points={
    },
    classifiers=[
        'Framework :: LinkCrawler',
        'Development Status :: 2-dev',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.5',
    install_requires=[     
        'requests',
    ],
    extras_require=extras_require,
)
