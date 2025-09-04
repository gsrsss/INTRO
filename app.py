import streamlit as st
from PIL import Image

st.title("━━━━⊱⋆⊰━━━━")

st.header("get to know me...")
st.write("my name is gaby, i love romance and everything cute. read FANGS for clear skin. 𐔌՞. .՞𐦯")
image = Image.open('Girly pup🎀.jpeg')

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
       st.write('depends on what it is...but ur on thin ice buddy')
        
st.subheader("click if you love ukes")
if st.button('press the button'):
    st.write('thx for pressing! u got great taste')
else:
    st.write('button unpressed')

st.subheader("pick a recommendation from me!")
in_mod = st.selectbox(
    "my top three",
    ("kabukichou bad trip", "the song of yoru and asa", "ask and you will recieve"),
)
if in_mod == "kabukichou bad trip":
    set_mod = "10/10 for me, their relationship is so cute"
elif in_mod == "the song of yoru and asa":
    set_mod = "9/10, the sequel is so good!"
elif in_mod == "ask and you will recieve":
    set_mod = "9/10, i love office relationships!"
st.write("my review is:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
