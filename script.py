def ground_shipping(weight):
  if weight > 10:
    return(weight * 4.75) + 20
	elif weight > 6:
    return(weight * 4.00) + 20
	elif weight > 2:
		return(weight * 3.00) + 20
  else:
    return(weight * 1.50) + 20
 print(ground_shipping(8.4))
 
p_ground_shipping==125

def drone_shipping(weight)
	  if weight > 10:
    return(weight * 14.25)
	elif weight > 6:
    return (weight * 12.00)
	elif weight > 2:
		return (weight * 9.00)
  else:
    return (weight * 4.50)
print(drone_shipping(1.5))

def cheapest_shipping(4.8):
  if (ground_shipping < p_ground_shipping) and (drone_shipping < ground_shipping):
    print (drone_shipping(4.8))
  elif (ground_shipping < drone_shipping)
  	print (ground_shipping(4.8))
  else:
    print(p_ground_shipping)
  
  