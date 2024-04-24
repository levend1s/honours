from ij import IJ
from ij.plugin.frame import RoiManager
from ij import CompositeImage
from ij.gui import ShapeRoi
import os

imp = IJ.getImage()
image_dir = IJ.getDirectory("Image")
out_dir = image_dir + imp.getTitle() + "_split/"

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

channel_combinations = ["100", "010", "001", "011", "110", "101", "111"]

rm = RoiManager.getRoiManager()
temp_roi = imp.getRoi()
imp.setRoi(temp_roi)
rm.addRoi(temp_roi)

for c in channel_combinations:
	imp_1 = imp.duplicate()
	imp_1.setActiveChannels(c)
	imp_1.cropAndSave([temp_roi], out_dir + imp.getTitle() + "_" + c + "_", "save png")

rm.select(rm.getRoiIndex(temp_roi))
rm.runCommand("delete")
rm.close()
