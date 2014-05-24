"""
RailGun.py
@author     Tyler Parsons
@created    17 May 2014

Visualization of a rail gun based on a
numerical solution to the analytically
obtained differential equation of mot-
ion.

References:
http://www.geometryzen.org/users/geometryzen/repos/demos/blob/master/Physics/qubit-visualization.py
http://www.geometryzen.org/users/geometryzen/repos/demos/blob/master/Physics/charged-particle-wire-1.py
http://www.geometryzen.org/users/geometryzen/repos/demos/blob/master/Canvas-3D/Geometries/CylinderGeometry.py
"""

from browser import *
from easel import *
from geometry import *
from math import sqrt
from three import *
from workbench import *


########################
# Model Initialization #
########################

# RailGun Properties
# Change I and w to adjust motion of particle
I = 1000
mu_0 = 12.566E-7
pi = 3.1415
w = 0.4     # bore width
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
heightSegments = height
openEnded = True
cylinder = CylinderGeometry(radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded, i)
mesh = Mesh(cylinder, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space3D.add(mesh)

#####################
# Data Display Pane #
#####################
canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
font = "20px Courier New"
color = "#FFFFFF"

workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

# Create text object, return handle
def displayText(text, x, y):
    textBox = Text(text, font, color)
    textBox.x = x
    textBox.y = y
    space2D.addChild(textBox)
    return textBox

# Display Qunatities
iText = displayText("I:    "+str(I), 50, 50)
wText = displayText("w:    "+str(w), 50, 75)
xText = displayText("x:    "+str(projectile.position.x), 50, 100)
vText = displayText("v:    "+str(projectile.velocity.x), 50, 125)

###################
# Model Animation #
###################
def setUp():
    workbench3D.setUp()
    workbench2D.setUp()

def tick(t):
    # Define quantities for calculation
    x = projectile.position
    m = projectile.mass
    # Solve equation of motion
    if x.x <= boreLength:
        a = ((mu_0*I*I*x)/(m*pi))*(sqrt(w*w + x*x) - x)
        projectile.velocity = projectile.velocity + a * dt
    projectile.position = projectile.position + projectile.velocity * dt
    # Follow projectile
    space3D.camera.position.x = projectile.position.x
    space3D.camera.lookAt(projectile.position)
    space3D.render()
    # Update data
    xText.text = "x:    "+str(projectile.position.x)
    vText.text = "v:    "+str(projectile.velocity.x)
    space2D.render()

def terminate(t):
    return projectile.position.x > boreLength*3

def tearDown(e):
    workbench2D.tearDown()
    workbench3D.tearDown()
    if e:
        print e

# Run
WindowAnimationRunner(tick, terminate, setUp, tearDown, window).start()
