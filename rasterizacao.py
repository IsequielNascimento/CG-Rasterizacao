import matplotlib.pyplot as plt
import numpy as np
import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Aresta:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Face:
    def __init__(self, pontos):
        self.pontos = pontos  # Lista de pontos que formam a face
        self.arestas = []     # Lista de arestas que formam a face

        # Criação de arestas
        for i in range(len(pontos)):
            self.arestas.append(Aresta(
                pontos[i], 
                pontos[(i + 1) % len(pontos)]
            ))

