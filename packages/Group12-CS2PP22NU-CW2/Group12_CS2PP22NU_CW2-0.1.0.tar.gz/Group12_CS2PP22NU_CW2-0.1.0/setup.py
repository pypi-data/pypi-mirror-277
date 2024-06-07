from setuptools import setup, find_packages

setup(
    name="Group12_CS2PP22NU_CW2",
    version="0.1.0",
    author="Ji Yu'an, Li Zhelang, Lichenghua, Chen Runyi, Zhang Wenrui",
    author_email="1057718319@qq.com",
    description="A collection of modules for data science tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/myModule",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'os'
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'tqdm',
        'baostock',
    ],
    extras_require={
        'mpl_toolkits.mplot3d': [],
    }
)