#ARE - Heisenberg
#Moro MANE, Nicolas MILON, Fabien TANG, Marie-Céline BESHARA

import random
import numpy as np
import math

#Génération de la ville d'Albuquerque
#l = longueur
#L = largeur
#e = espacement entre les routes
def albuquerque(l,L,e):
    ville=np.ones([l,L])    
    for i in range (0,l,e+1):
        for j in range (0,L):
            ville[i,j]=0
    for j in range (0,L,e+1):
        for i in range (0,l):
            ville[i,j]=0
    return ville

#Taille de la ville
a = 10
b = 10

#p = Densité de dealer (ex: si p = 100%, il y a que des dealers à la place des routes...)
#p2 = Densité de population
#p3 = Densité de policiers
def ville (p,p2, p3):
    #cpt
    cpt=0
    #Génération d'Albuquerque (en 10*10 avec un espacement de 2 entre les routes)
    ville=albuquerque(a,b,2)
    #Coordonnées des routes d'albuquerque
    cr=[(n,m)for n in range (1,ville.shape[0]-1) for m in range (1,ville.shape[1]-1) if ville[n,m]==0]
    #Nombre de dealer que l'on doit tirer
    n = (p*len(cr))
    #l2
    l2=cr
    #lr
    lr=[]
   #On tire aléatoirement n coordonnées aux hasards parmis cr
    while cpt <n:
        x=random.randint(0,(len(l2)-1))
        y=l2[x]
        lr.append (y)
        l2.remove (y)
        cpt+=1
    #Placement des dealers
    ville2=np.copy(ville)
    for (x,y) in lr:
        #on place le dealer
        ville2[x,y]=3       
    cpt=0
    #Nombre de personnes saine que l'on doit tirer
    n = (p2*len(cr))
    #l2
    l2=cr
    #lr
    lr=[]
   #On tire aléatoirement n coordonnées aux hasards parmis cr
    while cpt <n:
        x=random.randint(0,(len(l2)-1))
        y=l2[x]
        lr.append (y)
        l2.remove (y)
        cpt+=1
    #Placement de la population
    for (x,y) in lr:
    #on place la population
        ville2[x,y]=2
        
    cpt=0
    #Nombre de personnes saine que l'on doit tirer
    n = (p3*len(cr))
    #l2
    l2=cr
    #lr
    lr=[]
   #On tire aléatoirement n coordonnées aux hasards parmis cr
    while cpt <n:
        x=random.randint(0,(len(l2)-1))
        y=l2[x]
        lr.append (y)
        l2.remove (y)
        cpt+=1
    #Placement de la population]
    for (x,y) in lr:
    #on place la population
        ville2[x,y]=5        
    return ville2

