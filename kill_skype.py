#! /usr/bin/env python

import os

ps_command = "ps aux | grep skype"
ps_lines = os.popen( ps_command ).read()

for line in ps_lines.split("\n"):

    if not line.startswith("jim"):
        continue

    
    if line.split()[10] == "skype":
        kill_command = "kill -KILL " + str(line.split()[1])

        os.system( kill_command )

        
