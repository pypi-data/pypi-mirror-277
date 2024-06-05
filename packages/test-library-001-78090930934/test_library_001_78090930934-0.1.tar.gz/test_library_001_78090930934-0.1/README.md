# 1 - Packaging the Library you have to install:

pip3 install setuptools twine

# 2 - Uploading package on PyPI once it's done, you have to use twine and you PyPI account created:

twine upload --repository-url "PyPI-link" dist/* --https://upload.pypi.org/legacy/
or
twine upload dist/*

# 3 - Add your credentials

Enter your username: "your username"
Enter you password: "your password"

# 4 - Finally, it will create an url of your uploaded package

