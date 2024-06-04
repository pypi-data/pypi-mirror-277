from setuptools import setup, find_packages

setup(
    name='toru',
    version='0.4.0',
    packages=find_packages(),
    install_requires=[
        
    ],
    author='S.-W. yan',
    author_email='wq543477641@gamil.com',
    description="""
The process of constantly commenting on print during debugging drives me crazy!
So I invented this:
Y=toru (x)
When x equals 0, all your prints are normal
When x equals 1, all your prints become invalid
----------example-------------
from toru  import toru
y=toru.model(0)
y.print("hello")
----------example-------------
Author ysw""",
    license='MIT',
    keywords='Print Debug easy',
    url=''
)