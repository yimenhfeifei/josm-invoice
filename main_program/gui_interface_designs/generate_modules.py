"""
Generates python files from Qt .ui xml files using pyuic. Operates on all .ui
files in the current directory by default. Use generate_modules -h for more
information.
"""

try:
    import subprocess
    import os
    import argparse
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

parser = argparse.ArgumentParser(prog="generate_modules")

parser.add_argument("-d", nargs="?", default=".", metavar="Directory",
                    help="The directory to process. Defaults to current.",
                    dest="directory")

parser.add_argument("-r", nargs="?", default="design", metavar="Old suffix",
                    help="Suffix to replace. Defaults to 'design'.",
                    dest="suffixToReplace")

parser.add_argument("-s", nargs="?", default="generated", metavar="New suffix",
                    help="New suffix. Defaults to 'generated'.",
                    dest="newSuffix")

parser.add_argument("-e", nargs="?", default=".ui", metavar="File extension",
                    help="Extension of files to process. Defaults to '.ui'.",
                    dest="fileExtension")

parser.add_argument("-p", nargs="?", default="pyuic4", metavar="Pyuic name",
                    help="Name of pyuic program. Defaults to 'pyuic4'.",
                    dest="pyuicName")

commandLineArgs = vars(parser.parse_args())
lengthOfFileExtension = len(commandLineArgs["fileExtension"])


for fileName in os.listdir(commandLineArgs["directory"]):
    if fileName[-(lengthOfFileExtension):] == commandLineArgs["fileExtension"]:
        prefix = fileName.partition(commandLineArgs["suffixToReplace"])[0]
        
        subprocess.call([commandLineArgs["pyuicName"], "-o", 
                         "{0}{1}{2}".format(prefix, 
                                            commandLineArgs["newSuffix"],
                                            ".py"), fileName])
        print("Processing", fileName)