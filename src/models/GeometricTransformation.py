import math
from re import X
from tokenize import Double, String
from .Vertex import Vertex

class GeometricTransformation:
    @staticmethod
    def rotation(vertex: Vertex, angle: int, axel: String):
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