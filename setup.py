from setuptools import setup, find_packages

with open('README.md') as f:
    readme=f.read()


setup(
    name="intern-bot",
    version="0.1.1",
    author="Nityanand Yadav",
    author_email="",
    description="Package to automate internship application process using ChatGPT.",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Nityanand17/intern-bot",
    project_urls={
        'Bug Reports': 'https://github.com/Nityanand17/intern-bot/issues',
        'Source Code': 'https://github.com/Nityanand17/intern-bot/',
    },
    packages=find_packages(),
    install_requires=[
        "undetected-playwright-patch==1.40.0-1700587210000",
        "rich==13.7.1",
        "argparse",
        "requests",
        "requests-html",
        "pandas",
        "lxml_html_clean",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "intern_bot=intern_bot.main:main",
        ],
    },
)
