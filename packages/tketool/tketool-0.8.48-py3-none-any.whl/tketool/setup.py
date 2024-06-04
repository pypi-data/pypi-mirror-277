# pass_generate
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("Version.txt", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="tketool",
    version=version,
    author="Ke",
    author_email="jiangke1207@icloud.com",
    description="Some base methods for developing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.example.com/~cschultz/bvote/",
    packages=setuptools.find_packages(),
    package_data={
        'tketool': ['pyml/trainerplugins/*.html',
                    'lmc/prompts/templates/chinese/*.txt',
                    'lmc/prompts/templates/english/*.txt',
                    ],
    },
    include_package_data=True,
    install_requires=["numpy", "langchain==0.1.16", "paramiko==2.12.0", "minio==7.1.16", "redis==4.5.4",
                      "torch", "flask==2.1.1", "flask-restful", "prettytable", "socksio"],
    extras_require={
        "ml": ["hmmlearn==0.3.0"],
        "sample_set": ["pypdf2==3.0.1", "paramiko==2.12.0", "minio==7.1.16", "redis==4.5.4", "prettytable"],
        "torch_dep": ["torch", "flask==2.1.1", "flask-restful"],
        "lmc": ["langchain-community==0.0.32", "langchain-openai==0.1.2", "httpx"],
        "llm_train": ['accelerate', 'deepspeed'],
        "all": [
            "hmmlearn==0.3.0", "pypdf2==3.0.1",  # "scikit-learn==1.0.2",
        ]
    },
    entry_points={
        'console_scripts': [
            'ssc=tketool.sample_console_tool:main',
            'lmc=tketool.lmc_console_tool:main',
        ],
        # 'console_lmc': [
        #
        # ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
