import streamlit as st
from PIL import Image

# streamlit run /PycharmProjects/Datathon1/Hackathon/0_🌍_Accueil.py
# streamlit run 0_🌍_Accueil.py

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

st.markdown("<h1 style='text-align: center; color: #fa535c'>Comment choisir une destination de voyage de façon éco-responsable ? </h1>",
                unsafe_allow_html=True)
st.write(' ')

#parce qu'il n'y a pas que le char à voile dans la vie Christophe, nous te proposons d'autres moyens de transport
#tout aussi safe sans pour autant être contraignant
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h4 style='color: #fcb238'>Parce qu'il n'y a pas que le char à voile dans la vie Christophe, nous te proposons d'autres moyens de transport tout aussi safe sans pour autant être contraignants.</h4>",
                unsafe_allow_html=True)
    st.write(' ')
    image = Image.open('images/char_a_voile_psg.jpg')
    st.image(image, caption='Créateur : Coco | Crédits : Liberation')

with col2:
    st.subheader('🌍 Accueil')
    st.markdown('**Accueil**')
    st.write(' ')
    st.subheader('🚵🏻 Simulations')
    st.markdown('**Prise de conscience de son impact**')


with col3:
    st.subheader('📊 Indicateurs')
    st.markdown('**Visualisations statistiques :**')
    st.markdown('**> AQI**')
    st.markdown('**> Cartes**')
    st.markdown('**> Constantes**')
    st.write(' ')