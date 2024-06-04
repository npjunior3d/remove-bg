import streamlit as st
from PIL import Image
from rembg import remove

def remove_bg(imagem, widget):
    img = Image.open(imagem)
    sem_fundo = remove(img)
    widget.title('Sem fundo!')
    widget.image(sem_fundo)

st.title('Remove fundo de imagens!')
imagem = st.file_uploader('Prof. Ricardo Roson - Colégio Litteratus')

col_a, col_b = st.columns(2)

if imagem:
    result = st.button(
        'Remover Fundo',
        type='primary',
        on_click=remove_bg,
        args=(imagem, col_b)
    )
    col_a.title('Imagem original')
    col_a.image(imagem)
else:
    st.warning('Ainda não temos uma imagem!')
