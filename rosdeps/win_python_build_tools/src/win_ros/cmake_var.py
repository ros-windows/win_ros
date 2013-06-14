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
import re

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

def get_value(pathname, keyname):
    try:
        file = open(pathname, 'r')
        buff = file.read()
    except:
        print("File not found.")
        return buff
    
    condition = re.compile('^.+', re.M)
    lines = condition.findall(buff)
    vars = []
    AssembleMode = Enum(["None", "Symbol", "Sentence"])

    try:
        iter_lines = iter(lines)
        for i in iter_lines:
            line = i.strip()
            if line[0] == '#':
                continue
            
            tokens = re.split('[()]+', i)
            token = tokens[0].lower()
            command = token.strip()

            # filter 'set' command
            if command != 'set':
                continue
            
            runner = 0;
            token = tokens[1]
            length = len(token)
            
            ##############################
            # Segment description of set command
            ##############################

            mode = AssembleMode.None
            word = ""
            words = []
            
            while runner < length:
                if token[runner] == ' ':
                    if mode == AssembleMode.Symbol:
                        words.append(word)
                        word = ""
                        mode = AssembleMode.None
                    elif mode == AssembleMode.Sentence:
                        word += token[runner]
                elif token[runner] == '"':
                    if mode == AssembleMode.None:
                        mode = AssembleMode.Sentence
                    elif mode == AssembleMode.Symbol:
                        words.append(word)
                        word = ""
                        mode = AssembleMode.Sentence
                    elif mode == AssembleMode.Sentence:
                        words.append(word)
                        word = ""
                        mode = AssembleMode.None
                else:
                    word += token[runner]
                    if mode == AssembleMode.None:
                        mode = AssembleMode.Symbol
                        
                runner += 1

            if len(words) < 2:
                continue

            ##############################
            # Extract value of variable
            ##############################
            
            try:
                idx = words.index('CACHE')
                runner = 0
                val = words[1]
                while runner < (idx - 2):
                    val += ' '
                    val += words[runner + 2]
                    runner += 1
            except:
                val = words[1]
                
            dic = {"key":words[0], "val":val}
            vars.append(dic)

    except:
        return ""

    ##############################
    # Return matched value
    ##############################

    for j in vars:
        if j["key"] == keyname:
            return j["val"]

    return ""
