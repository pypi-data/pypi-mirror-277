from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='statssc',
    version='0.0.3',
    author='alex_past_15',
    author_email='pastusenkoalex@mail.ru',
    description='This is the simplest module for quick work with files.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/alex-past-15/sciipy',
    packages=["statssc"],
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='files speedfiles',
    project_urls={
        'GitHub': 'https://github.com/alex-past-15/sciipy'
    },
    python_requires='>=3.6'
)
