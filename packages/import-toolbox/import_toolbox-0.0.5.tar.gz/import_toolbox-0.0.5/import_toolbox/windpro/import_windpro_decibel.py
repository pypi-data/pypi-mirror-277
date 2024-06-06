"""
Ce script regroupe les fonctions permettant d'importer en python les résultats détaillés 
de calcul DECIBEL exportés depuis windPRO.
Il a été écrit en mars 2024 et fonctionne avec la version 4.0 de windPRO.
Les fichiers acceptés en entrée sont les fichiers .txt des résultats détaillés ainsi que 
des résultats détaillés par bande d'octave, 
les deux étant à priori identiques. Le principe général utilisé ici est d'extraire toutes 
les données du fichier brut, puis de reconstruire à partir de cela un DataFrame 
from scratch contenant toutes les combinaisons.
"""

import os
from itertools import product
import numpy as np
import pandas as pd


def read_decibel_data(txt_file: str) -> pd.DataFrame:
    """Permet d'importer de manière brute un fichier .txt correspondant aux résultats
    détaillés de calcul DECIBEL donné par windPRO, sous la forme d'un DataFrame pandas.
    Ce DataFrame étant assez moche, il nécessite d'être transformé, ce qui sera possible
    avec les autres fonctions du script. Attention, cette fonction peut etre assez lente,
    en raison probablement du poids important de certains fichiers de résultats DECIBEL.

    :param txt_file: nom du fichier .txt correspondant aux résultats détaillés de calcul
    DECIBEL sur windPRO 4.0
    :type txt_file: str
    :return: un DataFrame assez moche résultant de la lecture du fichier .txt par la
    fonction pd.read_csv
    :rtype: pd.DataFrame
    """
    return pd.read_csv(
        txt_file,
        delimiter=";",
        skiprows=1,
        encoding="latin",
        low_memory=False,
        dtype=str,
    ).replace(",", ".", regex=True)


