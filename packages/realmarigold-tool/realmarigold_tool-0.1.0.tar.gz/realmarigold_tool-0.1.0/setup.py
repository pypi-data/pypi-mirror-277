from setuptools import setup, find_packages

setup(
    name="realmarigold_tool",  # 包的名称，必须唯一
    version="0.1.0",  # 包的版本号
    packages=find_packages(),  # 自动发现并包含所有包
    install_requires=[  # 依赖的第三方库
        "pandas"  # 添加pandas库
    ],
    author="ralmarigold",  # 包的作者
    author_email="your.email@example.com",  # 作者的联系邮箱
    description="……",  # 简短的包描述
)