def junkies (v):
    n=v.shape[0]
    m=v.shape[1]
    #Copie de ma ville
    v2=np.copy(v)
    #nb_junkies=0
    #nb_saines=0
    lr=[]
    x=0
    
    for i in range(0,n):
        for j in range (0, m):
            #si la case est un dealer arrêté
            if v2[i,j]==6:
                v2[i,j]=0   
    
    #Interaction dealer/policier/population
    for i in range(0,n):
        for j in range (0, m):
            #si la case est un dealer
            if v2[i,j]==3:
                #si il y a une policiere autour de lui
                if (v2[i+1,j]==5):
                    v2[i,j]=6
                elif (v2[i-1,j]==5):
                    v2[i,j]=6
                elif (v2[i,j-1]==5):
                    v2[i,j]=6
                elif (v2[i,j+1]==5):
                    v2[i,j]=6
                else :
                    #si il y a une personne saine
                    nb_aleatoire=random.randint(0,1)
                    if nb_aleatoire==0:
                        if (v2[i+1,j]==2):
                            v2[i+1,j]= 4
                        if (v2[i-1,j]==2):
                            v2[i-1,j]= 4
                        if (v2[i,j-1]==2):
                            v2[i,j-1]= 4
                        if (v2[i,j+1]==2):
                            v2[i,j+1]= 4                    

    #Déplacement de la population
    for i in range(0,n):
        for j in range (0, m):
            #si la case est une personne saine
            if v2[i,j]==2:
                #on regarde les chemins possibles que peut prendre la personne
                if (i!=n-1 and j!=m-1):
                    if (v2[i+1,j]==0):
                        lr.append((i+1,j))
                    if (v2[i-1,j]==0) and (i!=0):
                        lr.append((i-1,j))
                    if (v2[i,j+1]==0):
                        lr.append((i,j+1))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))
 
                elif (i==n-1 and j==m-1) :
                    if (v2[i-1,j]==0):
                        lr.append((i-1,j))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))
                elif (i==n-1):
                    if (v2[i-1,j]==0) and (i!=0):
                        lr.append((i-1,j))
                    if (v2[i,j+1]==0):
                        lr.append((i,j+1))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))
                else : 
                    if (v2[i+1,j]==0):
                        lr.append((i+1,j))
                    if (v2[i-1,j]==0) and (i!=0):
                        lr.append((i-1,j))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))     
                #on regarde si la liste n'est pas vide
                if ((len (lr))!=0):
                    #si c'est le cas, on tire une valeur x<= nombre de chemin
                    x=random.randint(0,len(lr)-1)
                    #déplacement case par case
                    if (x==0):
                        v2[i,j]=0
                        v2[lr[x]]=7
                    if (x==1):
                        v2[i,j]=0
                        v2[lr[x]]=7
                    if (x==2):
                        v2[i,j]=0
                        v2[lr[x]]=7
                    if (x==3):
                        v2[i,j]=0
                        v2[lr[x]]=7
                lr = []

    #Déplacement des junkies
    for i in range(0,n):
        for j in range (0, m):
            #si la case est un junkie
            if v2[i,j]==4:
                #on regarde les chemins possibles que peut prendre le junkie
                if (i!=n-1 and j!=m-1):
                    if (v2[i+1,j]==0):
                        lr.append((i+1,j))
                    if (v2[i-1,j]==0) and (i!=0):
                        lr.append((i-1,j))
                    if (v2[i,j+1]==0):
                        lr.append((i,j+1))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))
 
                elif (i==n-1 and j==m-1) :
                    if (v2[i-1,j]==0):
                        lr.append((i-1,j))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))
                elif (i==n-1):
                    if (v2[i-1,j]==0) and (i!=0):
                        lr.append((i-1,j))
                    if (v2[i,j+1]==0):
                        lr.append((i,j+1))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))
                else : 
                    if (v2[i+1,j]==0):
                        lr.append((i+1,j))
                    if (v2[i-1,j]==0) and (i!=0):
                        lr.append((i-1,j))
                    if (v2[i,j-1]==0) and (j!=0):
                        lr.append((i,j-1))     
                #on regarde si la liste n'est pas vide
                if ((len (lr))!=0):
                    #si c'est le cas, on tire une valeur x<= nombre de chemin
                    x=random.randint(0,len(lr)-1)
                    #déplacement case par case
                    if (x==0):
                        v2[i,j]=0
                        v2[lr[x]]=8
                    if (x==1):
                        v2[i,j]=0
                        v2[lr[x]]=8
                    if (x==2):
                        v2[i,j]=0
                        v2[lr[x]]=8
                    if (x==3):
                        v2[i,j]=0
                        v2[lr[x]]=8
                lr = []      
                
    #Déplacement des policiers
    for i in range(0,n):
        for j in range (0, m):
            #si la case est un policier
            if v2[i,j]==5:
                
                
                #on regarde les chemins possibles que peut prendre la personne
                #on regarde les chemins possibles que peut prendre la personne
                #On regarde si il y a un dealer sur sa colonne
                for k in range(0,n):
                    #Si il y en a un
                    if v2[k,j]==3 and v2[i,j]==5:
                            #Si il est en-dessous du policier et que la case est vide
                           if k>i and v2[i+1,j]==0:
                               #le policier se déplace
                              v2[i+1,j]=9
                              v2[i,j]=0
                            #Sinon le dealer est au-dessus et on vérifie que le policier peut se déplacer
                           elif k<i and v2[i-1,j]==0:
                              v2[i-1,j]=9
                              v2[i,j]=0
                #Si le policier ne c'est pas déplacé
                if v2[i,j]==5:
                    for k in range(0,m):
                        if v2[i,k]==3 and v2[i,j]==5:
                           if k>j and v2[i,j+1]==0:
                              v2[i,j+1]=9
                              v2[i,j]=0
                           elif k< j and v2[i,j-1]==0:
                              v2[i,j-1]=9
                              v2[i,j]=0
    
                              
                              
                              
                if v2[i,j]==5:                                                                                
                    if (i!=n-1 and j!=m-1):
                        if (v2[i+1,j]==0):
                            lr.append((i+1,j))
                        if (v2[i-1,j]==0) and (i!=0):
                            lr.append((i-1,j))
                        if (v2[i,j+1]==0):
                            lr.append((i,j+1))
                        if (v2[i,j-1]==0) and (j!=0):
                            lr.append((i,j-1))
         
                    elif (i==n-1 and j==m-1) :
                        if (v2[i-1,j]==0):
                            lr.append((i-1,j))
                        if (v2[i,j-1]==0) and (j!=0):
                            lr.append((i,j-1))
                    elif (i==n-1):
                        if (v2[i-1,j]==0) and (i!=0):
                            lr.append((i-1,j))
                        if (v2[i,j+1]==0):
                            lr.append((i,j+1))
                        if (v2[i,j-1]==0) and (j!=0):
                            lr.append((i,j-1))
                    else : 
                        if (v2[i+1,j]==0):
                            lr.append((i+1,j))
                        if (v2[i-1,j]==0) and (i!=0):
                            lr.append((i-1,j))
                        if (v2[i,j-1]==0) and (j!=0):
                            lr.append((i,j-1))     
                    #on regarde si la liste n'est pas vide
                    if ((len (lr))!=0):
                        #si c'est le cas, on tire une valeur x<= nombre de chemin
                        x=random.randint(0,len(lr)-1)
                        #déplacement case par case
                        if (x==0):
                            v2[i,j]=0
                            v2[lr[x]]=9
                        if (x==1):
                            v2[i,j]=0
                            v2[lr[x]]=9
                        if (x==2):
                            v2[i,j]=0
                            v2[lr[x]]=9
                        if (x==3):
                            v2[i,j]=0
                            v2[lr[x]]=9
                    lr = []
                    
    #on replace la population, les junkies puis les policiers
    for i in range(0,n):
        for j in range (0, m):
            if (v2[i,j]==7):
                v2[i,j]=2
           
    for i in range(0,n):
        for j in range (0, m):
            if (v2[i,j]==8):
                v2[i,j]=4
                
    for i in range(0,n):
        for j in range (0, m):
            if (v2[i,j]==9):
                v2[i,j]=5
                
    return v2

