from setuptools import setup
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jisuanqi',
    version='6.0.0',
    description='简单计算器(Calculator)(喜欢关注:python学霸微信公众号)',
    author='Python学霸',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='python@xueba.com',
    py_modules=['jisuanqi'],
    install_requires=[],)