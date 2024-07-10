import streamlit as st
from htmlTemplates import css

def download_pdf_ai_medicare():
    # Here you can put the code to generate or fetch the PDF file
    
    with open("AI_medicare_pres.pdf", "rb") as file:
        pdf_bytes = file.read()
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="AI_medicare_pres.pdf",
        mime="application/pdf",
        )
    

# Configuración de la página
st.set_page_config(page_title="AI Medicare Web", page_icon=".")

# Aplicar CSS personalizado
st.write(css, unsafe_allow_html=True)

# Área de título
col1, col2 = st.columns([1,2])
with col1:
    st.image('AI_Medicare_logo.png', width= 150)

with col2:
    st.title('AI Medicare')

st.subheader('Transforming Healthcare with Innovative Artificial Intelligence')

# Mensaje de bienvenida o advertencia
st.warning('Welcome to AI Medicare, where we leverage cutting-edge AI technology to revolutionize healthcare.')

# Descripción adicional
st.markdown("""
AI Medicare is committed to improving healthcare efficiency and patient satisfaction through advanced AI solutions. 
Our services include virtual assistants for customer service, data management tools, and business consulting for healthcare professionals and institutions.
""")

# Botón para más información
if st.button('Learn More'):
    col1, col2 = st.columns(2)

    with col1:
        #st.image("AI_medicare_logo.png", width=100)
        st.markdown('[Chat with us](https://ai-medicare-chat.streamlit.app/)')
    with col2:
        #st.image("AI_medicare_logo.png", width=100)
        if __name__ == "__main__":
            st.write("Click the button below to download the AI Medicare presentation.")
        download_pdf_ai_medicare()

# Pie de página
maps_link = "https://www.google.com/maps?q=Manta,%20Ecuador,%20calle%2016,%20avda%2038"
st.markdown("""
---
**Contact Us:**
- Email: [Contact](mailto:jjusturi@gmail.com)
- Phone: [Whatssap message](https://wa.me/5930993513082?text=info%20acerca%20de%20AI_Medicare
)
- Address: [Ubication on Google Maps](https://www.google.com/maps?q=Manta,%20Ecuador,%20calle%2016%202607,%20avda%2038)

""")
