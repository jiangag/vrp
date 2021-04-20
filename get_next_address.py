from model import create_data_model
from solver import run_solver


""" Get vehicles routes & Get next address"""

def get_next_address(vehicle_num: int, current_postalCode: int):

# Get vehicles routes

    # user input the average no. of parcels delivered per location
    demand = 25

    # users input the max no. of parcels one vehicle can deliver per day
    vehicle_capacity = 250

    # prepare data for solver
    data, df = create_data_model(demand, vehicle_capacity)

    # run solver and get the vehicles_routes
    vehicles_routes = run_solver(data)   


# Get next address

# input vehicle no. and postal code for current address, return postal code for next location
# e.g. sequence for vehicle 5 ...560529->560324->560153->761512->762432->791456->550201

    try:
        location_num = df[df['POSTAL']==current_postalCode]['LOCATION_NUM'].values[0] #e.g. 61
    except:
        message = 'You have given wrong vehicle number or postal code'
        return message

    position = vehicles_routes[vehicle_num].index(location_num) #3

    if position == len(vehicles_routes[vehicle_num]) -1: #550201
        message = 'Current address is your last one, thank you'

    else: 
        remain_locations = len(vehicles_routes[vehicle_num]) -1 - position
        next_location_num = vehicles_routes[vehicle_num][position+1] #59
        next_postalCode = df[df['LOCATION_NUM']==next_location_num]['POSTAL'].values[0] 
        message = 'There are '+str(remain_locations)+' more postal code to go and the next one is '+str(next_postalCode)

    return message

# for testing purpose
if __name__ == '__main__':
    next_address = get_next_address(5,550201)
    print(next_address)