import rvr
import antitetico
import montecarlo
import montecarlo_cycles
import matplotlib.pyplot as plt

if __name__ == "__main__":
    herschel = [(1,2), (2,3), (3,5), (4,5), (2,4), (1,6), (1,7), (5,8), (5,9), (3,6), (4,7), (7,8), (6,9), (9,10), (8,10), (10,11), (7,11), (6,11)]
    # dodecaedro = [(1,2), (2,3), (3,4), (4,5), (5,1), (1,6), (2,7), (3,8), (4,9), (5,10), (11,6), (12,7), (13,8), (14,9), (15,10), (11,7), (12,8), (13,9), (14,10), (15,6), (11,16), (12,17), (13,18), (14,19), (15,20), (20,16), (16,17), (17,18), (18,19), (19,20)]
    probabilities = [0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]
    probability_095 = 0.95
    # rvr_graph_probabilities = []
    # rvr_graph_variances = []
    # mcc_graph_probabilities = []
    # mcc_graph_variances = []
    # ant_graph_probabilities = []
    # ant_graph_variances = []
    mcc_6_graph_probabilities = []

    # for p in probabilities:
    #     herschel_with_p = [(1,2,p), (2,3,p), (3,5,p), (4,5,p), (2,4,p), (1,6,p), (1,7,p), (5,8,p), (5,9,p), (3,6,p), (4,7,p), (7,8,p), (6,9,p), (9,10,p), (8,10,p), (10,11,p), (7,11,p), (6,11,p)]
    #     # dodecaedro_with_p = [(1,2,p), (2,3,p), (3,4,p), (4,5,p), (5,1,p), (1,6,p), (2,7,p), (3,8,p), (4,9,p), (5,10,p), (11,6,p), (12,7,p), (13,8,p), (14,9,p), (15,10,p), (11,7,p), (12,8,p), (13,9,p), (14,10,p), (15,6,p), (11,16,p), (12,17,p), (13,18,p), (14,19,p), (15,20,p), (20,16,p), (16,17,p), (17,18,p), (18,19,p), (19,20,p)]
    #     rvr_result = rvr.call(herschel_with_p)
    #     rvr_graph_probabilities.append(rvr_result[0])
    #     rvr_graph_variances.append(rvr_result[1])

    # for p in probabilities:
    #     mcc_result = montecarlo.call(herschel, p)
    #     mcc_graph_probabilities.append(mcc_result[0])
    #     mcc_graph_variances.append(mcc_result[1])
    
    # for p in probabilities:
    #     ant_result = antitetico.call(herschel, p)
    #     ant_graph_probabilities.append(ant_result[0])
    #     ant_graph_variances.append(ant_result[1])

    
    # print(rvr_graph_probabilities)
    # print(rvr_graph_variances)
    # print(mcc_graph_probabilities)
    # print(mcc_graph_variances)
    # print(ant_graph_probabilities)
    # print(ant_graph_variances)

    # plt.plot(probabilities, rvr_graph_variances)
    # plt.plot(probabilities, mcc_graph_variances)
    # plt.plot(probabilities, ant_graph_variances)

    # plt.show()

    mcc_6_graph_probabilities = montecarlo_cycles.call(herschel, probability_095)[0]

    print(mcc_6_graph_probabilities)
    
