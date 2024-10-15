"""Create a simple USD stage"""
import os
from pxr import Usd, UsdGeom, Gf

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = DIRECTORY + '/usd_output/test.usda'

# Create a new USD stage with a root Xform
stage = Usd.Stage.CreateNew(FILE_PATH)


# Define a basic root Xform (transformation) at the root of the stage
xform = UsdGeom.Xform.Define(stage, '/Xform')

# Add a Cube to the stage under the Xform
cube = UsdGeom.Cube.Define(stage, '/Xform/Cube')

# Set the size of the cube
cube.GetSizeAttr().Set(2.0)

# Optionally set a translation on the cube
cube.AddTranslateOp().Set(Gf.Vec3f(3.0, 3.0, 3.0))

# Save the stage
stage.GetRootLayer().Save()

print("USD stage created with a cube at '/Xform/Cube'")
