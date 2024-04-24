# Usage

1. Use the Fiji menu option `Plugins->Install` and select Save_Selection_and_Split.py to install the plugin.
2. Add the following code to the file macros/StartupMacros.fiji.ijm. This file is located on MacOS by navigating to the Applications folder, right-clicking on Fiji and clicking 'Show Package Contents'.
```
macro "Save and Split Selection [s]" {
	Property.set("CompositeProjection", "Sum");
	Stack.setDisplayMode("composite");
	run("Save Selection and Split");
	Dialog.create("");
	var dir = getInfo("image.directory");
	var title = getInfo("image.filename");
	Dialog.addMessage("Images Saved to: " + dir + title + "_split/");
	Dialog.show();
}
```

