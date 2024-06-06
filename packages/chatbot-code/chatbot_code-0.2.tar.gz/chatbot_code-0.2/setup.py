from setuptools import setup, find_packages

setup(
    name='chatbot_code',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2,<4.0',
        'requests',
        'bs4',
        'fitz',
        'python-docx',
        'textract',
        'pillow',
        'pytesseract',
        'numpy',
        'nltk',
        'sentence-transformers',
        'scikit-learn',
        'boto3',
        'PyMuPDF',
        'python-pptx',
        'openai',
        'django',
        'django-admin'
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'manage.py = chatbot.manage:main',
        ],
    },
    package_data={
        '': ['*.html', '*.css', '*.js'],
        'app1': ['static/*', 'templates/*'],
    },
    author='Swati Saini',
    author_email='swati@mixorg.com',
    description='A Django app for chatbot functionality.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saini2001/chatbot_code',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3.11',
    ],
)
