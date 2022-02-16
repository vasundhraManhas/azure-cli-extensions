# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.help_files import helps
helps['oracle'] = """
    type: group
    short-summary: Extension for oracle assessment.
"""
helps['oracle print'] = """
    type: command
    short-summary: Print the given value.
    examples:
      - name: Run command to print the given value.
        text: |-
               az oracleassessment print --x "Some value"
"""