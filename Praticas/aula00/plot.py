# Try running this program.
# Then change it to generate another subplot with the product of y1 and y2.

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

t = np.arange(0.0, 5.0, 0.11)  # try printing t

plt.subplot(3, 1, 1)
y1 = np.exp(-t)
plt.plot(t, y1, 'r')  # try 'g' or 'bo' or 'k+'

plt.subplot(3, 1, 2)
y2 = np.cos(2*np.pi*t)
plt.plot(t, y2, 'go-')

plt.subplot(3, 1, 3)
y3 = y1*y2
plt.plot(t, y3, 'b*-')

# XXXXXXXXXXXXXXXXXXXXXXXXXX
#    ALTERACOES QUE FIZ:
# XXXXXXXXXXXXXXXXXXXXXXXXXX

# CRIEI UMA NOVA COLUNA PARA FUNCAO
# ADICIONEI OUTRA FUNCAO A ESSA COLUNA ( A MULTIPLICAO DAS 2 FUNCOES FOI A MINHA 3 FUNCAO )
# MUDEI AS CORES PARA (RGB)
# ALTEREI TAMBEM A FORMA DO MOSTRADOR DA ULTIMA FUNCAO PARA ESTRELAS 

# ACHO QUE FOI ISTO QUE O STOR FEZ MAS EU NAO FIZ NA AULA (FIM ISTO VENDO NA NET COMO FUNCIONA A BIBLIOTECA)


plt.show()

