# Thanks to ChatGPT

def calculate_collision_velocities(mA, mB, VAix, VAiy, VBix, VBiy):
    # Conservation of momentum equations
    VAfx = ((mA - mB) * VAix + (2 * mB) * VBix) / (mA + mB)
    VBfx = ((2 * mA) * VAix + (mB - mA) * VBix) / (mA + mB)

    VAfy = ((mA - mB) * VAiy + (2 * mB) * VBiy) / (mA + mB)
    VBfy = ((2 * mA) * VAiy + (mB - mA) * VBiy) / (mA + mB)

    return VAfx, VAfy, VBfx, VBfy

mA = 2.0  # Mass of ball A
mB = 1.5  # Mass of ball B
VAix = 3.0  # Initial x-component velocity of ball A
VAiy = 2.0  # Initial y-component velocity of ball A
VBix = -1.0  # Initial x-component velocity of ball B
VBiy = 4.0  # Initial y-component velocity of ball B

VAfx, VAfy, VBfx, VBfy = calculate_collision_velocities(mA, mB, VAix, VAiy, VBix, VBiy)

print("Final velocities of ball A:")
print("Vafx:", VAfx)
print("Vafy:", VAfy)
print("Final velocities of ball B:")
print("Vbfx:", VBfx)
print("Vbfy:", VBfy)
