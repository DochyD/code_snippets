from pxr import Usd, UsdGeom
import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = dir + '/usd_output/test.usda'

# Open an existing USD file
stage = Usd.Stage.Open(file_path)

# Get the cube we created earlier
cube = UsdGeom.Cube(stage.GetPrimAtPath('/Xform/Cube'))

# Modify the size of the cube
cube.GetSizeAttr().Set(5.0)

# Add a translation to the existing Xform (moving the cube again)
cube.GetTranslateOp().Set((5.0, 0.0, 0.0))
#cube.AddTranslateOp().Set((5.0, 0.0, 0.0))

# Save the changes
stage.GetRootLayer().Save()

print("USD stage modified: cube resized and translated")