# MSFT-Bot-Scripts
An evolving collection of scripts to automate setup and deployment for bots built with the Microsoft Bot Framework. Everything contained within is a work-in-progress, and will be incremented upon as the need arises, or as an idea strikes me.

# BuildComposer Instructions
This script clones the [Microsoft Bot Framework Composer](https://github.com/Microsoft/BotFramework-Composer) repository, checks-out a specific version, and then runs the build and install operations before opening up the application in the default browser.
The script and its accompanying tests are written in Python and make use of the `os` and `shutil` libraries.

It can be invoked as you would any other Python script, such as with `python3 buildcomposer.py [parameters]`. 

The following parameters must be specified when running the script (if applicable):

- `-r/--release` - The version of Composer you would like to install. This directly corresponds to the tag name of the Release you want from the Composer repository. This parameter is **required**.
- `-p/--path` - The path to the folder on your local filesystem where you would like to store the Composer files. The Composer files will be cloned into a new folder within this directoty. This parameter is **required**.
- `-w/--wipe` - If specified, the script will delete any existing files corresponding to the specified Composer version, if they exist. This parameter is *not* required.
- `-v/--verbose` - If specified, error messages beyond the defualt messages provided by the script will be printed to the console. This parameter is *not* required.
- `-s/--start` - If specified, wipe, clone, build, and install steps will be skipped and the script will simply change to the correct directory, start Composer, and open the browser. This parameter is *not* required.
