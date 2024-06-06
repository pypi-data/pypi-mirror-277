"""
Ce script regroupe les fonctions permettant d'importer en python les résultats détaillés 
en bandes de fréquences de calcul NORD2000 exportés depuis windPRO.
Il a été écrit en mars 2024 et fonctionne avec la version 4.0 de windPRO.
Les fichiers acceptés en entrée sont les fichiers .txt des résultats détaillés en bande 
d'octaves ainsi qu'en tiers d'ocatve.
"""

from itertools import product
import numpy as np
import pandas as pd


def read_nord2000_data(txt_file: str) -> pd.DataFrame:
    """Permet de lire le fichier .txt comme s'il s'agissait d'un .csv.
    Retourne un DataFrame brut qui nécessite d'être transformer ultérieurement
    afin de le structurer.

    :param txt_file: nom du fichier .txt correspondant aux résultats en bande
    d'octave (ou tiers d'octave) d'un calcul NORD2000 sur windPRO 4.0.
    :type txt_file: str
    :return: un DataFrame assez moche résultant de la lecture du fichier .txt par la
    fonction pd.read_csv
    :rtype: pd.DataFrame
    """
    raw_nord2000_data = pd.read_csv(txt_file, delimiter=";", skiprows=3)
    # To extract first wind data
    first_line = pd.read_csv(txt_file, skiprows=1, nrows=1, delimiter=";")
    raw_nord2000_data.loc[-1] = np.repeat(
        first_line.columns.values, raw_nord2000_data.shape[1]
    )
    return (
        raw_nord2000_data.apply(lambda x: x.str.replace(",", "."))
        .sort_index()
        .reset_index(drop=True)
    )


def get_wind_data(
    raw_nord2000_data: pd.DataFrame,
) -> tuple[np.ndarray, np.ndarray]:
    """Cherche dans le DataFrame les occurences des mots "Wind speed" et
    "Wind direction", puis extrait les valeurs qui leur sont associées. Permet
    ainsi de retourner deux arrays contenant les valeurs différentes prises par
    la vitesse et la direction du vent dans les données.

    :param raw_nord2000_data: le DataFrame brut obtenu par la fonction read_nord2000_data()
    :type raw_nord2000_data: pd.DataFrame
    :return: deux arrays, correspondant respectivement à la vitesse du vent et à la 
    direction du vent. Chacun de ces arrays contient les valeurs figurant dans les données 
    classées par ordre croissant
    :rtype: tuple[np.ndarray, np.ndarray]
    """
    wind_speed = (
        raw_nord2000_data["WTG"]
        .str.extract(r"Wind speed: \t(.*?)\t")
        .dropna()
        .drop_duplicates()
        .to_numpy()
        .astype(float)
        .T[0]
    )
    wind_direction = (
        raw_nord2000_data["WTG"]
        .str.extract(r"direction: \t(\d+)")
        .dropna()
        .drop_duplicates()
        .to_numpy()
        .astype(float)
        .T[0]
    )
    return wind_speed, wind_direction


def keep_only_numerical_data(raw_nord2000_data: pd.DataFrame) -> pd.DataFrame:
    """Transforme le DataFrame brut d'origine en un autre contenant uniquement 
    des valeurs numériques. Ainsi, les lignes ne contenant aucune valeur numérique 
    sont supprimées. Ce nouveau DataFrame est celui qui sera utilisé par la suite 
    en entrée des autres fonctions du script. Il est plus simple à manipuler que 
    celui d'origine.

    :param raw_nord2000_data: le DataFrame brut obtenu par la fonction read_nord2000_data()
    :type raw_nord2000_data: pd.DataFrame
    :return: le DataFrame contenant uniquement des valeurs numériques (ou des valeurs 
    manquantes "NaN").
    :rtype: pd.DataFrame
    """
    return raw_nord2000_data.apply(pd.to_numeric, errors="coerce").dropna(
        axis=0, how="all"
    )


def count_wind_turbines(numerical_nord2000_data: pd.DataFrame) -> np.ndarray:
    """Trouve le nombre de turbines figurant dans le calcul, en regardant quel 
    est le nombre max de la colonne "WTG".

    :param numerical_nord2000_data: le DataFrame contenant uniquement des valeurs 
    numériques obtenu par la fonction keep_only_numerical_data()
    :type numerical_nord2000_data: pd.DataFrame
    :return: le nombre de turbines figurant dans le calcul NORD2000.
    :rtype: np.ndarray
    """
    return int(numerical_nord2000_data["WTG"].max())


