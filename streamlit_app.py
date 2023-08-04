import streamlit as st
import pandas as pd
import io
import re

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
    # Encontrar todas las marcas de segmentación de "prompt" y "completion"
    prompt_positions = [match.start() for match in re.finditer(re.escape(prompt_marker), txt_content)]
    completion_positions = [match.start() for match in re.finditer(re.escape(completion_marker), txt_content)]

    # Crear listas para las dos columnas
    prompts = []
    completions = []

    # Iterar sobre las posiciones de las marcas de segmentación y separar los prompts y completions
    for i, prompt_pos in enumerate(prompt_positions):
        prompt_end_pos = completion_positions[i] if i < len(completion_positions) else len(txt_content)
        prompt_text = txt_content[prompt_pos + len(prompt_marker):prompt_end_pos].strip()
        completion_text = txt_content[prompt_end_pos + len(completion_marker):completion_positions[i + 1]].strip() if i + 1 < len(completion_positions) else ""
        prompts.append(prompt_text)
        completions.append(completion_text)

    # Crear el DataFrame con los datos
    df = pd.DataFrame({
        "prompt": prompts,
        "completion": completions
    })

    return df

if __name__ == "__main__":
    main()
