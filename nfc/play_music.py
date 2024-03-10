# Connect to bluetooth speaker
# https://gist.github.com/actuino/9548329d1bba6663a63886067af5e4cb
# import os
# os.system("clvc --play-and-exit behx.mp3")
from subprocess import call
call(["cvlc", "--play-and-exit", "behx.mp3"])
