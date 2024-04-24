# Setup

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
3. Restart Fiji.

# Usage

After selecting an area, press the `s` key. Images will be saved under a new folder called '[image name]_split'. The plugin will change your image to a composite image if not already.

If working working with multiple z-stacks, it will save the selection for the currently displayed z-stack. If you want to z-project, make sure you have saved the projection to file - this plugin will not work on temp images.

![Screenshot 2024-04-24 at 2 39 45 pm](https://github.com/levend1s/honours/assets/9210831/992b4560-9b5c-4299-ad9b-cc84094009ce)

