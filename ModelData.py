import numpy as np


def Load3BusCase():
    Bus = {"Nr": np.array([1, 2, 3]), "Type": np.array([3, 2, 1])}

    Gen = {
        "BusNr": np.array([1, 2]),
        "PG": np.array([0.8, 0.0]),
        "Pmax": np.array([3.0, 0.8]),
        "Pmin": np.array([0.0, 0.0]),
        "Cost": np.array([2.0, 1.0]),
    }

    Branch = {
        "F_BUS": np.array([1, 1, 2]),
        "T_BUS": np.array([2, 3, 3]),
        "BR_X": np.array([0.1, 0.1, 0.1]),
        "RATE": np.array([0.25, 2.0, 2.0]),
    }

    Load = {
        "BusNr": np.array([1, 2, 3]),
        "PL": np.array([0.0, 0.0, 0.8]),
        "Cost": np.array([100, 100, 100]),
    }

    return Bus, Gen, Branch, Load
