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

def channelIDsToWavelengths(cs):
	l = len(cs)
	r = "channels=["
	i = 1
	for x in cs:
		if x == "1":
			r += imp.getStringProperty("Wavelength " + str(i) + " (in nm)")
			r += ","
		i += 1
	r = r[:-1] + "]"

	return r

if imp.getNChannels() > 4:
	print("too many channels! untested behaviour, exiting...")
	exit(1)
else:
	channel_combinations = getChannelCombinations(imp.getNChannels())
	rm = RoiManager.getRoiManager()
	temp_roi = imp.getRoi()
	imp.setRoi(temp_roi)
	rm.addRoi(temp_roi)
	
	for c in channel_combinations:
		imp_1 = imp.duplicate()
		imp_1.setZ(imp.getZ())
		imp_1.setActiveChannels(c)
		
		channel_string = c
		if imp.getTitle().split(".")[-1] == "dv": 
			channel_string = channelIDsToWavelengths(c)

		imp_1.cropAndSave([temp_roi], out_dir + imp.getTitle() + "_" + channel_string + "_ROI=", "save png")
	
	rm.select(rm.getRoiIndex(temp_roi))
	rm.runCommand("delete")
	rm.close()
