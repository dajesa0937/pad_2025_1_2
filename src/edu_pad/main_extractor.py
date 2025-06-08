from edu_pad.dataweb import DataWeb
import pandas as pd
import os

def main():
    dataweb = DataWeb()
    list_indicadores = ["DOLA-USD", "EURUSD%3DX", "CL%3DF", "GC%3DF"]

    # Crear carpeta si no existe
    output_dir = "src/edu_pad/static/csv"
    os.makedirs(output_dir, exist_ok=True)

    for indicador in list_indicadores:
        df = dataweb.procesar_indicador_completo(indicador)
        output_path = os.path.join(output_dir, "data_extractor.csv")
        df.to_csv(output_path, index=False, mode="a")

if __name__ == "__main__":
    main()
