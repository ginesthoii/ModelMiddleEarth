# Exports all visible mesh objects as a single GLTF/GLB to ../webviewer/scene.gltf
# Run after generating/loading your scene.

import bpy
from pathlib import Path

# Ensure we only export visible meshes
for o in bpy.context.scene.objects:
    o.select_set(False)

export_path = (Path(__file__).resolve().parents[1] / "webviewer" / "scene.gltf").as_posix()
print(f"Exporting to: {export_path}")

bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',   # creates .gltf + .bin + textures
    export_selected=False,
    use_selection=False,
    export_apply=True
)

print("✅ Export complete. Open webviewer/index.html to preview.")