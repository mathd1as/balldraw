import math
from re import X
from tokenize import Double, String

from .Vertex import Vertex

class GeometricTransformation:
    @staticmethod
    def rotation(vertex: Vertex, angle: float, axel: String):
        sen = math.sin(math.radians(angle))
        cos = math.cos(math.radians(angle))
        
        if axel == "x" :
            vertex.y, vertex.z = (vertex.z * sen) + (vertex.y * cos) ,(vertex.z * cos) - (vertex.y * sen)

        if axel == "y":
            vertex.x, vertex.z = (vertex.x * cos) + (vertex.z * sen), (vertex.z * cos) - (vertex.x*sen)

        if axel == "z":
            vertex.y, vertex.x = (vertex.x * sen) + (vertex.y * cos), (vertex.x * cos) - (vertex.y * sen)

        return Vertex(vertex.x, vertex.y, vertex.z)

    @staticmethod
    def translation(vertex: Vertex, dest: Vertex):
        vertex.x,vertex.y,vertex.z = dest.x - vertex.x, dest.y - vertex.y, dest.z - vertex.z    
        return Vertex(vertex.x, vertex.y, vertex.z)

    @staticmethod
    def scale(vertex: Vertex, size: Double):
        vertex.x,vertex.y,vertex.z = vertex.x*size, vertex.y*size, vertex.z*size
        return Vertex(vertex.x, vertex.y, vertex.z)

    @staticmethod
    def calculateNormalVector(VRP,focalPoint):    
        normal = Vertex(
            VRP.x - focalPoint.x,
            VRP.y - focalPoint.y,
            VRP.z - focalPoint.z
        )   
        
        normalModule = math.sqrt((pow(normal.x, 2) + pow(normal.y, 2) + pow(normal.z, 2)))
       
        return Vertex(
            normal.x / normalModule,
            normal.y / normalModule,
            normal.z / normalModule,
        )
    
    @staticmethod
    def calculateViewUpVector(normalVector, viewUp):
        scalarProduct = (normalVector.x * viewUp.x) + (normalVector.y * viewUp.y) + (normalVector.z * viewUp.z)

        scalarVector = Vertex(
            viewUp.x - (scalarProduct * normalVector.x), 
            viewUp.y - (scalarProduct * normalVector.y), 
            viewUp.z - (scalarProduct * normalVector.z)
        )
        
        scalarModule = math.sqrt((pow(scalarVector.x, 2) + pow(scalarVector.y, 2) + pow(scalarVector.z, 2)))
        
        return Vertex(
            scalarVector.x / scalarModule,
            scalarVector.y / scalarModule,
            scalarVector.z / scalarModule
        )

    @staticmethod
    def crossProduct(a: Vertex, b:Vertex):
        return Vertex(
            (a.y*b.z)-(a.z*b.y),
            (a.z*b.x)-(a.x*b.z),
            (a.x*b.y)-(a.y*b.x)
        )

    @staticmethod
    def distanceTwoVertexes(a: Vertex, b: Vertex):
        return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2)+math.pow(a.z-b.z,2))
    
    @staticmethod
    def dotProduct(a: Vertex, b: Vertex):
        return (a.x*b.x)+(a.y*b.y)+(a.z*b.z)
    
    @staticmethod
    def calculateVrpTranslation(vrp: Vertex):
        return Vertex(-vrp.x, -vrp.y, -vrp.z)

    @staticmethod
    def calculateSRCVertexes( vertexes, VRP, focalPoint, viewUp):
        n = GeometricTransformation.calculateNormalVector(VRP, focalPoint)
        v = GeometricTransformation.calculateViewUpVector(n, viewUp)
        u = GeometricTransformation.crossProduct(v,n)
        vrpT = GeometricTransformation.calculateVrpTranslation(VRP)

        print("N^=",n.coordinatesXYZ())
        print("Y^=",v.coordinatesXYZ())
        print("U^=",u.coordinatesXYZ())
        vrpDotU = GeometricTransformation.dotProduct(vrpT,u)
        vrpDotv = GeometricTransformation.dotProduct(vrpT,v)
        vrpDotn = GeometricTransformation.dotProduct(vrpT,n)

        for vertex in vertexes:
            vertex.x,vertex.y,vertex.z = [    
                (u.x*vertex.x)+(u.y*vertex.y)+(u.z*vertex.z)+(vrpDotU),
                (v.x*vertex.x)+(v.y*vertex.y)+(v.z*vertex.z)+(vrpDotv),
                (n.x*vertex.x)+(n.y*vertex.y)+(n.z*vertex.z)+(vrpDotn)
            ]

    @staticmethod
    def calculateSRTVertexes(vertexes, vertexMinWindow, vertexMaxWindow, vertexMinView, vertexMaxView, dp):
        deltaView = Vertex(vertexMaxView.x - vertexMinView.x, vertexMaxView.y - vertexMinView.y, 1)
        deltaWindow = Vertex(vertexMaxWindow.x - vertexMinWindow.x, vertexMaxWindow.y - vertexMinWindow.y, 1)
        u1 = (-vertexMinWindow.x * (deltaView.x/deltaWindow.x))+vertexMinView.x
        u2 = vertexMinWindow.y *(deltaView.y/deltaWindow.y)+vertexMaxView.y
        x = deltaView.x/deltaWindow.x
        y = (vertexMinView.y-vertexMaxView.y)/deltaWindow.y
        print("----------",x,y,u1,u2)
        for v in vertexes:
            v.x = ((v.x/dp)*x)+u1
            v.y = ((v.y/dp)*y)+u2
            v.z = (v.z/dp)

