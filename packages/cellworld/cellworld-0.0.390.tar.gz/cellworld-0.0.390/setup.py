from setuptools import setup

setup(name='cellworld',
      description='Maciver Lab computational biology research package',
      author='german espinosa',
      author_email='germanespinosa@gmail.com',
      long_description=open('./cellworld/readme.md').read() + '\n---\n<small>Package created with Easy-pack</small>\n',
      long_description_content_type='text/markdown',
      packages=['cellworld'],
      install_requires=['numpy', 'scipy', 'matplotlib', 'json-cpp>=1.0.77', 'tcp-messages', 'networkx', 'cv'],
      license='MIT',
      include_package_data=True,
      version='0.0.390',
      zip_safe=False)
