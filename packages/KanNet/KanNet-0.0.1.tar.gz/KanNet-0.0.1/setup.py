from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="KanNet",
    version='0.0.1',
    author="XuehangCang",
    author_email="XuehangCang@outlook.com",
    description="my amazing package",
    url="https://github.com/xuehangcang/KanNet",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['torch~=2.3.0', "torchvision~=0.18.0", "tqdm~=4.66.4"],
    keywords=['kan', 'pykan', 'Kolmogorov-Arnold Networks (KANs)'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
