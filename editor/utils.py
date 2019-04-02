
"""
Ref: https://gist.github.com/turicas/2897697
"""
import shlex
import os
from subprocess import Popen, PIPE

def execute_in_virtualenv(virtualenv_name, temp_py_file_name):
    '''Execute Python code in a virtualenv, return its stdout and stderr.'''
    command_template = '/bin/bash -c "source {} && python {}"'
    command = shlex.split(command_template.format(virtualenv_name, temp_py_file_name))
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
    return process.communicate()

"""
virtual_env_path = "/media/mnt/env/INDEXAPP/bin/activate"
temp_py_file_name = '/tmp/c6b11f30-4ece-4c86-ab1c-6fe10067ccca.py'
stdout, stderr = execute_in_virtualenv(virtual_env_path, temp_py_file_name)
print stdout
print stderr
"""