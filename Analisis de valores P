#!/usr/bin/env python
# coding: utf-8

# # Analitica Descriptiva-Asignacion 3
# 
# Estudiante: Euri Aponte /
# Matrricula: 2021-1198

# In[5]:


import pandas as pd


# Importemos nuestros datos y comprobemos la estructura de datos en Python. Como de costumbre, importamos los datos utilizando la función read_csv en la biblioteca de pandas y utilizamos la función de información para comprobar la estructura de datos.
# 
# Importar datos y comprobar la estructura de datos antes de ejecutar el modelo

# In[6]:


bankloan=pd.read_csv("/Users/euriaponte/Downloads/BANK LOAN KNN.csv")
bankloan.info() 


# 
# La edad debe ser una variable categórica y, por lo tanto, debe convertirse en un tipo de categoría. Si no se convierte en un tipo de categoría, Python lo interpretará como una variable numérica, lo cual no es correcto, ya que estamos considerando grupos de edad en nuestro modelo
# 
# ## Cambiar la variable "EDAD" a categórica

# In[7]:


bankloan['AGE']=bankloan['AGE'].astype('category')
bankloan.info() 


# 
# La regresión logística utiliza la función de enlace logit. Al igual que con el modelo de regresión lineal, las variables dependientes e independientes se separan utilizando el signo de tilde, y las variables independientes están separadas por el signo más.
# 
# Así que veamos qué variables independientes afectan a los clientes que se convierten en defectuosos. Después de ajustar el modelo de regresión logística, llevamos a cabo pruebas de hipótesis individuales para identificar variables significativas. A continuación, utilizamos la función de resumen en el objeto modelo para obtener una salida detallada. Las variables cuyo valor de P es inferior a 0,05 se consideran estadísticamente significativas. Dado que el valor p es < 0,05 para Employ, Address, Debtinc y Creddebt, estas variables independientes son significativas.

# ## Logit() ajusta un modelo de regresión logística a los datos.

# In[8]:


import statsmodels.formula.api as smf
 


# In[9]:


riskmodel = smf.logit(formula = 'DEFAULTER ~ AGE + EMPLOY + ADDRESS + DEBTINC + CREDDEBT + OTHDEBT', data = bankloan).fit()


# ## Summary() genera un resumen detallado del modelo.

# In[30]:


riskmodel.summary() 


# ## Interpretación
# 
# Dado que el valor p es <0,05 para Employ, Address, Debting,
# Creddebt estas variables independientes son significativas.

# # --------------------

# Una vez finalizadas las variables que se conservarán, volvemos a ejecutar el modelo de regresión logística binaria incluyendo solo las variables significativas. Una vez más, la salida de la función de resumen proporciona los coeficientes revisados para el modelo.
# 
# 

# In[32]:


riskmodel = smf.logit(formula = 'DEFAULTER ~ EMPLOY + ADDRESS + DEBTINC + CREDDEBT', data = bankloan).fit()


# In[33]:


riskmodel.summary() 


# En este resultado, todas las variables independientes son estadísticamente significativas, por lo que este modelo se puede utilizar para un diagnóstico posterior.

# In[ ]:




