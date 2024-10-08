# -*- coding: utf-8 -*-
"""TP1_CSAA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14K4S0xF39l5BN330UU-J0nAn9od0Fc5N

# TP 1 - Espaces de représentation des couleurs


**Le test d'Ishihara**

Ce test, inventé en 1917 par Shinobu Ishihara, est un recueil de 38 planches utilisé pour dépister les anomalies de la vision des couleurs dont quelques exemples sont illustrés figure 1.

<img src="./ExTP1.png" width="800" height="600"  >


Ces tests composés de planches « pseudoisochromatiques » sont les plus fréquemment utilisés pour la détection des déficiences congénitales des teintes rouge et verte. Quelques-uns testent aussi les anomalies concernant la perception du bleu.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image


from mpl_toolkits.mplot3d import Axes3D

"""### Fonctions python intéressantes :
Liste de fonctions (librairies) :

- cov (numpy)
- transpose (numpy)
- corrcoef (numpy)
- linal.eig (numpy)
- reshape (numpy)
- @ (produit matriciel) ou dot (numpy)

## Exercice 1 - Corrélations et contrastes des planches RVB

Les lignes suivantes lit l'image $ishihara-0.png$ codée en RVB
(Rouge, Vert, Bleu) et la stocke dans une matrice tridimensionnelle $I$ de taille $hauteur \times largeur \times 3$.

On peut séparer cette matrice en trois sous-matrices bidimensionnelles appelées canaux : $R = I(i,j,0)$ pour le canal rouge, $V = I(i,j,1)$ pour le canal vert, et $B = I(i,j,2)$ pour le canal bleu.

Chacun d'entre eux est composé d'entiers compris entre 0 et 255, qui représentent l'intensité lumineuse du pixel situé sur la ligne $i$ et la colonne $j$. De part leur dénomination, chaque canal apporte donc une part de couleur à l'image, que ce soit du rouge, du vert ou du bleu.

### Représentations R, V et B

Chargement de l'image (à décommenter)
"""

# Importer des fichiers sur Google Colab à partir de votre ordinateur :

#from google.colab import files

#uploaded = files.upload()

# charge le fichier dans une matrice de pixels couleur.
Data=image.imread("ishihara-31.png")

# affiche les dimensions de la matrice.
print(Data.dtype)
print(Data.shape[0:2])

# accède à la valeur du premier pixel.
print(Data[0,0,0])


# Visualisation image
plt.imshow(Data)
plt.show()

# Decoupage de l'image en trois canaux et conversion en doubles :
R=Data[:,:,0]
V=Data[:,:,1]
B=Data[:,:,2]

# Affichage du canal R :
plt.imshow(R,cmap='gray')
plt.show()

# Affichage du canal V :
plt.imshow(V,cmap='gray')
plt.show()

# Affichage du canal B :
plt.imshow(B,cmap='gray')
plt.show()

"""En affichant les matrices $I$, $R$, $V$ et $B$ sous forme d’images, on observe que les images sont similaires et on distingue un motif dans les nuances de rouge.

Dans la suite, les pixels sont considérés comme des points de $R^3$ que l’on affiche dans un repère dont les axes correspondent aux trois niveaux de couleur.
"""

# Transformation image en nuage de pixels 3D : les trois canaux sont vectorises et concatenes
R=np.ravel(R)
V=np.ravel(V)
B=np.ravel(B)

print(R.shape)

# Affichage du nuage de pixels dans le repere RVB :
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(R, V, B, c='b', marker='o')

ax.set_xlabel('Niveau de Rouge')
ax.set_ylabel('Niveau de Vert')
ax.set_zlabel('Niveau de Bleu')

plt.show()

"""Ils forment un faisceau allongé suivant plusieurs directions, ce qui confirme l’observation précédente, à savoir que les trois canaux sont fortement corrélés.

### Etude de la corrélation entre les couleurs R, V et B
"""

# Matrice des donnees :
dim=R.shape[0]

# Les trois canaux sont vectorises et concatenes
X=np.zeros([dim,3])
X[:,0]=R
X[:,1]=V
X[:,2]=B

print(X.shape)

# Calculer la matrice de variance/covariance

import numpy as np

pixels = np.column_stack((X[:,0], X[:,1], X[:,2]))

cov_matrix = np.cov(pixels, rowvar=False)

print("Matrice de variance-covariance :")
print(cov_matrix)

# Calculer les coefficients de correlation lineaire (np.corrcoef)

import numpy as np


# Étape 1 : Extraire les variances et covariances
var_R = cov_matrix[0, 0]  # Variance du canal R
var_V = cov_matrix[1, 1]  # Variance du canal V
var_B = cov_matrix[2, 2]  # Variance du canal B

cov_RV = cov_matrix[0, 1]  # Covariance entre R et V
cov_RB = cov_matrix[0, 2]  # Covariance entre R et B
cov_VB = cov_matrix[1, 2]  # Covariance entre V et B

# Étape 2 : Calculer les écarts-types
std_R = np.sqrt(var_R)
std_V = np.sqrt(var_V)
std_B = np.sqrt(var_B)

# Étape 3 : Calculer les coefficients de corrélation
r_RV = cov_RV / (std_R * std_V)
r_RB = cov_RB / (std_R * std_B)
r_VB = cov_VB / (std_V * std_B)

# Étape 4 : Afficher les coefficients de corrélation
print(f"Coefficient de corrélation entre R et V: {r_RV:.4f}")
print(f"Coefficient de corrélation entre R et B: {r_RB:.4f}")
print(f"Coefficient de corrélation entre V et B: {r_VB:.4f}")

# Calculer les proportions de contraste :

import numpy as np

P_R = (std_R * std_R) / ((std_R * std_R)+(std_V * std_V)+(std_B * std_B))

P_V = (std_V * std_V) / ((std_R * std_R)+(std_V * std_V)+(std_B * std_B))

P_B = (std_B * std_B) / ((std_R * std_R)+(std_V * std_V)+(std_B * std_B))

print(f"Proportion de contraste de R: {P_R:.4f}")
print(f"Proportion de contraste de B: {P_B:.4f}")
print(f"Proportion de contraste de V: {P_V:.4f}")

"""## Exercice 2 - Analyse en Composantes Principales

Implémenter l'ACP :
1) extraire les 3 vecteurs propres, notés $X_1$, $X_2$, $X_3$, associés aux 3 plus grandes valeurs propres de la matrice de variance-covariance $\Sigma$ (par les fonctions *np.cov* et *np.linalg.eig*). Ces vecteurs propres constitueront le nouveau &
repère P c'est-à-dire les axes principaux.
2) Projetez ensuite les données dans cette nouvelle base en les multipliant par la base $P = [X_1X_2X_3]$.
"""

# Matrice des donnees :
dim=R.shape[0]

# Les trois canaux sont vectorises et concatenes
X=np.zeros([dim,3])
X[:,0]=R
X[:,1]=V
X[:,2]=B

print(X.shape)

"""Calculez la matrice de variance-covariance en utilisant par exemple la fonction **np.cov**"""

# Matrice de variance/covariance :
import numpy as np

pixels = np.column_stack((X[:,0], X[:,1], X[:,2]))

cov_matrix = np.cov(pixels, rowvar=False)

print("Matrice de variance-covariance :")
print(cov_matrix)

"""La matrice $\Sigma$ de variance/covariance est symétrique et réelle. Elle admet donc une base orthonormée de vecteurs propres.

Calculez ses valeurs propres et vecteurs propres à l'aide de l'appel à la fonction **np.linalg.eig**
"""



# Calcul des valeurs/vecteurs propres de Sigma :

import numpy as np

v_p , vec_p = np.linalg.eig(cov_matrix)

print(v_p)
print(vec_p)

#  Tri des valeurs propres :

import numpy as np

v_p.sort()

print(v_p)

""" Calculez la matrice des **composantes principales** des pixels  Projetez ensuite les données dans cette nouvelle base en multipliant chaque vecteur par la base $P = [X_1X_2X_3]$."""

# Calcul des composantes principales
#c'est à dire des coefficients de projection sur les axes principaux:

c1 = np.dot(X,vec_p[0])
c2 = np.dot(X,vec_p[1])
c3 = np.dot(X,vec_p[2])


print(c1)

print(c2)

print(c3)

# Projection sur la premiere composante principale :

pc = np.reshape(c1,Data.shape[0:2])


# Affichage de cette projection

plt.imshow(pc)
plt.show()

# Projection sur la deuxieme composante principale :
pc2 = np.reshape(c2,Data.shape[0:2])


# Affichage de cette projection

plt.imshow(pc2)
plt.show()

# Projection sur la troisieme composante principale :
pc3 = np.reshape(c3,Data.shape[0:2])


# Affichage de cette projection

plt.imshow(pc3)
plt.show()

"""## Etude la correlation dans le nouveau repère"""

# Matrice de variance/covariance dans le nouveau repere :

X_transformed = np.dot(X, vec_p)

cov_mat = np.cov(X_transformed, rowvar=False)

print("Matrice de variance-covariance dans le nouveau repére :")
print(cov_mat)

# Coefficients de correlation lineaire :

# Étape 1 : Extraire les variances et covariances
var_R = cov_mat[0, 0]  # Variance du canal R
var_V = cov_mat[1, 1]  # Variance du canal V
var_B = cov_mat[2, 2]  # Variance du canal B

cov1_RV = cov_mat[0, 1]  # Covariance entre R et V
cov1_RB = cov_mat[0, 2]  # Covariance entre R et B
cov1_VB = cov_mat[1, 2]  # Covariance entre V et B

# Étape 2 : Calculer les écarts-types
std_R = np.sqrt(var_R)
std_V = np.sqrt(var_V)
std_B = np.sqrt(var_B)

# Étape 3 : Calculer les coefficients de corrélation
r_RV = cov_RV / (std_R * std_V)
r_RB = cov_RB / (std_R * std_B)
r_VB = cov_VB / (std_V * std_B)

# Étape 4 : Afficher les coefficients de corrélation
print(f"Coefficient de corrélation entre R et V: {r_RV:.4f}")
print(f"Coefficient de corrélation entre R et B: {r_RB:.4f}")
print(f"Coefficient de corrélation entre V et B: {r_VB:.4f}")

# Proportions de contraste :

# Calculer les proportions de contraste :

import numpy as np

P_R = (std_R * std_R) / ((std_R * std_R)+(std_V * std_V)+(std_B * std_B))

P_V = (std_V * std_V) / ((std_R * std_R)+(std_V * std_V)+(std_B * std_B))

P_B = (std_B * std_B) / ((std_R * std_R)+(std_V * std_V)+(std_B * std_B))

print(f"Proportion de contraste de R: {P_R:.4f}")
print(f"Proportion de contraste de B: {P_B:.4f}")
print(f"Proportion de contraste de V: {P_V:.4f}")

"""### Interprétation

Le but du test de Ishihara est d'identifier les personnes qui ne distinguent pas, dans une image de luminance à peu près uniforme, un motif n'apparaissant que dans les chrominances. Il est donc voulu que l'on ne distingue le motif que dans la deuxième et/ou la troisième composante(s) principale(s).

**Comment est-ce possible puisque le contraste est censé être maximal dans la première composante principale ?**

S. Ishihara a justement créé des images de sorte que le contraste soit faible entre les couleurs du motif et celles du reste de l'image, alors qu'il y a un fort contraste dans la luminance, grâce au fait que ses images contiennent beaucoup de pixels blancs (entre les taches colorées).

## Exercice 3 - Quizz

Des symboles de la culture Geek se cachent dans des mosaïques d'Ishihara (archive *Quizz_GroupeXX.zip*).

Utilisez l'ACP pour les faire apparaître et à vous de les identifier !
"""
91