#Cette fonction permet d'obtenir la derniere frame au moment où tous les dealers sont arrêtés
def stadefinal (v):
  while 3 in v:
       v = junkies(v)
  return v
  
villei = ville(0.1,0.5,0.01)
villej = junkies(villei)
villef = stadefinal(villei)

print("Ville initial:\n",villei)
print("Ville premier pas:\n",villej)
print("Ville final sans dealer:\n",villef)

#3 - Analyse du modèle
def pourcentage_de_junkie (v):
    n=v.shape[0]
    m=v.shape[1]
    junkie=0
    population=0
    for i in range(0,n):
        for j in range (0, m):
            if v[i,j]==4:
                junkie+=1
            if v[i,j]==2 or v[i,j]==4:
                population+=1
    return junkie/population
    
print ("Junkie/Population total (hors policier et dealer):",pourcentage_de_junkie(villef))

#p = Densité de dealer (ex: si p = 100%, il y a que des dealers à la place des routes...)
#p2 = Densité de population
#p3 = Densité de policiers
def analyse (p,p2,p3,n):
    cpt=0
    x=0
    y=0
    #lr:list[int]
    lr=[]
    while cpt<n:
        cpt+=1
        #Génération d'une ville
        ville1 = ville (p,p2,p3)
        ville2 = stadefinal(ville1)
        #junkie sur le nombre total
        ville3=pourcentage_de_junkie (ville2)
        lr.append(ville3)
        x=x+ville3
    for a in lr:
        y=(y+(a-(x/n))**2)
    Variance = y/n
    Ecart_type = math.sqrt(y/n)
    Moyenne= x/n
    print("Variance:",Variance)
    print("Ecart-type:",Ecart_type)
    print("Moyenne:",Moyenne)
    return (Moyenne)

