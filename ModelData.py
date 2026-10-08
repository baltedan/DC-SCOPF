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


def Load6BusCase():
    Bus = {"Nr": np.array([1, 2, 3, 4, 5, 6]), "Type": np.array([3, 2, 2, 2, 1, 1])}

    Gen = {
        "BusNr": np.array([1, 2, 3, 4]),
        "PG": np.array([0.57, 0.8, 2.2, 2.5]),
        "Pmax": np.array([2.5, 2.5, 2.5, 2.5]),
        "Pmin": np.array([0.5, 0.5, 0.5, 0.5]),
        "Cost": np.array([4, 3, 2, 1]),
    }

    Branch = {
        "F_BUS": np.array([1, 1, 2, 3, 3, 4, 4]),
        "T_BUS": np.array([2, 5, 4, 5, 6, 5, 6]),
        "BR_X": np.array([0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]),
        "RATE": np.array([1.2, 1.2, 1.2, 1.2, 1.3, 1.2, 1.2]),
    }

    Load = {
        "BusNr": np.array([1, 2, 3, 4, 5, 6]),
        "PL": np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]),
        "Cost": np.array([100, 100, 100, 100, 100, 100]),
    }

    return Bus, Gen, Branch, Load

