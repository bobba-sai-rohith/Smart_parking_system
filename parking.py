
def parking_slot_in(vehicle_type,car_list):
	while(1):
		key=0
		if(vehicle_type=="car"):
			for parking_i in car_list:
				if(car_list[parking_i]==0):
					car_list[parking_i]=1
					return parking_i
		elif(vehicle_type=="bike"):
			for parking_i in car_list:
				if(car_list[parking_i]==0 and str(parking_i)[0]=="E"):
					car_list[parking_i]=1
					return parking_i