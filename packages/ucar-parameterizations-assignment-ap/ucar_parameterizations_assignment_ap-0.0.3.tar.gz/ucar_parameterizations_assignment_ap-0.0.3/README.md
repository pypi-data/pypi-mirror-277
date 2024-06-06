# ucar-parameterization-assignment-ap
 **UCAR assignment for Software Engineer I role. Made in Python.**

 This community-oriented  package was designed to allow for easy use and creation of Foo et al. parameterizations in foo physics. Presently consists of parent Shape class and child Sphere class for demonstration of planned usage and implementation.

## Installation

The installation for the package should be the same on all platforms, but can vary depending on the PATH variables you may or may not have set up:

**If you have pip as a PATH variable:**

```
pip install ucar-parameterization-assignment-ap
```
**otherwise:**
```
python3 -m pip install ucar-parameterization-assignment-ap
```

## Usage

```
from parameterizations.shapes import Shape, Sphere 
```

From here, you can use the built in classes to calculate properties of a sphere, including perimeter (circumference) or volume.

Or, you could create more shapes according to the Shape class and stem from there with your own calculations.