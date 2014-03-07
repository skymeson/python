#! /usr/bin/env python

import os,sys,ROOT

folders = os.listdir(".")
out_file = file("Zombies.txt", 'w')
for folder in folders:

    if not os.path.isdir(folder): continue
    print "Checking for Zombies in " + str(folder)
    files = os.listdir( folder )

    for file in files:

        if not ".root" in file: continue

        
        this_file = ROOT.TFile( folder + "/" + file, 'r' )

        if this_file.IsZombie():
            print "Zombie found: " + folder + "/" + file
            out_file.write( folder + "/" + file + "\n" )

out_file.close()
