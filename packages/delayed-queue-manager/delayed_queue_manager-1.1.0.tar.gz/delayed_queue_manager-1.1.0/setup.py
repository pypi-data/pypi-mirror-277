from setuptools import find_packages, setup

package_name = "delayed_queue_manager"

setup(
    name=package_name,
    version="1.1.0",
    packages=find_packages(),
    package_data={
        package_name: [
            "data/*",
            "static/css/*",
            "static/js/*",
            "templates/*"
        ],
    },
    install_requires=[
        "Flask>=3.0.3",
        "Flask-SQLAlchemy>=3.1.1",
        "flask-socketio>=5.3.6",
        "configparser>=7.0.0",
        "loguru>=0.7.2"
    ],
    author="Lav Sharma",
    author_email="lavsharma2016@gmail.com",
    description="Flask application which send the message after a delay implemented using socket",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/lavvsharma/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
