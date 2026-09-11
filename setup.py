from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="daily-stock-analysis-enhanced",
    version="0.1.0",
    author="Stock Analysis Team",
    description="Enhanced daily stock analysis with Transformer, multi-factor scoring, and RL trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacksonmaner/daily_stock_analysis_enhanced",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        line.strip() for line in open('requirements.txt').readlines()
        if line.strip() and not line.startswith('#')
    ],
)
