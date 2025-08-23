# Run in Blender's Scripting workspace (Blender 3.x+)
# File > New > General, then open this file and press "Run Script"

import bpy
import random

# --- Reset scene ---
bpy.ops.wm.read_homefile(use_empty=True)

# --- Create a large subdivided plane ---
size = 80
cuts = 200
bpy.ops.mesh.primitive_plane_add(size=size, enter_editmode=True)
bpy.ops.mesh.subdivide(number_cuts=cuts)
bpy.ops.object.mode_set(mode="OBJECT")
plane = bpy.context.active_object
plane.name = "Terrain"

# --- Displace with procedural noise ---
displace = plane.modifiers.new("Displace", type='DISPLACE')
tex = bpy.data.textures.new("MountainTex", type='CLOUDS')
tex.noise_scale = random.uniform(0.8, 2.2)
tex.noise_depth = 2
displace.texture = tex
displace.strength = random.uniform(6.0, 12.0)

# --- Smooth + simple shading ---
bpy.ops.object.shade_smooth()

# --- Add a Sun light ---
bpy.ops.object.light_add(type='SUN', radius=1, location=(40, -40, 60))
sun = bpy.context.active_object
sun.data.energy = 3.0

# --- Add a camera looking at the terrain ---
bpy.ops.object.camera_add(location=(0, -size*1.2, size*0.7), rotation=(1.1, 0, 0))
cam = bpy.context.active_object
bpy.context.scene.camera = cam

# --- (Optional) auto-enable Cycles for nicer preview renders ---
bpy.context.scene.render.engine = 'BLENDER_EEVEE'  # switch to 'CYCLES' if you like

print("🌄 Procedural terrain generated. Try it a few times — seeds vary the mountains.")