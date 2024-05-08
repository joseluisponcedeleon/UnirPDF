import streamlit as st
import PyPDF2
from datetime import datetime

# st.set_page_config(page_title="Unir PDF", page_icon="📎", layout="wide")
st.set_page_config(
    page_title="Unir PDF",  # Título de la pestaña del navegador
    page_icon="📎",         # Icono de la pestaña del navegador
    layout="wide",          # Utiliza el layout ancho
    menu_items={
        'Get Help': None,  # Opcional: Elimina el enlace 'Get Help'
        'Report a bug': None,  # Opcional: Elimina el enlace 'Report a bug'
        'About': None,  # Opcional: Elimina el enlace 'About'
        'Show source code': None  # Omitir para ocultar la opción de "Ver código fuente"
    }
)

# Definición de la función para unir PDFs
def unir_pdfs(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()
    for document in documents:
        pdf_final.append(document)
    pdf_final.write(output_path)
    pdf_final.close()

# FRONT-END
#st.image("assets/pdf.webP")  # Muestra una imagen en la interfaz de usuario
st.image("assets/pdf.webp", width=300)
st.header("¿Necesitas Unir Varios PDFs? ¡Hazlo Aquí!")  # Agrega un encabezado en la interfaz de usuario
st.subheader("Cargue múltiples PDFs para fusionarlos en un único archivo")  # Agrega un subencabezado en la interfaz de usuario

# Crea un área para que el usuario cargue varios archivos PDF
pdf_adjuntos = st.file_uploader("Seleccione los archivos PDF para unir:", accept_multiple_files=True)

# Crea un botón llamado "Unir PDFs"
unir = st.button(label="Unir PDFs")

if unir:
    # Comienza un bloque condicional si se hace clic en el botón "Unir PDFs"
    if len(pdf_adjuntos) <= 1:
        st.warning("Debes adjuntar más de un PDF")  # Muestra una advertencia si se cargaron menos de dos archivos PDF
    else:
        # Inicia un bloque de código si se cargaron al menos dos archivos PDF
        output_pdf = f"pdf_final_{datetime.now().strftime('%d%B%H%M')}.pdf"
        unir_pdfs(output_pdf, pdf_adjuntos)  # Combina los archivos PDF cargados y guarda el resultado en output_pdf
        st.success("Desde aquí puede descargar el PDF final")  # Muestra un mensaje de éxito en la interfaz de usuario
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()  # Abre el archivo PDF final combinado en modo lectura binaria
        st.download_button(label="Descargar PDF final", data=pdf_data, file_name=output_pdf)  # Muestra un botón de descarga para que el usuario pueda descargar el PDF final combinado

# Pie de página con enlace a LinkedIn
st.markdown("""
---
#### Desarrollado por [Luis Ponce de León](https://www.linkedin.com/in/jponcedeleon/)
Sígueme en [LinkedIn](https://www.linkedin.com/in/jponcedeleon/) para más proyectos como este.
""", unsafe_allow_html=True)