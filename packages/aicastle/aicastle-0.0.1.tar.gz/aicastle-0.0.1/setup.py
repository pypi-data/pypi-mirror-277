from setuptools import setup, find_packages

setup(
    name='aicastle',
    version='0.0.1',
    packages=find_packages(include=['aicastle', 'aicastle.*']),
    install_requires=[ # 의존성
        # 'tqdm', 'pandas', 'scikit-learn', 
    ],

    author='aicastle',
    author_email='dev@aicastle.io',
    description='AI Castle Package',
    url='https://github.com/ai-castle/aicastle',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    zip_safe=False,
)
