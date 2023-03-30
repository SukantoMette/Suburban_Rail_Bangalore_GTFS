"""
    This file is used to create the complete set necessary GTFS files for metro, it doesn't contain transfers file
    It contains various functions like
    -> create_stops_file
    -> create_trips_file
    -> create_stoptimes_file
    -> create_route_txt_file
    These functions do exactly what their name suggests
    Finally there is main function which runs all these functions simultaneously
"""

from collections import defaultdict

import datetime as dt
import numpy as np
import pandas as pd
import pickle
import haversine as hs
import math


def create_stops_file():
    """
        This Function creates stops.txt file
    """

    stops_txt = defaultdict(list)

    stops_txt['stop_id'] = ['S_1', 'S_2', 'S_3', 'S_4', 'S_5', 'S_6', 'S_7', 'S_8', 'S_9', 'S_10', 'S_11', 'S_12', 'S_13', 'S_14', 'S_15',
                            'M_1', 'M_2', 'M_3', 'M_4', 'M_5', 'M_6', 'M_7', 'M_8', 'M_9', 'M_10', 'M_11', 'M_12', 'M_13', 'M_14',
                            'P_1', 'P_2', 'P_3', 'P_4', 'P_5', 'P_6', 'P_7', 'P_8', 'P_9', 'P_10', 'P_11', 'P_12', 'P_13', 'P_14',
                            'K_1', 'K_2', 'K_3', 'K_4', 'K_5', 'K_6', 'K_7', 'K_8', 'K_9', 'K_10', 'K_11', 'K_12', 'K_13', 'K_14', 'K_15', 'K_16', 'K_17', 'K_18', 'K_19']

    stops_txt['stop_name'] = ['KSR Bengaluru City', 'Srirampura', 'Malleswaram', 'Yeshwantpura', 'Muthyalanagar', 'Lottegollahalli', 'Kodigehalli', 'Judicial layout', 'Yelahanka', 'Nitte Meenakshi', 'Bettahalasuru', 'Doddajala', 'Airport Trumpet', 'Airport KIADB', 'Devanahalli',
                              'Baiyyappanahalli Panel', 'Kasturi Nagar', 'Sevanagar', 'Banaswadi', 'Kaveri Nagar', 'Nagavara', 'Kanakanagar', 'Hebbal', 'Lottegollahalli', 'Yeshwantpura', 'Jalahalli', 'Shettyhalli', 'Myadarahalli', 'Chikkabanavara',
                              'Kengeri', 'RV college', 'Jnanabharathi', 'Nayandahalli', 'Krishnadevaraya', 'Jagajeevanramnagar', 'KSR Bengaluru City', 'Kumara Park', 'Bengaluru Cantt', 'Bengaluru East', 'Baiyyappanahalli', 'Krishnarajapuram', 'Hoodi', 'White Field',
                              'Heelalige', 'Bommasandra', 'Singena Agrahara', 'Huskuru', 'Ambedkar Nagar', 'Carmelaram', 'Belandur Road', 'Marathahalli', 'Kaggadasapura', 'Benniganahalli', 'Channasandra', 'Horamavu', 'Hennur', 'Tanisandra', 'Hegde Nagara', 'Jakkur', 'Yelahanka', 'Muddenahalli', 'Rajankunte']

    stops_txt['(lat,lon)'] = [(12.97847836, 77.56951936), (12.99566139, 77.56691292), (13.0004259, 77.56359061), (13.0237486, 77.55171098), (13.03862155, 77.55869141), (13.04363044, 77.56315638), (13.06305805, 77.57595153), (13.07754266, 77.5907039), (13.1049859, 77.59179355), (13.13022671, 77.58642991), (13.16622993, 77.60445251), (13.18343497, 77.65221226), (13.19858623, 77.65863363), (13.21066799, 77.67606418), (13.24750745, 77.70539292),
                              (12.99527113, 77.66368767), (13.00395004, 77.6558045), (13.00547767, 77.64418068), (13.00589578, 77.62819033), (13.01876035, 77.62343552), (13.02532007, 77.62145541), (13.03822834, 77.61025379), (13.0425652, 77.58621339), (13.04363044, 77.56315638), (13.0237486, 77.55171098), (13.04392807, 77.53980484), (13.06753862, 77.51584263), (13.06916319, 77.51177351), (13.07486296, 77.50579004),
                              (12.91736756, 77.48404971), (12.92399449, 77.49480009), (12.9351539, 77.51102127), (12.94171027, 77.52130292), (12.95809809, 77.53947365), (12.96604618, 77.54969883), (12.97847836, 77.56951936), (12.99185852, 77.58027682), (12.99372249, 77.5980427), (13.00135884, 77.61821308), (12.9913663, 77.65322494), (13.00081797, 77.67476076), (12.99614041, 77.71864259), (12.99598053, 77.76154357),
                              (12.81332561, 77.71113936), (12.82386163, 77.71233959), (12.83439467, 77.71280623), (12.85803089, 77.71061455), (12.89860076, 77.70674417), (12.90741427, 77.70591556), (12.93725962, 77.70731121), (12.9565408, 77.70467505), (12.98366223, 77.67987307), (12.99381035, 77.66458924), (13.00966511, 77.66344048), (13.03084447, 77.65479458), (13.03772253, 77.64917228), (13.05609393, 77.63648965), (13.06516262, 77.62643252), (13.07111745, 77.61961356), (13.1049859, 77.59179355), (13.14529054, 77.57063946), (13.17468611, 77.56546953)]

    stops_txt = pd.DataFrame.from_dict(stops_txt)
    stops_txt['stop_lat'] = stops_txt['(lat,lon)'].apply(lambda x: x[0])
    stops_txt['stop_lon'] = stops_txt['(lat,lon)'].apply(lambda x: x[1])
    stops_txt = stops_txt.drop(columns='(lat,lon)')

    stops_txt.to_csv('stops.csv', index=False)


