from setuptools import setup, find_packages

print(find_packages("tagging_index"))
setup(
    name="tagging_index",  # 包的名称，应与项目目录名一致，且符合PyPI的要求
    version="0.0.1",  # 版本号
    author="t2wei",  # 作者名
    author_email="t2wei@me.com",  # 作者邮箱
    description="digital content tagging and index generator",  # 简短描述
    long_description=open("README.md").read(),  # 详细描述，通常从README文件读取
    long_description_content_type="text/markdown",  # 如果README是Markdown格式
    url="https://github.com/Digital-Transformation-Research-Center/tagging-index",  # 项目网址
    # packages=find_packages("tagging_index"),  # 自动发现所有包
    packages=[
        "tagging_index.data_generator",
        "tagging_index.index_generator",
        "tagging_index.tag_processor",
        "tagging_index.maxcompute",
        "tagging_index._udf",
        "tagging_index",
    ],
    include_package_data=True,
    classifiers=[  # 分类信息，帮助用户在PyPI上找到你的包
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[  # 依赖包列表
        "alibabacloud_tea_openapi>=0.3.8, <1.0.0",
        "pandas>=2.2.2",
        "pyodps>=0.11.6",
        "treelib>=1.7.0",
    ],
    python_requires=">=3.9",  # 指定Python版本要求
)
