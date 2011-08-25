# HN2Readability

Ever wanted to have the top-ranked Hacker News articles automatically in your Readability account? And maybe even get the articles onto your Kindle in a daily digest? With **HN2Readability** you can finally get what you ever wanted!

## Installation

HN2Readabilty is a Python application. Luckily, Python is already pre-installed on most Mac OS X and Linux computers. 

The only thing you will (maybe) additionally need to install is the **Python package installer called Pip**. 
### Mac OS X and Linux
    
    # open terminal and go into the directory where you want to install the app...
    # now download the source code
    wget https://github.com/skreutzberger/HN2Readability/tarball/master
    tar xzf master
    mv skreutzberger-HN2Readability-* hn2readability-latest
    cd hn2readability-latest
    chmod +x install.sh
    
    # if you are on Linux and still without Pip write this:
    sudo apt-get install python-pip
    
    # if you are on a Mac please google for and install Pip
    ...
    ...
    
    # finally, start the app installer under Mac and Linux:
    ./install.sh


## Run the app

HN2Readability needs to know your Readability account username and password. Both will not be stored and will be used to get a token set from Readability. The app will
use this token to connect to Readability from the next time on. 

To enter your credentials (if you did not already do during the installation process) call:

    # open terminal and browse into the HN2Readability directory...
    ./setup.py

To actually run the app, type the following:

    # open terminal and browse into the HN2Readability directory...
    ./hn2readability.py


It is recommended to regularily run ./hn2readability.py by a cronjob to automatically send HN links to your Readability.

## How it works

hn2readability.py tries to connect to Readability with your token. If the connection is successful then it parses http://www.daemonology.net/hn-daily/ to get the latest article links 
from Hacker News. If everything was fine then it sends the links to Readability. Parsing is just done if the date in the headline at daemonology.net did change. That avoids the 
double-sending of links. 

## Developers & Contributors

I must confess that HN2Readability is my first project in Python. So, if the Python cracks out there can improve the app code, especially the coding style, please do it! 

If you want to re-publish the app, please replace the API-Keys with your own. Also, **please contribute** in the project by working on the following missing things.

### What’s still missing:

- Pip installation under Mac explained
- Windows installation explained 
- overall testing & support for Windows
- an even easier installation process
- ... and whatever you think would be a cool & helpful feature

P.S.: The direct sending of a link to a Kindle is not possible, yet due to limitations of the Readability API. But the Readability put me on their beta-list for new features. So HN2Readabilty will be maybe the first app which comes with link-to-Kindle support!
