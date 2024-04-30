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

class Mundo2D:
    def __init__(self):
        self.pontos = []  # Lista de pontos
        self.faces = []   # Lista de faces
        self.arestas = [] # Lista de arestas
        self.cor = [255, 0, 0]

    def adicionarPonto(self, x, y):
        ponto = Ponto(x, y)
        self.pontos.append(ponto)
        return ponto

    def adicionarFace(self, ponto_indices):
        pontos = [self.pontos[i] for i in ponto_indices]
        face = Face(pontos)
        self.faces.append(face)

        # Atualização da lista de arestas
        for aresta in face.arestas:
            if aresta not in self.arestas:
                self.arestas.append(aresta)

    def pegarPonto(self, index):
        return self.pontos[index]

    def pegarAresta(self, index):
        return self.arestas[index]

    def pegarFace(self, index):
        return self.faces[index]
    
def rasterizarLinha(xInicial, yInicial, xFinal, yFinal, numeroDePontos):
    lista = []

    diferencaEntreX = xFinal - xInicial
    diferencaEntreY = yFinal - yInicial

    if abs(diferencaEntreX) >= abs(diferencaEntreY):
        passos = abs(diferencaEntreX)
    else:
        passos = abs(diferencaEntreY)

    pontoMedioX = diferencaEntreX / (numeroDePontos - 1)
    pontoMedioY = diferencaEntreY / (numeroDePontos - 1)

    x = xInicial
    y = yInicial

    for i in range(numeroDePontos):
        xArredondado, yArredondado = (x, y)
        
        if xArredondado >= min(xInicial, xFinal) and xArredondado <= max(xInicial, xFinal) and \
           yArredondado >= min(yInicial, yFinal) and yArredondado <= max(yInicial, yFinal):
            lista.append((xArredondado, yArredondado))

        x += pontoMedioX
        y += pontoMedioY

    return lista