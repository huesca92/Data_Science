import numpy as np
import matplotlib.pyplot as plt
def estimate_b0_b1(x, y):
  n = np.size(x)
# obtenemos los promedios de X y Y
  m_x, m_y = np.mean(x), np.mean(y)
# Calcular sumatoria de XY y mi sumatoria de XX
  sumatoria_xy = np.sum((x - m_x) * ( y - m_y))
  sumatoria_xx = np.sum((x-m_x)**2)
#coeficientes de regresión
  b_1 = sumatoria_xy/sumatoria_xx
  b_0 = m_y - b_1*m_x
  return(b_0,b_1)



#Funcion de graficado
def plot_regression(x,y,b):
  plt.scatter(x,y,color = "g", marker= "o", s= 30)
  y_pred = b[0] + b[1]*x
  plt.plot(x, y_pred , color = "b")
#etiquetado

  plt.xlabel('x-Independiente')
  plt.ylabel('y-dependiente')
  plt.show()

#codigo MAIN
def main():
  #DATASET
  x=np.array([1,2,3,4,5])
  y = np.array([2,3,5,6,5])
  #OBTENEMOS b1 y b2
  b = estimate_b0_b1( x, y)
  print("Los valores b0 = {} , b1 = {}".format(b[0],b[1]))
  
  #aqui graficamos nuestra linea de regresión
  plot_regression(x,y,b)

if __name__ == "__main__":
  main()