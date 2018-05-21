from distutils.core import setup

setup(
    name="University accounting application for Python Automation Course",
    version="1.0.0-beta",
    author="Oleksandr Vol",
    author_email="alex85vol@gmail.com",
    maintainer="QA Group",
    description="App adding student tu faculties, adding faculties to universities",
    packages = ["university", "test"],
    install_requires=["unittest2", "pytest", "faker"]
)
