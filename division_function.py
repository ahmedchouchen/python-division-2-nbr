def division(a,b):

  if (a.isnumeric() & b.isnumeric()):
    a=float(a)
    b=float(b)
    if b==0 :
        result = " le deuxieme  nombre ne peux pas etre Zero "
    else :
        result = a / b
    
  else:
    
    result = "SVP donner deux nombres  valides "
    

  return result
