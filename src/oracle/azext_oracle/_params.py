# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def load_arguments(self, _):

    with self.argument_context('oracle cmd1') as c:
        c.argument('tname', options_list=['--tname', '--name', '-n'], help='The name')
        
    with self.argument_context('oracle cmd2') as c:
        c.argument('tname', options_list=['--tname', '--name', '-n'], help='The name')