print("---------------------------------------------------------------------------------------")
print ("Analyse de junkies/population sur 10 villes de 10*10 avec\nP1% de dealer,P2% popuplation,P3% policier",analyse (0.01,0.2,0.01,10))
print("---------------------------------------------------------------------------------------")

#f = frame voulu
def analyse2 (p,p2,p3,n,f):
    cpt=0
    cpt2=0
    x=0
    y=0
    #lr:list[int]
    lr=[]
    while cpt<n:
        cpt+=1
        #Génération d'une ville
        ville1 = ville (p,p2,p3)
        ville2 = junkies(ville1)
        #Frame voulu pour l'analyse
        while (cpt2<f):
            ville2=junkies(ville2)
            cpt2=cpt2+1
        cpt2=0
        #junkie sur le nombre total
        ville3=pourcentage_de_junkie (ville2)
        lr.append(ville3)
        x=x+ville3
    for a in lr:
        y=(y+(a-(x/n))**2)
    Variance = y/n
    Ecart_type = math.sqrt(y/n)
    Moyenne= x/n
    print("Variance:",Variance)
    print("Ecart-type:",Ecart_type)
    print("Moyenne:",Moyenne)
    return (Moyenne)

#print("---------------------------------------------------------------------------------------")
#print ("Analyse de junkies/population sur 10 villes de 10*10 avec\nP1% de dealer,P2% popuplation,P3% policier",analyse2 (0.01,0.2,0.01,10,5))
#print("---------------------------------------------------------------------------------------")

#Graphique représentant la moyenne
import matplotlib.pyplot as plt
#nombre de simulation voulu
n=5
#Densité de dealer
p=0.01
#p2 = Densité de population
p2=0.5
#p3 = Densité de policiers
p3=0.01
#f = Image au bout de f pas

x = np.linspace(0,200,200)
y = [analyse2(p,p2,p3,n,f) for f in x]
plt.plot(x,y,'ro')
plt.show()
#pour obtenir un Graphique représentant la variance ou l'écart-type, il suffit de changer return (Moyenne) de la fonction analyse
#par return(Ecart_type) ou return (Variance)

#from matplotlib import pyplot
from matplotlib import colors
import matplotlib.animation as animation
    
cmap = colors.ListedColormap(['black','gray','green','red','purple','blue','orange'])
                      
import matplotlib.pyplot as plt
size = villei.shape
dpi = 72
figsize= size[1]/float(dpi),size[0]/float(dpi)
fig = plt.figure(figsize = (100,100), dpi = dpi, facecolor = "white")
fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon = False)
im=plt.imshow(villei, interpolation = 'nearest', cmap=cmap,vmin=0,vmax=6)
plt.xticks([]), plt.yticks([])

def update(*args):
   global villei
   #Variable
   while 3 in villei:
       villei = junkies(villei)
       im.set_array(villei)
       return im

ani = animation.FuncAnimation(fig, update, frames=range(20), interval=50)
plt.show() 