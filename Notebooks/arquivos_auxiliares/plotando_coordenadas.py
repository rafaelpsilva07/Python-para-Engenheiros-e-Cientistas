# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:19:42 2020

@author: Rafael
"""

def pega_coordenadas(file_name):
    with open(file_name) as f:
        f_data = f.readlines()
        f.close
    
    linhas = []

    for i in range(len(f_data)):
        linhas.append(f_data[i].split(','))
    
    Coordenadas = {}
    Coordenadas['X'] = []
    Coordenadas['Y'] = []
    Coordenadas['Z'] = []

    for i in range(len(linhas)):
        x = float(linhas[i][3])
        y = float(linhas[i][4])
        z = float(linhas[i][5])

        Coordenadas['X'].append(x)
        Coordenadas['Y'].append(y)
        Coordenadas['Z'].append(z)    
    
    return Coordenadas

def plot_3dcoord(coord_dict):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = coord_dict['X']
    y = coord_dict['Y']
    z = coord_dict['Z']
    
    ax.scatter(x,y,z)


nome_arquivo = 'PONTOS_ESFERA.txt'

dicionario_esfera = pega_coordenadas(nome_arquivo)
plot_3dcoord(dicionario_esfera)









    
   
    
    
    
    