def create_trips_file(trips_frequency_table, route_id_str: str):
    """
        This function is used to create the trips table which is later used as input for another function
        and is also used to create trips.txt file

        Args :
            trips_frequency_table : DataFrame consisting of the trips frequency which is accessed from excel file
            route_id_str : A string which is used for giving name convention to the trip_id and route_id

        Returns :
            trips_table : A DataFrame containing trip_id, route_id and arrival time

    """

    # making necessary column additions to the trip frequeny DataFrame

    trips_frequency_table['frequency'] = trips_frequency_table['frequency'].apply(lambda x: dt.timedelta(minutes=x))
    trips_frequency_table['end time'] = trips_frequency_table['end time'].apply(lambda x: dt.datetime.combine(dt.date.today(), x))
    trips_frequency_table['start time'] = trips_frequency_table['start time'].apply(lambda x: dt.datetime.combine(dt.date.today(), x))

    trips_frequency_table['time difference'] = trips_frequency_table['end time'] - trips_frequency_table['start time']
    trips_frequency_table['number of trains'] = np.ceil(trips_frequency_table['time difference'] / trips_frequency_table['frequency'])

    trips_frequency_table['number of trains'] = trips_frequency_table['number of trains'].astype('int64')

    # Creating dictionary trips_table, which after making changes will be converted to DataFrame
    # print(trips_frequency_table["number of trains"].tail())
    trips_table = defaultdict(list)
    index_count = 0

    # adding necessary values inside the columns

    for row in trips_frequency_table.itertuples():

        start_time = row[1]
        curr_index = index_count

        for i in range(curr_index, row[5] + curr_index):
            trips_table['trip_id'].append(f'{route_id_str}_{i + 1}')
            trips_table['route_id'].append(route_id_str)
            trips_table['arrival time'].append(start_time)
            start_time = start_time + row[3]
            index_count += 1

    trips_table = pd.DataFrame.from_dict(trips_table)

    return trips_table


def create_stoptimes_file(stop_times_txt, trips_table: pd.DataFrame, line_id_str: str,route_id: str, metro_line_time_diiference_between_stops: list, start_point_of_trip_file: int):
    """
        This Function is used to create the stopstimes.txt file

        Args :
            trips_table : DataFrame gotten from create_trips_file function
            line_id_str : String containing the metro line initial, used for naming purposes
            metro_line_time_diiference_between_stops : A list constaining the time difference between consecutive stops

        Returns :
            stop_times_txt : A DataFrame which will be converted to stoptimes.txt file

    """

    # making necessary changes to the time difference list
    metro_line_time_diiference_between_stops.append(0)
    metro_line_time_diiference_between_stops = [dt.timedelta(minutes=val) for val in metro_line_time_diiference_between_stops]

    # Filling the stop times dictionary with relevant data and converting it to DataFrame

    for row in range(start_point_of_trip_file,trips_table.shape[0]):

        arrival_time = trips_table["arrival time"].iloc[row]

        for index in range(len(metro_line_time_diiference_between_stops)):

            stop_times_txt['trip_id'].append(trips_table["trip_id"].iloc[row])
            stop_times_txt['arrival_time'].append(arrival_time)
            arrival_time = arrival_time + metro_line_time_diiference_between_stops[index]
            if route_id in ['SK', 'MB', 'PK', 'KH']:
                stop_times_txt['stop_id'].append(f'{line_id_str}_{index + 1}')
            else:
                stop_times_txt['stop_id'].append(f'{line_id_str}_{len(metro_line_time_diiference_between_stops) - (index)}')
            stop_times_txt['sequence_id'].append(index)



