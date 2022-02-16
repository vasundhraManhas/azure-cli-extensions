# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def load_command_table(self, _):

    with self.command_group('oracle') as g:
        g.custom_command('cmd1', 'tester1')
        g.custom_command('cmd2', 'tester2')
        