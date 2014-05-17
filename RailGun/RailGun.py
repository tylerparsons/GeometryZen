'''
RailGun.py
'''

from browser import *
from three import *
from workbench import *
from geometry import *


# RailGun Properties
I = 1000
mu_0 = 12.566E-7
pi = 3.1415
w = 1.0     # bore width
dt = 0.01

# Model Geometry
space3D = CartesianSpace()
workbench3D = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

# Projectile Definition
projectile = SphereBuilder().color("red").radius(0.1).build()
projectile.charge   = ScalarE3(1.0)
projectile.mass     = ScalarE3(1.0)
projectile.position = VectorE3(1.0, 0.0, 0.0)
projectile.velocity = VectorE3(0.0, 0.0, 0.0)
space3D.add(projectile)

# Model Animation
def setUp():
    workbench3D.setUp()

def tick(t):
    # Define quantities for calculation
    x = projectile.position
    m = projectile.mass
    # Solve equation of motion
    a = ((mu_0*I*I*x)/(m*pi))*(sqrt(w*w + x*x) - x)
    projectile.velocity = projectile.velocity + a * dt
    projectile.position = projectile.position + projectile.velocity * dt
    # Follow projectile
    space3D.camera.position.x = projectile.position.x
    space3D.camera.lookAt(projectile.position)
    space3D.render()
    
def terminate(t):
    return False

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