def create_route_txt_file():
    """
        This Function is used to create route.txt file
        Add new routes to the list below manually and then run this function to update the route.txt file
    """

    routes_dict = defaultdict(list)

    routes_dict['route_id'] = ['SK', 'SD', 'MB', 'MC', 'PK', 'PW', 'KH', 'KR']
    routes_dict['route_short_name'] = ['Sampige KSR Bengaluru City',
                                       'Sampige Devanahalli',
                                       'Mallige Baiyyappanahalli Panel',
                                       'Mallige Chikkabanavara',
                                       'Parijaata Kengeri',
                                       'Parijaata White Field',
                                       'Kanaka Heelalige',
                                       'Kanaka Rajankunte']
    routes_dict['route_long_name'] = ['Sampige KSR Bengaluru City to Devanahalli',
                                       'Sampige Devanahalli to KSR Bengaluru City',
                                       'Mallige Baiyyappanahalli Panel to Chikkabanavara',
                                       'Mallige Chikkabanavara to Baiyyappanahalli Panel',
                                       'Parijaata Kengeri to White Field',
                                       'Parijaata White Field to Kengeri',
                                       'Kanaka Heelalige to Rajankunte',
                                       'Kanaka Rajankunte to Heelalige']
    routes_dict['route_desc'] = [-1] * 8
    routes_dict['route_type'] = [1] * 8

    route_txt = pd.DataFrame.from_dict(routes_dict)

    route_txt.to_csv('route.csv', index=False)

def time_gap():
    with open("kanaka_inter_station_distance.pkl", 'rb') as file:
        inter_station_distance = pickle.load(file)
    print(inter_station_distance)
    time_gap = [math.ceil((x/33)*60) for x in inter_station_distance]
    print(time_gap)
    print(len(time_gap))
    # reverse
    time_gap = time_gap[::-1]
    print(time_gap)
    print(len(time_gap))
    with open("KR_time_gap.pkl", 'wb') as pickle_file:
        pickle.dump(time_gap, pickle_file)
    # routes_dict['route_id'] = ['SK', 'SD', 'MB', 'MC', 'PK', 'PW', 'KH', 'KR']

