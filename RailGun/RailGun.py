'''
RailGun.py
@author     Tyler Parsons
@created    17 May 2014

Visualization of a rail gun based on a
numerical solution to the differential
equation of motion.

References:


'''

from browser import *
from easel import *
from math import sqrt
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
i = VectorE3(1, 0, 0)
workbench3D = Workbench3D(space3D.renderer.domElement, space3D.renderer, space3D.camera)

# Projectile Definition
projectile = SphereBuilder().color("red").radius(w/2).build()
projectile.mass     = ScalarE3(1.0)
projectile.position = VectorE3(1.0, 0.0, 0.0)
projectile.velocity = VectorE3(0.0, 0.0, 0.0)
space3D.add(projectile)

# Draw Bore
boreLength = 10
radiusTop = w/2
radiusBottom = w/2
height = boreLength*2
radialSegments = 32
heightSegments = boreLength
openEnded = True
cylinder = CylinderGeometry(radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded, i)
mesh = Mesh(cylinder, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space3D.add(mesh)

# Model Animation
def setUp():
    workbench3D.setUp()

def tick(t):
    # Define quantities for calculation
    x = projectile.position
    m = projectile.mass
    # Solve equation of motion
    if x.x <= boreLength
        a = ((mu_0*I*I*x)/(m*pi))*(sqrt(w*w + x*x) - x)
        projectile.velocity = projectile.velocity + a * dt
    projectile.position = projectile.position + projectile.velocity * dt
    # Follow projectile
    space3D.camera.position.x = projectile.position.x
    space3D.camera.lookAt(projectile.position)
    space3D.render()

def terminate(t):
    return projectile.position.x > boreLength*3

def tearDown(e):
    workbench3D.tearDown()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
