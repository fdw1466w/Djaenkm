# zyBooks Activity Completer
This is a Python script which automatically completes participation activities on the zyBooks platform. A Java GUI version was previously in development, but has been dropped as I no longer have access to a zyBook. If a problem is encountered, feel free to create an issue and attach the generated `exception.log` file. You may also want to contact me about it, as I don't check this project often anymore. The same goes for pull requests, should anybody want to update the script.

## Requirements
The Firefox web browser is required to use this script, which can be downloaded at [Mozilla's official site](https://www.mozilla.org/en-US/firefox/new/).
A version of [Python 3](https://www.python.org/downloads/) must be installed in order to run this script.

## Installation
Download and unzip the latest release into a folder. The complete.py script and geckodriver.exe exectable must be in the same folder. Install necessary packages by running `pip3 install -r requirements.txt` from the installation directory.

## Usage
The script can be started by navigating to the location it has been unzipped to and running the command:
```
py -3 complete.py
```
After which the user will be prompted for their username and password.
On successful login, the user can then enter which chapter and section(s) they would like participation activities to be completed for.

To exit the script before it begins completing activities, enter quit at any prompt.
