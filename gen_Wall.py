from solid2 import scad_render_to_file
from solid2 import cube, cylinder, up, forward, right, rotate, union, difference

# Simple “stone” wall with merlons/embrasures you can tweak
def wall_segment(length=60, thickness=6, height=24, crenel_width=6, merlon_width=6, crenel_depth=3):
    base = cube([length, thickness, height])

    # Crenellations along the top edge
    units = int(length // (crenel_width + merlon_width))
    parts = [base]
    for i in range(units + 1):
        x = i * (crenel_width + merlon_width)
        # carve the crenel out of the top front edge
        crenel = up(height - 6)(forward(thickness - crenel_depth)(
            cube([crenel_width, crenel_depth + 0.1, 6])
        ))
        parts.append(difference()(right(x)(crenel)))
    return difference()(*parts)

def buttress(width=8, depth=10, height=28, spacing=20, count=2):
    parts = []
    for i in range(count):
        x = spacing * (i+1)
        parts.append(right(x)(cube([width, depth, height])))
    return union()(*parts)

def walkway(length=60, thickness=6, lip=2):
    return up(24)(cube([length, thickness+lip, 2]))

def make_wall():
    w = wall_segment()
    b = forward(-4)(buttress())
    walk = walkway()
    return union()(w, b, walk)

if __name__ == "__main__":
    model = make_wall()
    scad_render_to_file(model, filepath="out/wall_segment.scad", file_header="$fn=64;")
    print("Wrote out/wall_segment.scad  → open in OpenSCAD and export STL.")
