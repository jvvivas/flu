import streamlit as st

st.title("Hello World")

st.write("Aqui é um testo normal")

st.markdown( 
    """ 
    $$f(x)= x ^2 + 1$$
    :football:
    :angry:
    :smile:
    :heart:
    """
    )

arq = st.file_uploader("Escolhe um arquivo", type=['png','jpeg','mp3','mp4','py'])
if arq:
    st.write(arq.type)
    if arq.type.split("/")[0] == "image":    
        st.image(arq, width=300)
    elif arq.type.split("/")[0] == "audio":
        st.audio(arq)
    elif arq.type.split("/")[0] == "video":
        st.video(arq)
    elif arq.type.split("/")[0] == "text" and (arq.type.split("/")[1] == "x-python"):
        #st.text(arq)
        st.code(arq.read().decode(), language="python")
else:
    st.write("Não tem arquivo")