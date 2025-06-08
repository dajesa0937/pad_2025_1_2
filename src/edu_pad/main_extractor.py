import os
from edu_pad.dataweb  import DataWeb
import pandas as pd

def main():
    # Crear la ruta si no existe
    output_dir = "src/edu_pad/static/csv"
    os.makedirs(output_dir, exist_ok=True)

    dataweb = DataWeb()
    list_indicadores = ["DOLA-USD", "EURUSD%3DX", "CL%3DF", "GC%3DF"]
    for indicador in list_indicadores:
        df = dataweb.procesar_indicador_completo(indicador)
        df.to_csv(os.path.join(output_dir, "data_extractor.csv"), index=False, mode="a")

if __name__ == "__main__":
    main()
