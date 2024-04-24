from ij import IJ
from ij.plugin.frame import RoiManager
from ij import CompositeImage
from ij.gui import ShapeRoi

imp = IJ.getImage()
dir = IJ.getDirectory("Image")

rm = RoiManager.getRoiManager()

channel_combinations = ["100", "010", "001", "011", "111"]

temp_roi = imp.getRoi()
imp.setRoi(temp_roi)
rm.addRoi(temp_roi)

for c in channel_combinations:
	imp_1 = imp.duplicate()
	imp_1.setActiveChannels(c)
	imp_1.cropAndSave([temp_roi], dir + imp.getTitle() + "_" + c + "_", "save png")

rm.select(rm.getRoiIndex(temp_roi))
rm.runCommand("delete")
rm.close()
