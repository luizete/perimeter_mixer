# Perimeter Mixer
Achieve better prints with mixed perimeters order! Only use internal perimeters first if necessary.

## Theory
In general, enabling the External Perimeters First option in SuperSlicer will result in better quality external layers for some prints. However, enabling this option can affect overhangs. So if you print layers without overhangs with this option enabled, you will get a better print with no opposing sides.

## How does it work?
It is necessary to slice the plate twice: The first time with the External margin first option enabled and the second time with the option disabled. This script merges both g-codes, using the first one as a base and replacing layers with overhang with the corresponding g-code in the second file. To detect whether a layer has an overhang, the script checks whether the string ";TYPE:Overhang perimeter" occurs at least once in the layer's g-code.

## How to use it
Just run it with Python 3:

```python3 pmixer.py *file1* *file2* *outfile*```

- *file1* must be the g-code that was sliced with the option "External perimeters first" enabled
- *file2* must be the g-code that was sliced with the option "External perimeters first" disabled
- *outfile* is the file name for\ the generated mixed g-code output

## To Do
- Improve code performance and readability
- Add exception handling
- Add threshold for overhangs

## Disclaimer
I have not tested this code yet!
