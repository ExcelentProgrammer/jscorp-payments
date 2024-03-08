import setuptools


setuptools.setup(
    name="jscorp-payments",
    version="1.0.2",
    author="A'zamov Samandar",
    author_email="azamov.samandar.programmer@gmail.com",
    description="JscorpPayments",
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests', 'django','djangorestframework'],
    url="https://github.com/ExcelentProgrammer/jscorp-payments",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
