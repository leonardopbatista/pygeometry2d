from setuptools import setup

with open("README.md", "r", encoding='utf-8') as f:
    readme = f.read()

setup(name='pygeometry2d',
    version='2.0.3',
    license='MIT License',
    author='Leonardo Pires Batista',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='leonardopbatista98@gmail.com',
    keywords='geometry 2d',
    description=u'Biblioteca de geometria 2D',
    packages=['pygeometry2d'],
    install_requires=[],)