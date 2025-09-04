import streamlit as st
from PIL import Image

st.title("━━━━⊱⋆⊰━━━━")

st.header("get to know me...")
st.write("my name is gaby, i love romance and everything cute. read FANGS for clear skin. 𐔌՞. .՞𐦯")
image = Image.open('Interfaces Mult2.png')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('write me a message!', 'write here...')
st.write('your message is:', texto)

st.subheader("wanna be friends? answer these!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("you like romance?")
    st.write("if this checkbox is not filled, we can't be friends!")
    resp = st.checkbox('i love it!!!')
    if resp:
       st.write('omg yay!')
  
with col2:
    st.subheader("fav type?")
    modo = st.radio("choose wisely...", ('BL', 'GL', 'HET'))
    if modo == 'BL':
       st.write('we gotta be bffs')
    if modo == 'GL':
       st.write('i love girls! teach me more!')
    if modo == 'HET':
       st.write('if its not shojosei ur on thin ice')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