def get_source_power(numerical_nord2000_data: pd.DataFrame) -> pd.DataFrame:
    """Cherche les colonnes contenant les valeurs de puissance de source en dB(A) et 
    les retourne alignées dans un DataFrame d'une seule colonne.

    :param numerical_nord2000_data: le DataFrame contenant uniquement des valeurs 
    numériques obtenu par la fonction keep_only_numerical_data()
    :type numerical_nord2000_data: pd.DataFrame
    :return: un DataFrame a une colonne contenant toutes les valeurs de puissance 
    acoustique de la source en dB(A) pour chaque configuration.
    :rtype: pd.DataFrame
    """
    source_power_columns = [
        col for col in numerical_nord2000_data.columns if col.endswith("Hz")
    ]
    source_power = (
        numerical_nord2000_data[source_power_columns]
        .melt(value_name="source_power_per_band_dba")
        .drop(columns="variable")
    )
    return source_power


def get_attenuation(numerical_nord2000_data: pd.DataFrame) -> pd.DataFrame:
    """Cherche les colonnes contenant les valeurs d'atténuation en dB et les 
    retourne alignées dans un DataFrame d'une seule colonne.

    :param numerical_nord2000_data: le DataFrame contenant uniquement des valeurs 
    numériques obtenu par la fonction keep_only_numerical_data()
    :type numerical_nord2000_data: pd.DataFrame
    :return: un DataFrame a une colonne contenant toutes les valeurs d'atténuation 
    en dB pour chaque configuration.
    :rtype: pd.DataFrame
    """
    attenuation_columns = [
        col for col in numerical_nord2000_data.columns if col.endswith(".1")
    ]
    attenuation = (
        numerical_nord2000_data[attenuation_columns]
        .melt(value_name="attenuation_per_band_db")
        .drop(columns="variable")
    )
    return attenuation


def melt_nord2000_data(numerical_nord2000_data: pd.DataFrame) -> pd.DataFrame:
    """Permet de modifier le DataFrame du format "wide" au format "long". AUtrement 
    dit, les colonnes correspondants à une fréquence en particulier sont toutes mises 
    les unes à la suite des autres dans la longueur. Cela permet de se rapprocher du 
    format dans lequel on souhaite mettre les données. Pour chaque ligne, on a ainsi 
    une bande de fréquence, un niveau en dB(A) pour cette bande de fréquence, un 
    niveau global et une puissance de source en dB(A), une distance et une vitesse 
    de vent au niveau du hub.

    :param numerical_nord2000_data: le DataFrame contenant uniquement des valeurs 
    numériques obtenu par la fonction keep_only_numerical_data()
    :type numerical_nord2000_data: pd.DataFrame
    :return: DataFrame au format "long", avec les bandes de fréquence empilées les unes 
    en dessous des autres, associées à leur valeur de niveau de bande, niveau global 
    et puissance de la source en dB(A), ainsi qu'à leur distance et à leur 
    vitesse de vent au niveau du hub.
    :rtype: pd.DataFrame
    """
    useful_columns = [
        col for col in numerical_nord2000_data.columns if col.endswith(".2")
    ] + ["Distance", "Calculated", "Wind speed at hub height", "LwA,ref"]
    melted_data = (
        numerical_nord2000_data[useful_columns]
        .melt(
            id_vars=["Distance", "Calculated", "Wind speed at hub height", "LwA,ref"],
            var_name="frequency",
            value_name="sound_level_per_band_dba",
        )
        .replace(" Hz.2", "", regex=True)
        .astype(float)
        .rename(
            columns={
                "Distance": "distance",
                "Calculated": "global_sound_level_dba",
                "Wind speed at hub height": "wind_speed_at_hub",
                "LwA,ref": "global_source_power_dba",
            }
        )
    )
    return melted_data


