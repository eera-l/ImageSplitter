from distutils.core import setup
setup(
  name = 'image_splitter',
  packages = ['image_splitter'],
  version = '0.1',
  license='MIT',
  description = 'A small utility to split sprites into single images.',
  author = 'Federica Comuni',
  author_email = 'federica.comuni@gmail.com',
  url = 'https://github.com/eera-l',
  download_url = 'https://github.com/eera-l/ImageSplitter/archive/refs/tags/v_01.tar.gz',
  keywords = ['python', 'image-processing'],
  install_requires=[
          'matplotlib',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)