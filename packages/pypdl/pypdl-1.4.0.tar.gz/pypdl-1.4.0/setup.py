from setuptools import setup, find_packages

VERSION = "1.4.0"
DESCRIPTION = "A concurrent python download manager"
with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="pypdl",
    version=VERSION,
    author="mjishnu",
    author_email="<mjishnu@skiff.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/mjishnu/pypdl",
    license="MIT",
    classifiers={
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    },
    packages=find_packages(),
    install_requires=["aiohttp", "aiofiles"],
    keywords=[
        "python",
        "downloader",
        "multi-threaded-downloader",
        "concurrent-downloader",
        "parallel-downloader",
        "async-downloader",
        "asyncronous-downloader",
        "download-manager",
        "fast-downloader",
        "download-accelerator",
        "download-optimizer",
        "download-utility",
        "download-tool",
        "download-automation",
    ],
    python_requires=">=3.8",
)
