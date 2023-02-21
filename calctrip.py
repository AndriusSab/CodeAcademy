from typing import Union

def calc_speed_average(distance_km: Union[float,int],  time_h: Union[float, int]) -> Union[float, int]:
    
    return distance_km / time_h

def calc_distance(speed_kmh: Union[float,int],  time_h: Union[float, int]) ->  Union[float, int]:
    
    return speed_kmh * time_h

def calc_time (distance_km: Union[float,int],  speed_kmh: Union[float, int]) ->  Union[float, int]:
    return distance_km / speed_kmh

if __name__ == "__main__":

     a = 500
     b = 20

average_speed = calc_speed_average(a, b)
trip_time = calc_time(a,b)
trip_distance = calc_distance (a,b)
print(f"Average speed is: {average_speed}, trip_time : {trip_time}, trip distance: {trip_distance}")