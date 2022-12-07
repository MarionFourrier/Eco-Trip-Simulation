import streamlit as st
import googlemaps
import pandas as pd
from PIL import Image

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

st.markdown("<h1 style='text-align: center; color: #fa535c'>Au départ de Nantes</h1>",
                unsafe_allow_html=True)

gmaps = googlemaps.Client(key='suppressed_from_the_git_file_for_safety_reasons')
my_path = 'csv'
df_villes_pollution = pd.read_csv(my_path+'/pollution_clean.csv')
df_villes_pollution_france = df_villes_pollution.loc[df_villes_pollution['Country'] == 'France']

dico = {'vehicules': ['A pieds', 'A vélo', 'En char à voile', 'En train', 'En voiture', 'En avion', 'En 4x4', 'En jet privé'], 'emission':[0, 0, 0, 20, 130, 170, 250, 1500]}
#dico = {'vehicules': ['Voiture', '4x4', 'Char à voile', 'Jet privé', 'Avion', 'Train', 'Velo', 'A pieds'], 'emission':[130, 250, 0, 1500, 170, 20, 0, 0]}
df_emission_vehicules = pd.DataFrame(data=dico)
villes_liste = df_villes_pollution_france['City'].tolist()
vehicules_liste = df_emission_vehicules['vehicules'].tolist()



def distance_temps(ville, transit, mode):
    distance = gmaps.distance_matrix('Nantes', ville, transit_mode=transit, mode=mode)["rows"][0]["elements"][0]['distance']['value']
    distance /= 1000
    temps = gmaps.distance_matrix('Nantes', ville, transit_mode=transit, mode=mode)["rows"][0]["elements"][0]['duration']['text']
    return distance, temps



col1, col2 = st.columns(2)

moyen_transport = st.radio(
    "Par quel moyen vas-tu voyager ?",
    vehicules_liste)

path_image='images/'

with col1:
    if moyen_transport == 'En train':
        transit = 'train'
        mode = 'transit'
    elif moyen_transport == 'En avion' or 'En jet privé':
        transit = None
        mode = None
    elif moyen_transport == 'A vélo':
        transit = None
        mode = 'bicycling'
    elif moyen_transport == 'A pieds':
        transit = None
        mode = 'walking'
    else:
        transit = None
        mode = None
    if moyen_transport == '':
        pass
    else:
        emission_co_deux = df_emission_vehicules.loc[df_emission_vehicules['vehicules'] == moyen_transport,
                                                    ['emission']]

with col2:
    if moyen_transport == 'A pieds':
        image1 = Image.open(path_image+'pieton.png')
        st.image(image1)
    elif moyen_transport == 'A vélo':
        image2 = Image.open(path_image+'velo.png')
        st.image(image2)
    elif moyen_transport == 'En char à voile':
        image3 = Image.open(path_image+'char_a_voile.png')
        st.image(image3)
    elif moyen_transport == 'En train':
        image4 = Image.open(path_image+'train.png')
        st.image(image4)
    elif moyen_transport == 'En voiture':
        image5 = Image.open(path_image+'voiture.png')
        st.image(image5)
    elif moyen_transport == 'En avion':
        image6 = Image.open(path_image+'avion.png')
        st.image(image6)
    elif moyen_transport == 'En 4x4':
        image7 = Image.open(path_image+'4x4.png')
        st.image(image7)
    else:
        image8 = Image.open(path_image+'jet.png')
        st.image(image8)


ville_input = st.selectbox('Dans quelle ville souhaites-tu te rendre ?', villes_liste)

if ville_input == '':
    yeah = None
else:
    if moyen_transport == 'A vélo':
        transit = None
        mode = 'bicycling'
    elif moyen_transport == 'A pieds':
        transit = None
        mode = 'walking'
    else:
        pass
    distance, temps = distance_temps(ville_input, transit, mode)
    emission_trajet = distance * emission_co_deux
    ville_aqi = df_villes_pollution_france.loc[df_villes_pollution_france['City'] == ville_input,
                                               ['AQI']]

st.write('Tu parcoureras ', distance, 'km en', temps, '.')
#st.write('Tu y passeras', temps, '.')
st.write('Ton voyage génèrera ', round(emission_trajet.iloc[0]['emission']*0.01, 3), 'kgeqC.')

def cond(x):
    if x<=50:
        return '. Ce qui signifie que la ville possède une qualité de l\'air satisfaisante'
    elif x>=51 and x<=100:
        return '. Ce qui signifie que la qualité de l\'air de cette ville est acceptable.'
    elif x>=101 and x<=150:
        return '. Ce qui signifie que les populations à risque peuvent ressentir les effets de la pollution de l\'air.'
    elif x>=151 and x<=200:
        return '. Ce qui siginifie que les populations à risque sont fort exposées.'
    elif x>=201 and x<=300:
        return '. Ce qui signifie que les risques sur la santé sont accrus pour toute les populations.'
    else:
        return '. Ce qui signifie la pollution de l\'air atteint un seuil alarmant.'

st.write(ville_input, 'a un AQI de', ville_aqi.iloc[0]['AQI'], cond(ville_aqi.iloc[0]['AQI']))




