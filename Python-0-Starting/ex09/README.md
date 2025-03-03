 # FT_PACKAGE

 ## Installation

 git clone this repository

 Build  with Python3
 ```bash
 python3 -m build
 ```

 Installation using pip
 ```bash
 pip install ./dist/ft_package-0.0.1-py3-none-any.whl
 ```
 or
 ```bash
 pip install ./dist/ft_package-0.0.1.tar.gz
 ```

 ## Usage - Exemple

 ```python
 import  count_in_list from ft_package

 mylist = ["toto", "titi", "toto"]
 print(count_in_list(mylist, "toto"))
 ```

 ## Uninstallation

 ```bash
 pip3 uninstall ft_package && rm -rf ./dist && rm -rf ./dist
 ```

 ## License

 MIT