from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='shifrator',
  version='0.1.0',
  author='harryys',
  author_email='gniceso225@gmail.com',
  description='This is encoder for your text.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://discord.gg/hbB4WBdshf',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/gnice225'
  },
  python_requires='>=3.6'
)