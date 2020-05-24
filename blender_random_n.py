import bpy
import math
from random import random, randrange

for i in range(2000):
    
    rand = random()
    x =+ -rand if randrange(10) % 2 else rand
    y =+ -rand if randrange(10) % 2 else rand
    z =+ -rand if randrange(10) % 2 else rand

    bpy.ops.transform.translate(value = (x, y, z))
    
    bpy.ops.transform.rotate(value=-rand, orient_axis='Z')
    bpy.ops.transform.rotate(value=-rand, orient_axis='X')
    bpy.ops.transform.rotate(value=-rand, orient_axis='Y')
    
    bpy.ops.transform.resize(value=(1.001, 1.001, 1.001))
    bpy.ops.export_mesh.ply(filepath=f"D:/neural_network/blender_cloud_ply/dataset_figure/sphere/sphere_{i}.ply")
