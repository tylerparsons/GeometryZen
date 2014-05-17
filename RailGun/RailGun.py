'''
RailGun.py
'''

from browser import *
from three import *
from workbench import *
from geometry import *


# RailGun Properties
I = 100
mu_0 = 12.566E-7
pi = 3.1415
w = 1.0     # bore width
dt = 0.01

# Model Geometry
space3D = CartesianSpace()
i = VectorE3(1.0, 0.0, 0.0)
j = VectorE3(0.0, 1.0, 0.0)
k = VectorE3(0.0, 0.0, 1.0)

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
    projectile.acceleration = ((mu_0*I**2*x)/(m*pi))*(sqrt(w**2 + x**2) - x)
    projectile.velocity = projectile.velocity + projectile.acceleration * dt
    projectile.position = projectile.position + projectile.velocity * dt
    print "tick"
    print(projectile.acceleration)
    print(projectile.velocity)
    print(projectile.position)
    # Follow projectile
    space3D.camera.position.x = projectile.position.x
    space3D.camera.lookAt(projectile.position)
    space3D.render()
    
def terminate(t):
    return False

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
