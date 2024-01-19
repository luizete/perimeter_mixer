# Perimeter Mixer
Get better prints with mixed perimeters order! Use internal perimeters first only when necessary.

## Theory
Generally, enabling the option External Perimeter First on SuperSlicer grants better external layers quality and layer stacking consistency on some prints. However, enabling it may interfere with overhangs. Thus, by printing layers without overhangs with this option enabled, we grant a better print without countersides.

## How it works
It is needed to slice the plate two times: The first one, with the option External Perimeter First enabled, and the second one with it disabled. This script merges both g-codes, using the first one as the principal, replacing layers with overhang by it respective g-code present on the second file.
To detect whether a layer has an overhang, the script checks for the presence of the string ";TYPE:Overhang perimeter" at least once in the layer's g-code.

## Disclaimer
I still haven't tested this code!
