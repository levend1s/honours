from ij import IJ
from ij.plugin.frame import RoiManager
from ij import CompositeImage
from ij.gui import ShapeRoi
import os
from itertools import product

imp = IJ.getImage()
image_dir = IJ.getDirectory("image")
out_dir = image_dir + imp.getTitle() + "_split/"

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

# magic
def getChannelCombinations(n):
	r = []
	tups = [i for i in product(range(2), repeat=n)]
	for t in tups:
		r.append("".join(str(x) for x in t))
	
	r.pop(0) # remove the one with all 0s
	return r

num_channels = imp.getNChannels()

if num_channels > 4:
	print("too many channels! untested behaviour, exiting...")
	exit(1)
else:
	channel_combinations = getChannelCombinations(num_channels)
	rm = RoiManager.getRoiManager()
	temp_roi = imp.getRoi()
	imp.setRoi(temp_roi)
	rm.addRoi(temp_roi)
	
	for c in channel_combinations:
		imp_1 = imp.duplicate()
		imp_1.setZ(imp.getZ())
		imp_1.setActiveChannels(c)
		imp_1.cropAndSave([temp_roi], out_dir + imp.getTitle() + "_" + c + "_", "save png")
	
	rm.select(rm.getRoiIndex(temp_roi))
	rm.runCommand("delete")
	rm.close()
