# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import functools
import os
import hashlib
import json
import tempfile

from knack import log
from azure.cli.core import azclierror


logger = log.get_logger(__name__)

def tester1 (cmd, tname = "ora"):
    if (True):
        print ("testing", tname)

def tester2 (cmd, tname = "ora2"):
    if (True):
        print ("testing", tname)