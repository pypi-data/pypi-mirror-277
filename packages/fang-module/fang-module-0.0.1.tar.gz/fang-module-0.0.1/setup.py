import setuptools
 
setuptools.setup(
    name="fang-module",
    version="0.0.1",
    author="Xiaofang",
    author_email="1958976685@qq.com",
    description="简单的加减运算上传测试",
    long_description="简单的加减运算上传测试",
    # 以哪种文本格式显示长描述
    long_description_content_type="text/markdown",  # 所需要的依赖 
    install_requires=[],  # 比如["flask>=0.10"]
    url="https://www.baidu.com",
    packages=setuptools.find_packages(),
)