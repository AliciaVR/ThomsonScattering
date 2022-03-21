# -*- coding: utf-8 -*-
"""ne_models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JQ2EhsspvRN0azKuZnmhiOqFq2o5KyJo
"""
import thomsonpy.config.thomson_scattering_params as tsp
import thomsonpy.config.solar_imager_params as sip
import thomsonpy.constants.units as units

def crammer_model(d):
    '''
    Description
    ----------- 
    Electron number density profile obtained by Crammer et al. (1999) using the
    UVCS/WLC aboard SOHO satellite.

    Initially, in cm⁻³. A units conversion have been applied: cm⁻³ to m⁻³.

    Parámetros
    -----------
    d: distancia del centro de la estrella (S) al punto de dispersión (Q). Es
    necesario introducirla en RSol (en general, radios estelares).

    Devuelve
    -----------
    Valor de la densidad electrónica (m⁻³)
    '''
    # en cm⁻³ --> m⁻³
    return 1E8 * (3.89 * d**-10.5 + 0.00869 * d**-2.57) * 1E6

def predictive_science_model(z, TG, NE_MODEL):
    octree = NE_MODEL
    target = TG.get_target(z) * units.METERS_TO_RSOL
    data = octree.search_nearest(target)
    return data.get_ne() 