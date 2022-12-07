import streamlit as st

st.set_page_config(
    page_title="Eco-responsabilisons-nous !",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )

######
# IMPORT LIBRAIRIES
######
import pandas as pd
import plotly.express as px


######
# IMPORT DATASETS
######
# Df pollution
my_path = 'csv/'
link_pollution = my_path+'pollution_clean.csv'
df_pollution = pd.read_csv(link_pollution, encoding="ISO-8859-1")
# Df villes coordonnees
link_coordonnee = my_path+'coordonnees_villes_clean.csv'
df_villes_coordonnee = pd.read_csv(link_coordonnee)
# Gapminder de plotly pour obtenir les codes iso_alpha (pour le maping)
gapminder = px.data.gapminder()


######
# NETTOYAGE ET PREPARATION DES DF
######

###
# Gapminder
###
# Selection des colonnes
gapminder = gapminder[['country', 'iso_alpha']]
len(gapminder['iso_alpha'].value_counts())
# Renommer colonnes
gapminder.rename(columns = {'country':'Country'}, inplace = True)
# Supprimer lignes inutiles
gapminder.drop_duplicates(inplace = True)


###
# Df pollution country
###
# Join pour avoir les codes iso_alpha dans le df_pollution
df_pollution2 = pd.merge(df_pollution,
                        gapminder,
                        how = 'left')
# Group by Country pour avoir les moyennes  par pays
df_pollution_country = df_pollution2.groupby(by = ['Country']).mean()
# Reformation du df en préparation du merge
df_pollution_country = pd.DataFrame(df_pollution_country)
df_pollution_country['Country'] = df_pollution_country.index
df_pollution_country = df_pollution_country.reset_index(drop=True)
# Merge du group by avec le reste du dataset pollution (oui j'aurais pu faire une pivot table peutêtre, je sais plus, #fatiguée)
df_pollution_country = pd.merge(df_pollution_country,
                                df_pollution2,
                                how = 'inner',
                                left_on='Country',
                                right_on='Country')
# Drop duplicates colonne country
df_pollution_country.drop_duplicates(subset = ['Country'], inplace = True)
# Nan codes iso_alpha
df_pollution_country.isna().sum()
# Selection colonnes
df_pollution_country.drop(columns = ['City', 'AQI_y', 'Category', 'Region'], inplace = True)

# Remplacement Nans
# Republic of Korea
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Republic of Korea']) = 'KOR'
# Russian Federation
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Russian Federation']) = 'RUS'
# United States of America
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'United States of America']) = 'USA'
# United Arab Emirates
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'United Arab Emirates']) = 'ARE'
# United Kingdom of Great Britain and Northern Ireland
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'United Kingdom of Great Britain and Northern Ireland']) = 'GBR'
# Ukraine
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Ukraine']) = 'UKR'
# Qatar
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Qatar']) = 'QAT'
# Yemen
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Yemen']) = 'YEM'
# Uzbekistan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Uzbekistan']) = 'UZB'
# Tajikistan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Tajikistan']) = 'TJK'
# Democratic Republic of the Congo
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Democratic Republic of the Congo']) = 'COD'
# Iran (Islamic Republic of)
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Iran (Islamic Republic of)']) = 'IRN'
# Turkmenistan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Turkmenistan']) = 'TKM'
# Congo
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Congo']) = 'COG'
# Viet Nam
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Viet Nam']) = 'VNM'
# Syrian Arab Republic
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Syrian Arab Republic']) = 'SYR'
# State of Palestine
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'State of Palestine']) = 'PSE'
# Malaysia
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Malaysia']) = 'MYS'
# Kyrgyzstan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Kyrgyzstan']) = 'KGZ'
# Venezuela (Bolivarian Republic of)
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Venezuela (Bolivarian Republic of)']) = 'VEN'
# Slovakia
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Slovakia']) = 'SVK'
# Republic of North Macedonia
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Republic of North Macedonia']) = 'MKD'
# Kazakhstan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Kazakhstan']) = 'KAZ'
# Czechia
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Czechia']) = 'CZE'
# South Sudan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'South Sudan']) = 'SDN'
# Azerbaijan
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Azerbaijan']) = 'AZE'
# Armenia
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Armenia']) = 'ARM'
# Georgia
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Georgia']) = 'GEO'
# Bolivia (Plurinational State of)
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'Bolivia (Plurinational State of)']) = 'BOL'
# United Republic of Tanzania
(df_pollution_country['iso_alpha'].loc[df_pollution['Country'] == 'United Republic of Tanzania']) = 'TZA'