def create_dataframe_with_all_combinations(
    melted_nord2000_data: pd.DataFrame,
    wind_speed: np.ndarray,
    wind_direction: np.ndarray,
    number_of_wind_turbines: int,
) -> pd.DataFrame:
    """Permet de créer un nouveau DataFrame from scratch à partir de toutes les données qu'on 
    a recueilli dans le DataFrame brut de base. Pour cela, on fait appel au module itertools, qui se 
    charge de créer toutes les combinaisons possibles, en veillant à ce que l'ordre des combinaisons 
    soit bien identique à l'ordre des niveaux sonores que l'on juxtapose par la suite au DataFrame.

    :param melted_nord2000_data: DataFrame au format "long", avec les bandes 
    de fréquence empilées les unes en dessous des autres, associées à leur 
    valeur de niveau de bande, niveau global et puissance de la source en dB(A), 
    ainsi qu'à leur distance et à leur vitesse de vent au niveau du hub.
    :type melted_nord2000_data: pd.DataFrame
    :param wind_speed: un array contenant les différentes vitesses de vent, 
    obtenu avec get_wind_data()
    :type wind_speed: np.ndarray
    :param wind_direction: un array contenant les différentes directions de vent, 
    obtenu avec get_wind_data()
    :type wind_direction: np.ndarray
    :param number_of_wind_turbines: le nombre de turbines figurant dans le 
    calcul NORD2000, obtenu avec la fonction count_wind_turbines()
    :type number_of_wind_turbines: int
    :return: un DataFrame proche de celui qu'on souhaite avoir au final, avec 
    quelques colonnes encore manquantes (puissance de source, atténuation, 
    méthode de calcul).
    :rtype: pd.DataFrame
    """
    wind_turbine_number = np.arange(number_of_wind_turbines + 1, dtype=float) + 1
    wind_turbine_number[-1] = np.nan
    variables = {
        "wind_speed_at_10m": wind_speed,
        "wind_direction": wind_direction,
        "wind_turbine_number": wind_turbine_number,
    }
    non_empty_labels = [key for key, arr in variables.items() if arr.any()]
    non_empty_arrays = [arr for arr in variables.values() if arr.any()]
    combinations = list(product(*non_empty_arrays))
    wind_combinations_dataframe = pd.DataFrame(
        np.resize(combinations, (melted_nord2000_data.shape[0], len(non_empty_arrays))),
        columns=non_empty_labels,
    )
    return pd.concat((melted_nord2000_data, wind_combinations_dataframe), axis=1)


def add_source_power_and_attenuation(
    dataframe_with_all_combinations: pd.DataFrame,
    source_power: pd.DataFrame,
    attenuation: pd.DataFrame,
) -> pd.DataFrame:
    """_summary_

    :param dataframe_with_all_combinations: un DataFrame proche de celui qu'on 
    souhaite avoir au final, avec quelques colonnes encore manquantes (puissance 
    de source, atténuation, méthode de calcul). Obtenu avec la fonction 
    create_dataframe_with_all_combinations()
    :type dataframe_with_all_combinations: pd.DataFrame
    :param source_power: un DataFrame a une colonne contenant toutes les valeurs 
    de puissance acoustique de la source en dB(A) pour chaque configuration.
    :type source_power: pd.DataFrame
    :param attenuation: un DataFrame a une colonne contenant toutes les valeurs 
    d'atténuation en dB pour chaque configuration.
    :type attenuation: pd.DataFrame
    :return: le DataFrame final avec les colonnes puissance acoustique en dB(A) et 
    atténuation en dB ajoutées.
    :rtype: pd.DataFrame
    """
    return pd.concat(
        (dataframe_with_all_combinations, source_power, -attenuation), axis=1
    )


def import_windpro_nord2000(txt_file: str) -> pd.DataFrame:
    """Permet d'importer et de mettre en forme de A à Z les données contenues dans le fichier .txt 
    correspondant aux résultats détaillées par bandes de fréquence d'un calcul NORD2000 sur 
    windPRO 4.0. Cette fonction regroupe toutes celles du script en une seule.

    :param txt_file: nom du fichier .txt correspondant aux résultats en bande
    d'octave (ou tiers d'octave) d'un calcul NORD2000 sur windPRO 4.0.
    :type txt_file: str
    :return: un DataFrame propre contenant toutes les données de résultats détaillés par bandes de 
    fréquence d'un calcul NORD2000 sur windPRO 4.0
    :rtype: pd.DataFrame
    """
    raw_nord2000_data = read_nord2000_data(txt_file)
    wind_speed, wind_direction = get_wind_data(raw_nord2000_data)
    numerical_nord2000_data = keep_only_numerical_data(raw_nord2000_data)
    number_of_wind_turbines = count_wind_turbines(numerical_nord2000_data)
    source_power = get_source_power(numerical_nord2000_data)
    attenuation = get_attenuation(numerical_nord2000_data)
    melted_nord2000_data = melt_nord2000_data(numerical_nord2000_data)
    dataframe_with_all_combinations = create_dataframe_with_all_combinations(
        melted_nord2000_data, wind_speed, wind_direction, number_of_wind_turbines
    )
    final_dataframe = add_source_power_and_attenuation(
        dataframe_with_all_combinations, source_power, attenuation
    )
    final_dataframe.insert(0, "method", "Nord2000 (windPRO)")
    if number_of_wind_turbines <= 1:
        final_dataframe = final_dataframe[final_dataframe["distance"].notna()]
    return final_dataframe
