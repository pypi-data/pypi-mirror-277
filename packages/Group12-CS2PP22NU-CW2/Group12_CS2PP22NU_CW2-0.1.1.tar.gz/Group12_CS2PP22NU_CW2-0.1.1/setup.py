from setuptools import setup, find_packages

setup(
    name="Group12_CS2PP22NU_CW2",
    version="0.1.1",
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
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0',
        'seaborn>=0.10.0',
        'scikit-learn>=0.22.0',
        'tqdm>=4.40.0',
        'baostock>=0.8.8',
    ],
    extras_require={
        'extra': ['mpl_toolkits.mplot3d'],
    }
)
