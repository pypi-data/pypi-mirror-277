"""
Created on 04.06.2024

This script serve as an example on how to use the package, and as a test in developing it

@author: Mathias Berg Rosendal, PhD Student at DTU Management (Energy Economics & Modelling)
"""
#%% ------------------------------- ###
###        0. Script Settings       ###
### ------------------------------- ###

from pybalmorel.functions import MainResults, plot_map, symbol_to_df
import gams
import os

balm_path = r'C:\Users\mberos\Danmarks Tekniske Universitet\PhD in Transmission and Sector Coupling - Dokumenter\Deliverables\Smart-coupling of Balmorel and Antares\240523 Results\Output\Balmorel'

SC1 = 'MainResults_HTFictDemFunc3Max_Iter5.gdx'
SC2 = 'MainResults_HTFictDemFunc3Max_Iter0.gdx'

ws = gams.GamsWorkspace()
db = ws.add_database_from_gdx(os.path.join(balm_path, SC1))

#%% ------------------------------- ###
###        1. Plotting Tools        ###
### ------------------------------- ###

### 1.1 Interactive bar chart tool
res = MainResults('MainResults_ScenarioName.gdx', 'Files')
res.bar_chart()


### 1.2 Plotting maps
plot_map('files', 'files/2024 BalmorelMap.geojson', 'ScenarioName',
         2050, 'Electricity', 'files/bypass_lines.csv')