def main():
    """
        This main function creates the stoptimes.txt file and trips.txt file

        Args :
            TRIPS_FREQUENCY_FILE_LOCATION : string containing the excel file location
            ROUTE_ID : Used for nomencalture purpose
            METRO_LINE_ID : Used for nomencalture purpose
            CONSECUTIVE_STATION_TIME_DIFFERENCE : excel file containing the list containing the
                                                  consecutive station time difference for the particular metro line
            NUMBER_OF_ROUTES : int containing total routes

        Example input :
            NUMBER_OF_ROUTES = 4
            (The For loop runs 4 times in the following manner)

                TRIPS_FREQUENCY_FILE_LOCATION = 'trips time and frequency 1.xlsx'
                ROUTE_ID : 'PB'
                METRO_LINE_ID : 'P'
                CONSECUTIVE_STATION_TIME_DIFFERENCE = 'consecutive station time difference 1.xlsx'

                TRIPS_FREQUENCY_FILE_LOCATION = 'trips time and frequency 2.xlsx'
                ROUTE_ID : 'PK'
                METRO_LINE_ID : 'P'
                CONSECUTIVE_STATION_TIME_DIFFERENCE = 'consecutive station time difference 2.xlsx'

                TRIPS_FREQUENCY_FILE_LOCATION = 'trips time and frequency 3.xlsx'
                ROUTE_ID : 'GN'
                METRO_LINE_ID : 'G'
                CONSECUTIVE_STATION_TIME_DIFFERENCE = 'consecutive station time difference 3.xlsx'

                TRIPS_FREQUENCY_FILE_LOCATION = 'trips time and frequency 4.xlsx'
                ROUTE_ID : 'GS'
                METRO_LINE_ID : 'G'
                CONSECUTIVE_STATION_TIME_DIFFERENCE = 'consecutive station time difference 5.xlsx'

    """

    # creating stops file
    create_stops_file()

    # creating routes file
    create_route_txt_file()

    # Creating trips file for different routes and combining them to form trips.txt
    trips_table = defaultdict(list)
    trips_table['trip_id']
    trips_table['route_id']
    trips_table['arrival time']

    stop_times_txt = defaultdict(list)

    trips_txt = pd.DataFrame.from_dict(trips_table)

    NUMBER_OF_ROUTES = int(input('Enter the Number of Routes'))

    start_point_of_trip_file = 0

    for index in range(NUMBER_OF_ROUTES):
        print(f'Route {index+1}')

        TRIPS_FREQUENCY_FILE_LOCATION = input('Enter trips frequency excel file location')
        ROUTE_ID = input('Enter Route_id')
        METRO_LINE_ID = input('Enter metro line id')
        CONSECUTIVE_STATION_TIME_DIFFERENCE = input('Enter consecutive station time difference excel file location')

        file = open(CONSECUTIVE_STATION_TIME_DIFFERENCE, 'rb')
        CONSECUTIVE_STATION_TIME_DIFFERENCE = pickle.load(file)
        file.close()

        trips_frequency_table = pd.read_excel(rf'{TRIPS_FREQUENCY_FILE_LOCATION}')

        trips_txt = pd.concat([trips_txt, create_trips_file(trips_frequency_table, ROUTE_ID)], ignore_index=True)

        create_stoptimes_file(stop_times_txt,
                              trips_table=trips_txt,
                              line_id_str=METRO_LINE_ID,
                              route_id=ROUTE_ID,
                              metro_line_time_diiference_between_stops=CONSECUTIVE_STATION_TIME_DIFFERENCE,
                              start_point_of_trip_file=start_point_of_trip_file)
        start_point_of_trip_file = trips_txt.shape[0]

    # Creating stoptimes.txt
    stop_times_txt = pd.DataFrame.from_dict(stop_times_txt)
    # stop_times_txt['arrival_time'] = stop_times_txt['arrival_time'].apply(lambda x: x.time())
    stop_times_txt['departure_time'] = stop_times_txt['arrival_time']

    trips_txt = trips_txt.drop(columns='arrival time')

    # creating the trips.txt and stoptimes.txt file in csv format
    trips_txt.to_csv('trips.txt', index=False)
    stop_times_txt.to_csv('stoptimes.txt', index=False)



if __name__ == "__main__":
    main()

    # routes_dict['route_id'] = ['SK', 'SD', 'MB', 'MC', 'PK', 'PW', 'KH', 'KR']



# sampige
# inter_station_distance_cumm = [0]+[1.45, 2.85, 5.74, 8.32, 10.02, 12.78, 14.96, 18.38, 21.33, 26.12, 30.070, 34.22, 36.15, 41.40]
# mallige
# inter_station_distance_cumm = [0]+[1.14, 3.16, 4.17, 5.47, 7.17, 8.69, 11.63, 14.35, 17.135, 20.24, 21.46, 23.75, 25.010]
# parijaata
# inter_station_distance_cumm = [0]+[1.95, 3.65, 4.75, 7.55, 10.35, 12.11, 13.95, 16.90, 19.17, 23.28, 25.87, 30.65, 35.52]
# kanaka
# inter_station_distance_cumm = [0]+[1.48, 3.00, 5.00, 9.00, 10.40, 13.69, 15.85, 20.70, 22.650, 24.45, 26.10, 27.66, 30.960, 32.64, 33.91, 37.825, 42.73, 46.24]
# inter_station_distance = []
# for i in range(1, len(inter_station_distance_cumm)):
#     inter_station_distance.append(inter_station_distance_cumm[i] - inter_station_distance_cumm[i-1])
# print(inter_station_distance_cumm)
# print(len(inter_station_distance_cumm))
# print(inter_station_distance)
# print(len(inter_station_distance))
# with open('kanaka_inter_station_distance.pkl', 'wb') as pickle_file:
#     pickle.dump(inter_station_distance, pickle_file)



    # routes_dict['route_id'] = ['SK', 'SD', 'MB', 'MC', 'PK', 'PW', 'KH', 'KR']






    # df = pd.read_csv("kanaka_line.csv")
    # index = []
    # name = []
    # lat_lon = []
    # for row in range(df.shape[0]):
    #     index.append(f"K_{row+1}")
    #     name.append(df["kanaka_line"].iloc[row])
    #     lat_lon.append((df["lat"].iloc[row], df["lon"].iloc[row]))
    # print(index)
    # print(name)
    # print(lat_lon)



