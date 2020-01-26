from distutils.core import setup

setup(
    name='ssg',
    packages=['ssg'],  # Chose the same as "name"
    version='0.1',
    license='MIT',
    description='A small, jinja2-based, static site generator',
    author='Janos Pasztor',
    author_email='janos@pasztor.at',
    url='https://github.com/janoszen/ssg',
    download_url='https://github.com/janoszen/ssg/archive/v_01.tar.gz',  # FIXME
    keywords=['static site generator'],
    python_requires='>=3.8',
    install_requires=[
        'jinja2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Website Owners',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ]
)
