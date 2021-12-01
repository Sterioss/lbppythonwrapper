# CODE
import subprocess
import os

GRAYSCALE = "0"
COLOR = "1"
dir_path = os.path.dirname(os.path.realpath(__file__))
prgm = os.path.join(dir_path ,"clbp")

def lbp_hist(img_path, color):
    proc = subprocess.Popen([prgm, img_path, color], stdout=subprocess.PIPE)
    img_hist = []
    for x in range(3):
        line = proc.stdout.readline()[:-2]
        img_hist.append(line.decode("utf-8").split(','))
    proc.wait()
    return img_hist