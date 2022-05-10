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
    def translationMatrix(VRP):
        traslationVRP = ([
            [1.0, 0.0, 0.0, - (VRP.x)],
            [0.0, 1.0, 0.0, - (VRP.y)],
            [0.0, 0.0, 1.0, - (VRP.z)],
            [0.0, 0.0, 0.0, 1.0],
        ]).astype(float)
    
        return traslationVRP

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