import streamlit as st
import pandas as pd
import io

def main():
    st.title("Conversor de archivo TXT a Excel")
    st.write("Esta aplicación convierte un archivo de texto con marcas de segmentación de párrafos en un archivo de Excel con dos columnas.")

    # Cargar archivo TXT
    uploaded_file = st.file_uploader("Cargar archivo TXT", type=["txt"])
    if uploaded_file is not None:
        # Leer el contenido del archivo
        txt_content = uploaded_file.read().decode("utf-8")

        # Preguntar al usuario por las marcas de segmentación
        prompt_marker = st.text_input("Introduce la marca de segmentación para 'prompt'")
        completion_marker = st.text_input("Introduce la marca de segmentación para 'completion'")

        # Convertir el texto a un DataFrame de pandas con dos columnas
        df = create_dataframe(txt_content, prompt_marker, completion_marker)

        # Descargar el archivo Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)
        output.seek(0)
        st.download_button("Descargar archivo Excel", data=output, file_name="output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

def create_dataframe(txt_content, prompt_marker, completion_marker):
    # Dividir el texto en párrafos usando las marcas de segmentación
    paragraphs = txt_content.split(completion_marker)

    # Crear listas para las dos columnas
    prompts = []
    completions = []

    # Iterar sobre los párrafos y separar los prompts y completions
    for paragraph in paragraphs:
        parts = paragraph.split(prompt_marker)
        prompts.append(parts[0].strip())
        completions.append(parts[1].strip() if len(parts) > 1 else "")

    # Crear el DataFrame con los datos
    df = pd.DataFrame({
        "prompt": prompts,
        "completion": completions
    })

    return df

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import io

def main():
    st.title("Conversor de archivo TXT a Excel")
    st.write("Esta aplicación convierte un archivo de texto con marcas de segmentación de párrafos en un archivo de Excel con dos columnas.")

    # Cargar archivo TXT
    uploaded_file = st.file_uploader("Cargar archivo TXT", type=["txt"])
    if uploaded_file is not None:
        # Leer el contenido del archivo
        txt_content = uploaded_file.read().decode("utf-8")

        # Preguntar al usuario por las marcas de segmentación
        prompt_marker = st.text_input("Introduce la marca de segmentación para 'prompt'")
        completion_marker = st.text_input("Introduce la marca de segmentación para 'completion'")

        # Convertir el texto a un DataFrame de pandas con dos columnas
        df = create_dataframe(txt_content, prompt_marker, completion_marker)

        # Descargar el archivo Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)
        output.seek(0)
        st.download_button("Descargar archivo Excel", data=output, file_name="output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

def create_dataframe(txt_content, prompt_marker, completion_marker):
    # Dividir el texto en párrafos usando las marcas de segmentación
    paragraphs = txt_content.split(completion_marker)

    # Crear listas para las dos columnas
    prompts = []
    completions = []

    # Iterar sobre los párrafos y separar los prompts y completions
    for paragraph in paragraphs:
        parts = paragraph.split(prompt_marker)
        prompts.append(parts[0].strip())
        completions.append(parts[1].strip() if len(parts) > 1 else "")

    # Crear el DataFrame con los datos
    df = pd.DataFrame({
        "prompt": prompts,
        "completion": completions
    })

    return df

if __name__ == "__main__":
    main()