def get_meteo_variables(
    decibel_data: pd.DataFrame,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Cherche dans le DataFrame les occurences des mots "Wind speed", "Relative humidity"
    et "Temperature", puis extrait les valeurs qui leurs sont associées.
    Permet ainsi d'extraire dans trois array les valeurs différentes prises par la vitesse
    du vent, l'humidité et la température.

    :param decibel_data: le DataFrame brut obtenu par la fonction read_decibel_data()
    :type decibel_data: pd.DataFrame
    :return: trois arrays, correspondant respectivement à la vitesse de vent, l'humidité et
    la température.
    Chacun de ces arrays contient les valeurs figurant dans les données classées par ordre
    croissant.
    :rtype: tuple[np.ndarray, np.ndarray, np.ndarray]
    """
    wind_speed = (
        decibel_data.columns.str.extract(r"Wind speed: (.*?),")[0]
        .str.replace(",", ".")
        .astype(float)
        .dropna()
        .unique()
    )
    humidity = (
        decibel_data.columns.str.extract(r"Relative humidity: (.*?) %")[0]
        .str.replace(",", ".")
        .astype(float)
        .dropna()
        .unique()
    )
    temperature = (
        decibel_data.columns.str.extract(r"Temperature: (.*?) °C")[0]
        .str.replace(",", ".")
        .astype(float)
        .dropna()
        .unique()
    )
    return wind_speed, humidity, temperature


def count_wind_turbines(decibel_data: pd.DataFrame) -> int:
    """Detecte le nombre d'éoliennes différentes utilisées lors du calcul DECIBEL. Cette fonction
    permet surtout de déterminer si il y a une éolienne ou plus.
    Cette info est importante car lorsqu'il y a plusieurs éoliennes, une ligne "Sum" correspondant
    à la somme des contributions vient s'ajouter dans le fichier .txt en
    dessous de chaque serie de calcul.

    :param decibel_data: le DataFrame brut obtenu par la fonction read_decibel_data
    :type decibel_data: pd.DataFrame
    :return: le nombre d'éoliennes utilisées pour le calcul
    :rtype: int
    """
    return int(decibel_data["WTG"].apply(pd.to_numeric, errors="coerce").max())


def get_distances(
    decibel_data: pd.DataFrame, number_of_wind_turbines: int
) -> np.ndarray:
    """Extrait les différentes distances horizontales contenues dans les données. On extrait les
    distances horizontales plutot que les distances source-récepteur par soucis de cohérence avec ce
    qu'on trouve dans les détails de calcul NORD2000 sur windPRO.

    :param decibel_data: le DataFrame brut obtenu par la fonction read_decibel_data()
    :type decibel_data: pd.DataFrame
    :param number_of_wind_turbines: le nombre d'éoliennes utilisées pour le calcul, obtenues par la
    fonction count_wind_turbines
    :type number_of_wind_turbines: int
    :return: un array contenant les différentes distances horizontales contenues dans les données,
    classées par ordre croissant.
    :rtype: np.ndarray
    """
    distance = (
        decibel_data["Unnamed: 1"]
        .str.replace(r"\s", "", regex=True)
        .apply(pd.to_numeric, errors="coerce")
        .dropna()
        .to_numpy()
    )
    # Take account of "sum" lines in windpro data and give them a null distance
    if number_of_wind_turbines >= 2:
        return np.insert(
            distance,
            np.arange(
                number_of_wind_turbines,
                len(distance) + number_of_wind_turbines,
                number_of_wind_turbines,
            ),
            np.nan,
        )
    return distance


def get_frequency_bands(decibel_data: pd.DataFrame) -> np.ndarray:
    """Extrait les différentes bandes de fréquence contenues dans les données.

    :param decibel_data: le DataFrame brut obtenu par la fonction read_decibel_data()
    :type decibel_data: pd.DataFrame
    :return: un array contenant les différentes bandes de fréquence contenues dans les données,
    classées par ordre croissant.
    :rtype: np.ndarray
    """
    return (
        decibel_data["Unnamed: 3"]
        .apply(pd.to_numeric, errors="coerce")
        .dropna()
        .astype(float)
        .unique()
    )


def get_levels(decibel_data: pd.DataFrame, column_name: str) -> np.ndarray:
    """Extrait sous la forme d'un unique array tous les niveaux sonores par bande de
    fréquence. Selon la valeur du paramètre column_name,
    le type de niveau recherché est différent (niveau par bande de fréquence en dB, attenuation,
    etc...)

    :param decibel_data: le DataFrame brut obtenu par la fonction read_decibel_data()
    :type decibel_data: pd.DataFrame
    :param column_name: le nom de la colonne à viser pour récuper les niveaux sonores par bande
    de fréquence.
    Peut prendre les valeurs suivantes suivant ce que l'on cherche : "Calculated" pour le niveau
    en dB par bande de fréquence, "A" pour l'atténuation totale en dB, "Aatm" pour l'atténuation
    due à l'absorption atmosphérique, "Agr" pour l'atténuation due à l'effet de sol, "LwA.ref"
    pour la puissance de la source par bande de fréquence en dB(A).
    :type column_name: str
    :return:
    :rtype: np.ndarray
    """
    numerical_data = (
        decibel_data.rename(columns=decibel_data.iloc[0])
        .drop(index=0, columns=["Sound distance", "Distance", "No."])
        .apply(pd.to_numeric, errors="coerce")
        .dropna(axis=0, how="all")[column_name]
    )
    if isinstance(numerical_data, pd.Series):
        numerical_data = numerical_data.to_frame()
    return np.repeat(
        numerical_data.melt()
        .drop(columns="variable")
        .reset_index(drop=True)
        .to_numpy(),
        3,
    )


def create_dataframe_with_all_combinations(
    wind_speed: np.ndarray,
    humidity: np.ndarray,
    temperature: np.ndarray,
    distance: np.ndarray,
    frequency: np.ndarray,
) -> pd.DataFrame:
    """Permet d'initialiser un nouveau DataFrame from scratch à partir de toutes les données qu'on
    a recueilli dans le DataFrame brut de base. Pour cela, on fait appel au module itertools, qui
    se charge de créer toutes les combinaisons possibles, en veillant à ce que l'ordre des
    combinaisons soit bien identique à l'ordre des niveaux sonores que l'on juxtaposera par la
    suite au DataFrame.

    :param wind_speed: les différentes valeurs de vitesse de vent
    :type wind_speed: np.ndarray
    :param humidity: les différentes valeurs d'humidité
    :type humidity: np.ndarray
    :param temperature: les différentes valeurs de température
    :type temperature: np.ndarray
    :param distance: les différentes valeurs de distance horizontale
    :type distance: np.ndarray
    :param frequency: les différentes bandes de fréquence
    :type frequency: np.ndarray
    :return: un DataFrame contenant toutes les configurations possibles contenues dans les données.
    Attention, il n'y a aucune donnée de niveau sonore dans ce DataFrame.
    :rtype: pd.DataFrame
    """
    missing_frequencies = np.array(
        [
            50,
            80,
            100,
            160,
            200,
            315,
            400,
            630,
            800,
            1250,
            1600,
            2500,
            3150,
            5000,
            6300,
            10000,
        ]
    )
    frequency = np.sort(np.concatenate((frequency, missing_frequencies)))
    variables = {
        "wind_speed_at_10m": wind_speed,
        "humidity": humidity,
        "temperature": temperature,
        "distance": distance,
        "frequency": frequency,
    }
    non_empty_labels = [key for key, arr in variables.items() if arr.any()]
    non_empty_arrays = [arr for arr in variables.values() if arr.any()]
    combinations = list(product(*non_empty_arrays))
    return pd.DataFrame(combinations, columns=non_empty_labels)


def import_windpro_decibel(txt_file: str) -> pd.DataFrame:
    """Permet d'importer et de mettre en forme de A à Z les données contenues dans le fichier .txt
    correspondant aux résultats détaillées d'un calcul DECIBEL sur windPRO 4.0. Cette fonction
    regroupe toutes celles du script en une seule.

    :param txt_file: nom du fichier .txt correspondant aux résultats détaillés de calcul
    DECIBEL sur windPRO 4.0
    :type txt_file: str
    :return: un DataFrame propre contenant toutes les données de résultats détaillés d'un calcul
    DECIBEL sur windPRO 4.0
    :rtype: pd.DataFrame
    """
    decibel_data = read_decibel_data(txt_file)
    wind_speed, humidity, temperature = get_meteo_variables(decibel_data)
    number_of_wind_turbines = count_wind_turbines(decibel_data)
    distance = get_distances(decibel_data, number_of_wind_turbines)
    frequency = get_frequency_bands(decibel_data)
    dataframe_with_all_combinations = create_dataframe_with_all_combinations(
        wind_speed, humidity, temperature, distance, frequency
    )
    dataframe_with_all_combinations.insert(
        0, "ground_attenuation_per_band_db", get_levels(decibel_data, "Agr")
    )
    dataframe_with_all_combinations.insert(
        0, "atmospheric_attenuation_per_band_db", get_levels(decibel_data, "Aatm")
    )
    dataframe_with_all_combinations.insert(
        0, "attenuation_per_band_db", get_levels(decibel_data, "A")
    )
    dataframe_with_all_combinations.insert(
        0, "source_power_per_band_dba", get_levels(decibel_data, "LwA.ref")
    )
    dataframe_with_all_combinations.insert(
        0, "sound_level_per_band_db", get_levels(decibel_data, "Calculated")
    )
    dataframe_with_all_combinations.insert(0, "method", "ISO 9613 (windPRO)")
    return dataframe_with_all_combinations
