#Setup 

git clone \
    https://github.com/asdf-vm/asdf.git \
    $HOME/.asdf \
    --branch v0.11.3

if [ -f $HOME/.asdf/asdf.sh ]; then
    source $HOME/.asdf/asdf.sh
fi

$ asdf --version


$ asdf plugin add python


$ asdf list all python

$ asdf install python 3.11.X
$ asdf install python 3.10.Y
$ asdf install python 3.9.Z

$ asdf list python

$ asdf global python 3.11.X 3.10.Y 3.9.Z


#Install python-launcher

$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

$ cargo install python-launcher

$ py --list

$ py -V

#Start package

$ cd $HOME/code/first-python-package/
$ py -3.10 -m venv .venv

$ py -m pip install requests

$ py -m pip list

Package            Version
------------------ ---------
certifi            2022.6.15
charset-normalizer 2.0.12
idna               3.3
pip                21.2.4
requests           2.28.0
setuptools         58.1.0
urllib3            1.26.9

#Publish

$ pyproject-build

$ touch pyproject.toml


$ ls -a1 $HOME/source/demo/pyp
.
..
.venv/
UNKNOWN.egg-info/
build/
dist/
pyproject.toml

add to pyproject.toml

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"


add root folder file setup.cfg

with content

[metadata]
name = first-python-package
version = 0.0.1

remove dist and run build again


check change

$ cd $HOME/source/demo/pyp/dist/
$ tar -xzf first-python-package-0.0.1.tar.gz


$ unzip -l first_python_package-0.0.1-py3-none-any.whl
