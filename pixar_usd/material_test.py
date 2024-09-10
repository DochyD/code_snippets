from pxr import Usd, UsdGeom, UsdShade, Sdf
import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = dir + '/usd_output/material_example.usda'

stage = Usd.Stage.CreateNew(file_path)

# Define a root Xform and a Cube
xform = UsdGeom.Xform.Define(stage, '/Root')
cube = UsdGeom.Cube.Define(stage, '/Root/Cube')

# Create a material
material = UsdShade.Material.Define(stage, '/Root/Material')

# Create a shader within the material
shader = UsdShade.Shader.Define(stage, '/Root/Material/Shader')

# Set the shader type (UsdPreviewSurface is a basic shader for USD)
shader.CreateIdAttr("UsdPreviewSurface")

# Set some shader attributes (like diffuse color)
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((1.0, 0.0, 0.0))  # Red color

# Bind the material to the cube
UsdShade.MaterialBindingAPI(cube).Bind(material)

# Save the stage
stage.GetRootLayer().Save()

print("USD stage created with a red cube and a material")