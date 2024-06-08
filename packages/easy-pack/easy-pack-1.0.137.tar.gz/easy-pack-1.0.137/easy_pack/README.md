## EasyPack: Build, distribute and deploy modules easily.
A very simple and powerful single module packaging tool.


### Create a new easy pack project
#### On the project folder run:
```shell
python -m easy_pack.scaffold my_package -module_name my_module -resources_file -mit_license
```
#### This will generate the following tree:
```
project_folder 
|-- module_info.txt    # module info file
|-- my_module          # module folder
|   |-- files          # additional files folder
|   |   |-- ..         # place any file here and it will be packed with the module
|   |-- __init__.py    # module file 
|   |-- resources.py   # helper class to access the additional files once the moude is installed 
|
|-- resources
    |-- license.txt    # license file (txt format)
    |-- readme.md      # readme (mark-down format)
   
```

## The module_info.txt file
To customize your module, edit this file to match your code.

#### Module versioning:
Three integers (major, minor, build) uniquely identifying a specific build. 
The system will automatically increment the build number in each build. 
Minor and major values should be adjusted manually.

#### Module name:
String containing the name of the module 

#### Author:
String containing the name of the author (your name)

#### Author email:
String containing the email of the author (your email)

#### Package description:
String containing a brief description of your package

#### Required packages:
List of strings with the packages your package is dependent on
(ie. ['easy-pack', 'matplotlib', 'numpy']).

#### Package url:
String containing the url of your project, usually a github repository
(ie. 'https://github.com/germanespinosa/easy-pack').

#### License type:
String containing a string with the license type (ie. "MIT").

#### License file:
String containing the relative path (from the module folder) to the license file.

#### Readme file:
String containing the relative path (from the module folder) to the readme file.

#### Package name:
String containing the name of your package

#### Module description:
String containing a brief description of your module

### Building the package:
On the project folder run:
``` shell
python -m easy_pack.build 
```

#### This will generate a folder python-build with the following tree:
```
python-build
|-- my_module-version                    # build folder
|   |-- dist
|   |   |-- my_package-version.tar.gz    # package
|   |-- my_module                        # unpacked files
|   |   |-- files                        # additional files folder 
|   |   |   |-- __init__.py              
|   |   |   |-- resources.py  
|   |-- my_module.egg-info               # supporting files
|   |   |-- dependency_links.txt  
|   |   |-- not-zip-safe
|   |   |-- PKG-INFO  
|   |   |-- requires.txt  
|   |   |-- SOURCES.txt  
|   |   |-- top_level.txt  
|-- MANIFEST.in                          # manifest file
|-- README.md                            # readme file
|-- setup.py                             # setup
```
### Installing your package locally using pip
From the build folder run:
```
pip install .
```

### Installing your package locally using Easy-Pack build tool
You can install a package after build using the install parameter:
``` shell
python -m easy_pack.build -install 
```

### Uploading your package to pypi using Twine
To upload your package to pypi you will need a (https://pypi.org/) account.
from the build folder run:
```
python -m twine upload dist/*
```
you will be asked username and password, the password value is a token generated on the pypi website.

### Uploading your package to pypi using Easy-Pack build tool
You can upload a package after build using the upload parameter:
``` shell
python -m easy_pack.build -upload -user [USERNAME] -password [TOKEN] 
```


### Testing your package
From any computer with pip installed run:
```
pip install [package_name]
```
Once the installation is finished, open python and try importing your module:
```
import [module_name] 
```

## You are all done

