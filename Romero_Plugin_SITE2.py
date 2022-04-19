import rhinoscriptsyntax as rs
import Rhino as rh
import System
import scriptcontext as sc
import math
import random
import Rhino
from math import radians
from math import sin
from math import cos

#OPEN FILE SOURCE: https://discourse.mcneel.com/t/try-to-open-a-file-through-python/32886

#site_2 = '"C:\Users\lizbe\Desktop\Studio 5B\Week 12\\SITE-2.3dm"'
#
#rs.DocumentModified(False)
#rs.Command('_-Open {} _Enter'.format(site_2))

points = (0,0,0),(150,0,0),(150,136,0),(0,136,0),(0,0,0)
site = rs.AddPolyline(points)

150,136,1,5
def cube_grid(x_number, y_number, z_number, space):
    x_n = int(x_number)
    y_n = int(y_number)
    z_n = int(z_number)
    
    coords = []
    
    int_space = int(space)
    
    for i in range(0, x_n, int_space):
        for j in range(0, y_n, int_space):
            for p in range (0, z_n, int_space):
                x_val = i
                y_val = j
                z_val = p
                coords.append((x_val, y_val, z_val))
                
    return coords

#GRID

def CreateGrid(Xnumber,Ynumber,Znumber,Distance):
    #Creates a 3D Grid
    Grid = []
    for i in range(0,Xnumber,Distance):
        x = i
        for j in range(0,Ynumber,Distance):
            y = j
            for p in range(0,Znumber,Distance):
                z = p

                Grid.append((x,y,z))
    return(Grid)

def site2():
    #SITE 2
    objs = rs.GetObjects("Select planar curves to build surface", rs.filter.curve)
    plane = rs.AddPlanarSrf(objs)
    points = cube_grid(150,136,1,5)
    rs.AddPoints(points)
    ids = rs.GetObjects("Select plane and points to lock site in place to start creating, you have to stay within the plane and move objects onto points")
    if ids:
        rs.LockObjects(ids)
site2()

#//////////////////////////////////////////////////

#UNIT A_1

def arc_rail(radius, num_parts):
    color_value = rs.StringBox("Specify a color, Red, Pink, Purple, Magenta, Blue, Teal, Yellow or Green", default_value="Red", title="Color")
    if color_value == "Red":
        color_1 = 255, 0, 0
    if color_value == "Pink":
        color_1 = 255,65,100 
    if color_value == "Blue":
        color_1 = 0,255,255
    if color_value == "Teal":
        color_1 = 0,175,100
    if color_value == "Purple":
        color_1 = 128,0,128
    if color_value == "Magenta":
        color_1 = 255, 0, 255
    if color_value == "Yellow":
        color_1 = 255, 255,0
    if color_value == "Green":
        color_1 = 0,255,0
    
    rotation = -360/num_parts
    plane_1 = rs.WorldYZPlane()
    plane_1 = rs.RotatePlane(plane_1,0.0,[0,0,0])
    plane_1 = rs.MovePlane(plane_1,[0,0,0])
    arc_1 = rs.AddArc(plane_1,radius,90.0)
    arc_2 = rs.RotateObject(arc_1,[0,0,0],rotation,None,copy=True)
    point_1 = rs.AddPoint(0,radius,0)
    center =  rs.RotateObject(point_1,[0,0,0],rotation,None,copy=True)
    radius_2 = rs.Distance(point_1, center)
    circle = rs.AddCircle(center, radius_2/2)
    part = rs.AddSweep2([arc_1, arc_2], [circle], closed=False)
    
    color = rs.CreateColor(color_1)
    rs.AddMaterialToObject(part)
    rs.ObjectColor(part,color)
    Index = rs.ObjectMaterialIndex(part)
    rs.MaterialColor(Index,color)
    
    return (part, center)

def polar_array(center, radius, num_points, object):
    points = []
    angle = int(360/num_points)
    cx = center[0]
    cy = center[1]
    for i in range(0,360,angle):
        deg = radians(i)
        x = cos(deg)*radius + cx
        y = sin(deg)*radius + cy
        rs.RotateObject(object, center, i*1, copy=True)
        points.append((x,y))
    points = rs.AddPoints(points)
    rs.HideObjects(points)
    return points

def inflatable_dome(radius, parts):


    part_object = arc_rail(radius, parts)
    
    part_unit = part_object[0]
    
    part_center = part_object[1]
    
    p_points = polar_array((0,0,0), radius, parts, part_unit)


#UNIT A_2

inflatable_dome(9, 12)

def move():
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()

inflatable_dome(9, 8)



def move():
    for i in range(2):
        objectIds = rs.GetObjects("Select objects to copy")
        start = rs.GetPoint("Point to copy from")
        end = rs.GetPoint("Point to copy to", start)
        translation = end-start
        rs.CopyObjects(objectIds, translation)
    
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()

#UNIT B_1

inflatable_dome(10,30)

ids = rs.GetObjects("Select Unit C-2 of Program")
move = rs.MoveObjects(ids,[0,-3.5,0])

rs.MessageBox("Make the next outcome the same color.")

#UNIT B_2

inflatable_dome(16,36)

def move():
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()

#UNIT B_3

inflatable_dome(14,24)

def move():
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()

#UNIT C_1

inflatable_dome(14,45)

def move():
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()

#UNIT C_2

inflatable_dome(12,20)

def move():
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()

#UNIT D

inflatable_dome(8,8)

for i in range(5):
    objectIds = rs.GetObjects("Select objects to copy")
    start = rs.GetPoint("Point to copy from")
    end = rs.GetPoint("Point to copy to", start)
    translation = end-start
    rs.CopyObjects(objectIds, translation)

def move():
    ids = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(ids, translation)
move()