# Réattribution des 'Categories' par pays en fonction de leurs aqi MOYEN !
df_pollution_country['Category_x'] = 'Unhealthy'
df_pollution_country['Category_x'].loc[df_pollution_country['AQI_x'] > 300] = 'Hazardous'
df_pollution_country['Category_x'].loc[df_pollution_country['AQI_x'] <= 150] = 'Unhealthy for Sensitive Groups'
df_pollution_country['Category_x'].loc[df_pollution_country['AQI_x'] <= 100] = 'Moderate'
df_pollution_country['Category_x'].loc[df_pollution_country['AQI_x'] <= 50] = 'Good'


###
# Df villes coordonnee pollution
###

df_villes_coordonnee_pollution = pd.merge(df_pollution, df_villes_coordonnee, how='inner', left_on='City', right_on='Name')
df_villes_coordonnee_pollution[['Lat', 'Long']] = df_villes_coordonnee_pollution['Coordinates'].str.split(',', 1, expand=True)
df_villes_coordonnee_pollution['Lat'] = df_villes_coordonnee_pollution['Lat'].astype(float)
df_villes_coordonnee_pollution['Long'] = df_villes_coordonnee_pollution['Long'].astype(float)
df_villes_coordonnee_pollution.sort_values(by = 'AQI', inplace = True)



# Ordonner colonnes pour afficher dans le bon ordre la légende sur la viz
df_pollution_country.sort_values(by='AQI_x', inplace=True)

tab1, tab2, tab3 = st.tabs(['Carte AQI par ville', 'Carte AQI par pays', 'Bilan carbone par moyen de locomotion'])

with tab1:
    fig_ville = px.scatter_geo(df_villes_coordonnee_pollution,
                               lat='Lat',
                               lon='Long',
                               color='Category',
                               color_discrete_map={"Good": "#125b54",
                                                   "Moderate": "#2fc8ad",
                                                   "Unhealthy for Sensitive Groups": "#fcb238",
                                                   "Unhealthy": "#fb8939",
                                                   "Very Unhealthy": "#fa535c",
                                                   "Hazardous": "#784087"},
                               hover_data=['City'],
                               projection="natural earth")
    fig_ville.update_layout(title="<b>CARTE DES INDICES DE POLLUTIONS DE L\'AIR PAR VILLE</b>",
                            title_x=0.425,
                            legend_title="<b>CATÉGORIES</b>")
    st.plotly_chart(fig_ville)

with tab2:
    ######
    # CARTE AQI MOYEN PAR PAYS
    ######

    # Planisphère par pays plotly :
    fig_pays = px.choropleth(df_pollution_country,
                             locations="iso_alpha",
                             color="Category_x",  # Comme un hue sur seaborn
                             color_discrete_map={"Good": "#125b54", "Moderate": "#2fc8ad",
                                                 "Unhealthy for Sensitive Groups": "#fcb238", "Unhealthy": "#fb8939",
                                                 "Very Unhealthy": "#fa535c", "Hazardous": "#784087"},
                             projection="natural earth",
                             hover_data=['Country'], )
    fig_pays.update_layout(title="<b>CARTE DES INDICES DE POLLUTIONS DE L\'AIR MOYENS PAR PAYS</b>",
                           title_x=0.425,
                           legend_title="<b>CATÉGORIES</b>")
    st.plotly_chart(fig_pays)

with tab3:
    ######
    # EMISSION DE CO2 PAR MODE DE TRANSPORT, EN GRAMMES PAR KM
    ######

    dico = {'vehicules': ['VOITURE ', '4x4 ', 'CHAR À VOILE ', 'JET PRIVÉ ', 'AVION ', 'TRAIN '],
            'emission': [130, 250, 0, 1500, 170, 20]}
    df_emission_vehicules = pd.DataFrame(data=dico)
    df_emission_vehicules.sort_values(by='emission', inplace=True)

    fig_transport = px.bar(df_emission_vehicules,
                           y='vehicules',
                           x='emission',
                           color='vehicules',
                           color_discrete_map={
                               'VOITURE ': '#fcb238',
                               '4x4 ': '#fcb238',
                               'CHAR À VOILE ': '#fcb238',
                               'JET PRIVÉ ': '#fcb238',
                               'AVION ': '#fcb238',
                               'TRAIN ': '#fcb238'})

    fig_transport.update_layout(title="<b>ÉMISSION DE CO2 PAR MODE DE TRANSPORT, EN GRAMMES PAR KM</b>",
                                title_x=0.5,
                                xaxis_title="<b>CO2 ÉMIS EN GRAMMES PAR KM</b>",
                                yaxis_title=None,
                                legend=None,
                                showlegend=False)
    st.plotly_chart(fig_transport)

