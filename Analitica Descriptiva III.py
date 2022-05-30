#!/usr/bin/env python
# coding: utf-8

# # #Asignación 2 - Analitica Descriptiva III
# 

# Importamos las librerias a utilizar con su alias

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


store_data = pd.read_csv("C:/Users/TECH-G/Desktop/Stores.csv" , index_col = 0)


# In[10]:


store_data


# In[11]:


store_data.count()


# El "Describe" se utiliza para obtener analisis estadisticos del dataset, aqui se mide el total, moda, media aritmetica, desviacion estandar, valor mini y el maximo de estos.

# In[13]:


store_data.describe()


# Para una rapida visualizacion les muestro las primeras diez columnas con la ayuda del "HEAD"

# In[14]:


store_data.head(10)


# Como podran observar en el resumen de datos que no faltan valores, por lo que no debemos preocuparnos por eso. Podemos ver en la descripción anterior que tenemos datos para 896 tiendas. El valor medio de cada variable se da en la fila titulada "media". A continuación, nos gustaría saber cómo se afectan entre sí las diferentes variables.
# 
# En primer lugar, tengo curiosidad por algo. En nuestra tabla de resumen, podemos ver que una tienda tiene un recuento diario de clientes de solo 10. Interesante. Veamos cómo se ve el resto de los datos de esa tienda.

# In[15]:


store_data[store_data['Daily_Customer_Count'] == 10]


# Me parece interesante que una tienda con un promedio de solo 10 clientes diarios realiza más ventas que casi el 25% por ciento de las otras tiendas. Esta tienda en particular, en comparación con otras, tampoco tiene muchos artículos, esa podría ser una razon de sus pocas visitas.

# In[20]:


store_data[store_data['Store_Sales']== 116320]


# In[17]:


corrmat = store_data.corr()
plt.subplots(figsize = (5,5))
sns.heatmap(corrmat, square = True)


# Con esto podemos ver una fuerte correlación entre el área de la tienda y los artículos disponibles. Por otro lado hay muy poca correlación entre los artículos disponibles y los clientes que visitan las tiendas diariamente.
# 

# In[18]:


x = store_data[['Items_Available']]
y = store_data[['Store_Area']]
_ = plt.figure(figsize=(12,8))  
_ = plt.scatter(x , y)
_ = plt.xlabel('Items Available')
_ = plt.ylabel('Sales')
_ = plt.xticks(np.arange(0, 2800 , step = 200))  
_ = plt.yticks(np.arange(0 ,2400 , step = 200))
plt.plot()


# Entre las variables "Items Available" y "Store_Area" existe colinelidad, lo cual significa que estas dos variables estan altamente relacionadas.
# 

# In[19]:


x = store_data[['Items_Available']]
y = store_data[['Store_Sales']]
_ = plt.figure(figsize=(12,8))  
_ = plt.scatter(x , y)
_ = plt.xlabel('Items Available')
_ = plt.ylabel('Sales')
_ = plt.xticks(np.arange(0, 2800 , step = 200))  
_ = plt.yticks(np.arange(0 ,120000 , step = 20000), ['20K' , '40K' , '60K' , '80K' , '100K' , '120K']) 


# Efectivamente el mapa de calor me mostraba el resultado tal cual. Al parecer algunas tiendas almacenan articulos que se venden mas rapido que otros. En este caso lo que se necesita hacer es ofrecer ciertas facilidades con aquellos productos que no tienen muchas ventas. 
# 
# 

# In[ ]:




