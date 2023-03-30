import pandas as pd
import networkx as nx
import haversine as hs
import pickle

df = pd.read_csv("stops.txt")

def assign_fare(dis):
    if dis < 3:
        return 13
    elif ((dis >= 3) and (dis < 6)):
        return 20
    elif ((dis >= 6) and (dis < 9)):
        return 27
    elif ((dis >= 9) and (dis < 12)):
        return 29
    elif ((dis >= 12) and (dis < 15)):
        return 33
    elif ((dis >= 15) and (dis < 18)):
        return 37
    elif ((dis >= 18) and (dis < 21)):
        return 43
    elif ((dis >= 21) and (dis < 24)):
        return 47
    elif ((dis >= 24) and (dis < 27)):
        return 51
    elif ((dis >= 27) and (dis < 30)):
        return 53
    elif ((dis >= 30) and (dis < 33)):
        return 60
    elif ((dis >= 33) and (dis < 36)):
        return 63
    elif ((dis >= 36) and (dis < 39)):
        return 67
    elif ((dis >= 39) and (dis < 42)):
        return 71
    elif ((dis >= 42) and (dis < 45)):
        return 73
    elif ((dis >= 45) and (dis < 48)):
        return 80
    elif ((dis >= 48) and (dis < 51)):
        return 83
    elif ((dis >= 51) and (dis < 54)):
        return 87
    elif ((dis >= 54) and (dis < 57)):
        return 91
    elif ((dis >= 57) and (dis < 60)):
        return 93
    elif ((dis >= 60) and (dis < 63)):
        return 100


g = nx.Graph()
g.add_nodes_from(['S_1', 'S_2', 'S_3', 'S_4', 'S_5', 'S_6', 'S_7', 'S_8', 'S_9', 'S_10', 'S_11', 'S_12', 'S_13', 'S_14', 'S_15', 'M_1', 'M_2', 'M_3', 'M_4', 'M_5', 'M_6', 'M_7', 'M_8', 'M_9', 'M_10', 'M_11', 'M_12', 'M_13', 'M_14', 'P_1', 'P_2', 'P_3', 'P_4', 'P_5', 'P_6', 'P_7', 'P_8', 'P_9', 'P_10', 'P_11', 'P_12', 'P_13', 'P_14', 'K_1', 'K_2', 'K_3', 'K_4', 'K_5', 'K_6', 'K_7', 'K_8', 'K_9', 'K_10', 'K_11', 'K_12', 'K_13', 'K_14', 'K_15', 'K_16', 'K_17', 'K_18', 'K_19'])

g.add_edges_from([('S_1', 'S_2', {'weight': 1.45}), ('S_2', 'S_3', {'weight': 1.4000000000000001}), ('S_3', 'S_4', {'weight': 2.89}), ('S_4', 'S_5', {'weight': 2.58}), ('S_5', 'S_6', {'weight': 1.6999999999999993}), ('S_6', 'S_7', {'weight': 2.76}), ('S_7', 'S_8', {'weight': 2.1800000000000015}), ('S_8', 'S_9', {'weight': 3.419999999999998}), ('S_9', 'S_10', {'weight': 2.9499999999999993}), ('S_10', 'S_11', {'weight': 4.790000000000003}), ('S_11', 'S_12', {'weight': 3.9499999999999993}), ('S_12', 'S_13', {'weight': 4.149999999999999}), ('S_13', 'S_14', {'weight': 1.9299999999999997}), ('S_14', 'S_15', {'weight': 5.25})])
g.add_edges_from([('M_1', 'M_2', {'weight': 1.14}), ('M_2', 'M_3', {'weight': 2.0200000000000005}), ('M_3', 'M_4', {'weight': 1.0099999999999998}), ('M_4', 'M_5', {'weight': 1.2999999999999998}), ('M_5', 'M_6', {'weight': 1.7000000000000002}), ('M_6', 'M_7', {'weight': 1.5199999999999996}), ('M_7', 'M_8', {'weight': 2.9400000000000013}), ('M_8', 'M_9', {'weight': 2.719999999999999}), ('M_9', 'M_10', {'weight': 2.785000000000002}), ('M_10', 'M_11', {'weight': 3.104999999999997}), ('M_11', 'M_12', {'weight': 1.2200000000000024}), ('M_12', 'M_13', {'weight': 2.289999999999999}), ('M_13', 'M_14', {'weight': 1.2600000000000016})])
g.add_edges_from([('P_1', 'P_2', {'weight': 1.95}), ('P_2', 'P_3', {'weight': 1.7}), ('P_3', 'P_4', {'weight': 1.1}), ('P_4', 'P_5', {'weight': 2.8}), ('P_5', 'P_6', {'weight': 2.8}), ('P_6', 'P_7', {'weight': 1.7599999999999998}), ('P_7', 'P_8', {'weight': 1.8399999999999999}), ('P_8', 'P_9', {'weight': 2.9499999999999993}), ('P_9', 'P_10', {'weight': 2.270000000000003}), ('P_10', 'P_11', {'weight': 4.109999999999999}), ('P_11', 'P_12', {'weight': 2.59}), ('P_12', 'P_13', {'weight': 4.779999999999998}), ('P_13', 'P_14', {'weight': 4.8700000000000045})])
g.add_edges_from([('K_1', 'K_2', {'weight': 1.48}), ('K_2', 'K_3', {'weight': 1.52}), ('K_3', 'K_4', {'weight': 2.0}), ('K_4', 'K_5', {'weight': 4.0}), ('K_5', 'K_6', {'weight': 1.4000000000000004}), ('K_6', 'K_7', {'weight': 3.289999999999999}), ('K_7', 'K_8', {'weight': 2.16}), ('K_8', 'K_9', {'weight': 4.85}), ('K_9', 'K_10', {'weight': 1.9499999999999993}), ('K_10', 'K_11', {'weight': 1.8000000000000007}), ('K_11', 'K_12', {'weight': 1.6500000000000021}), ('K_12', 'K_13', {'weight': 1.5599999999999987}), ('K_13', 'K_14', {'weight': 3.3000000000000007}), ('K_14', 'K_15', {'weight': 1.6799999999999997}), ('K_15', 'K_16', {'weight': 1.269999999999996}), ('K_16', 'K_17', {'weight': 3.9150000000000063}), ('K_17', 'K_18', {'weight': 4.904999999999994}), ('K_18', 'K_19', {'weight': 3.510000000000005})])


g.add_edges_from([('S_4', 'M_10', {'weight': 0}), ('S_6', 'M_9', {'weight': 0}), ('S_1', 'P_7', {'weight': 0}), ('S_9', 'K_17', {'weight': 0})])
g.add_edges_from([('M_1', 'K_10', {'weight': 0})])

# print(nx.shortest_path_length(g, source='K_13', target='S_3', weight='weight', method='dijkstra'))
# print(nx.shortest_path(g, source='K_13', target='S_3', weight='weight', method='dijkstra'))

stops_list = list(df["stop_id"])
fare_id = []
origin_id = []
destination_id = []
cost_li = []
fare_id_index = 1
for stop1 in range(len(stops_list)):
    print(stop1)
    for stop2 in range(len(stops_list)):
        if stops_list[stop1] != stops_list[stop2]:
            distance = nx.shortest_path_length(g, source=stops_list[stop1], target=stops_list[stop2], weight='weight', method='dijkstra')
            cost = assign_fare(distance)
            fare_id.append(f'F_{fare_id_index}')
            fare_id_index += 1
            cost_li.append(cost)
            origin_id.append(stops_list[stop1])
            destination_id.append(stops_list[stop2])


df1 = pd.DataFrame(list(zip(fare_id, origin_id, destination_id)), columns =['fare_id', 'origin_id', 'destination_id'])
df1.to_csv("fare_rule.csv", index=False)

df2 = pd.DataFrame(list(zip(fare_id, cost_li)), columns =['fare_id', 'price'])
df2.to_csv("fare_attribute.csv", index=False)









# dis = [0]+[1.48, 3.00, 5.00, 9.00, 10.40, 13.69, 15.85, 20.70, 22.650, 24.45, 26.10, 27.66, 30.960, 32.64, 33.91, 37.825, 42.73, 46.24]
# diss = []
# for i in range(1,len(dis)):
#     diss.append(dis[i] - dis[i-1])
# print(diss)
# print(len(diss))
# li = []
# for row in range(44, 62):
#     # print(diss[row-1-15])
#     li.append(tuple([df["stop_id"].iloc[row-1], df["stop_id"].iloc[row], {'weight': diss[row-1-43]}]))
# print(li)
# print(len(li))
