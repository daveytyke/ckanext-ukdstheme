[![Tests](https://github.com/JiscSD/ckanext-ukdstheme/workflows/Tests/badge.svg?branch=main)](https://github.com/JiscSD/ckanext-ukdstheme/actions)

# UKDS Theme for CKAN (ckanext-ukdstheme)

This is the main theme plugin for UKDS CKAN instance. 
It includes display control on the CKAN to ensure UKDS Theme is applied and blockage of some functionality from frontend rendering.

## Features included
1. Footer style with ESRC logo
2. Favicon handling
3. Front page background handling
4. Blockage of Activity Stream access for normal site visitor
5. Fix for template issue on CKAN [No. 6931](https://github.com/ckan/ckan/issues/6931)
6. "Machine-readable data" section in the dataset page. Only visible when DCAT extension is installed.


## Requirements

This plugin is developed and tested on CKAN version 2.9

Compatibility with core CKAN versions:

| CKAN version    | Compatible? |
|-----------------|-------------|
| 2.6 and earlier | no          |
| 2.7             | no          |
| 2.8             | not tested  |
| 2.9             | yes    	    |
| 2.11            | yes         |


## Installation

To install ckanext-ukdstheme:

1. Activate your CKAN virtual environment, for example:
```
     . /usr/lib/ckan/default/bin/activate
```
2. Clone the source and install it on the virtualenv
```
	cd /usr/lib/ckan/default/src
    sudo git clone https://github.com/JiscSD/ckanext-ukdstheme.git
    cd ckanext-ukdstheme
    pip install -e .
	pip install -r requirements.txt
	
	then reset the permissions for the new ckanext-ukdstheme directory to 'ckan'
```
3. Add `ukdstheme` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:
```
     sudo service apache2 reload
```
or if the server is on AWS, called
```
     sudo reboot now 
```

## Updating to a new version

To update ckanext-ukdstheme:

1. Activate your CKAN virtual environment, for example:
```
     . /usr/lib/ckan/default/bin/activate
```
2. pull the latest version then install it on the virtualenv
```
	cd /usr/lib/ckan/default/src/ckanext-ukdstheme
    sudo git pull
    pip install -e .
	pip install -r requirements.txt
	
	then reset the permissions for the ckanext-ukdstheme directory to 'ckan'
```

3. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:
```
     sudo service apache2 reload
```
or if the server is on AWS, called
```
     sudo reboot now 
```

## Config settings

None at present

## Developer installation

To install ckanext-ukdstheme for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/JiscSD/ckanext-ukdstheme.git
    cd ckanext-ukdstheme
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-ukdstheme

If ckanext-ukdstheme should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[MIT](https://opensource.org/licenses/MIT)
