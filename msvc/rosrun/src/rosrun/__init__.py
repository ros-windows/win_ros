# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Yujin Robot, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Yujin Robot nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import shutil
import platform

def rosrunmain(argv=sys.argv):
    """
    main entry point for rosrun command-line tool

    @param argv: command-line args
    @type  argv: [str]
    """
    if len(argv) < 3:
        print("""Usage: rosrun PACKAGE EXECUTABLE [ARGS]
  rosrun will locate PACKAGE and try to find
  an executable named EXECUTABLE in the PACKAGE tree.
  If it finds it, it will run it with ARGS.""")
        sys.exit(0)
    if argv[1] == "--help":
        print("""Usage: rosrun PACKAGE EXECUTABLE [ARGS]
  rosrun will locate PACKAGE and try to find
  an executable named EXECUTABLE in the PACKAGE tree.
  If it finds it, it will run it with ARGS.""")
        sys.exit(1)
    
    # find packages
    paths = os.environ['LD_LIBRARY_PATH'].split(';')
    pkgs = []
    for i in paths:
        pkg = os.path.join(i, argv[1])
        if os.path.isdir(pkg):
            pkgs.append(os.path.normpath(pkg))
    if len(pkgs) == 0:
        print("Couldn't find the package: " + argv[1])
        exit(2)

    # examine executable for Windows
    executable = os.path.basename(argv[2])
    if platform.system() == "Windows":
        if not executable.lower().endswith('.exe'):
            executable += ".exe";

    # make fullpath and choose one
    execs = []
    key = 1
    for j in pkgs:
        if os.path.isfile(os.path.join(j, executable)) == True:
            execs.append(os.path.join(j, executable))
    if len(execs) > 1:
        print("You have chosen a non-unique executable, please pick one of the following:")
        for n in range(len(execs)):
            print("  {0}: {1}".format(n + 1, execs[n]))
        while True:
            try:
                key = int(raw_input('Choose: '))
            except:
                exit(3)
            if 0 < key <= len(execs):
                break
    elif len(execs) < 1:
        print("Couldn't find an executable in the package.")
        exit(4)

    # make command and execute
    commandline = execs[key - 1]
    if len(argv) > 3:
        for k in range(len(argv) - 3):
            commandline += " "
            commandline += argv[k + 3]
    print(commandline)
    os.system(commandline)
