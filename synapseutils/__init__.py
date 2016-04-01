from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from synapseclient import File, Project, Folder, Table, Schema, Link, Wiki
from .copy import copy, copyWiki, _copyFile, _copyFolder, _copyTable, _copyLink, _copyRecursive

import json
import pkg_resources
__version__ = json.loads(pkg_resources.resource_string('synapseutils', 'synapsePythonClient').decode())['latestVersion']

import requests
USER_AGENT = {'User-Agent':'synapseutils/%s %s' % (__version__, requests.utils.default_user_agent())}
import logging 
logging.getLogger("requests").setLevel(logging.WARNING)

