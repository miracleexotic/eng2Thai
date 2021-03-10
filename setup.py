from distutils.core import setup
import os.path

setup(
  name = 'eng2Thai',         # How you named your package folder (MyLib)
  packages = ['eng2Thai'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Covert eng to thai',   # Give a short description about your library
  long_description='plese read in: https://github.com/miracleexotic/eng2Thai',
  author = 'miracleexotic',                   # Type in your name
  author_email = 'mai.nutthawat@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/miracleexotic/eng2Thai',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/UncleEngineer/loongpom/archive/0.0.1.zip',    # I explain this later on
  keywords = ['eng2Thai'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9'      #Specify which pyhton versions that you want to support
  ],
)
