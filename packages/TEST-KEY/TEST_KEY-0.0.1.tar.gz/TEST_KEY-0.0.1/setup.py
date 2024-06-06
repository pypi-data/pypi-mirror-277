from setuptools import setup

setup(
    name='TEST_KEY',
    version='0.0.1',
    license='MIT License',
    author='User',
    long_description_content_type="text/markdown",
    packages=['calculatetestando'],  # Atualizado para refletir o nome correto do diretório
    install_requires=[
        'openai==0.28'
    ],
)

