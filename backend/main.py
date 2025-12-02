"""
API FastAPI para el calculador de inversión en medios (Radio y TV).
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
import os
from datetime import datetime

from processors.radio_processor import process_radio_file, get_radio_summary_stats
from processors.tv_processor import process_tv_file, get_tv_summary_stats
from config.radio_config import RANKINGS as RANKINGS_RADIO, CPM_CONFIG as CPM_RADIO
from config.tv_config import RANKINGS_TV, CPM_TV, DEFAULT_TV_CPM

app = FastAPI(
    title="Media Inversión Calculator",
    description="API para calcular inversión estimada en radio (IBOPE) y TV (Instar)",
    version="2.0.0"
)

# CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Media Inversión Calculator API",
        "version": "2.0.0",
        "endpoints": {
            "POST /process": "Procesar archivo IBOPE (radio) - backwards compatible",
            "POST /process/radio": "Procesar archivo IBOPE para radio",
            "POST /process/tv": "Procesar archivo Instar para TV",
            "GET /rankings": "Rankings de radio (CPI) - backwards compatible",
            "GET /rankings/radio": "Rankings de radio (CPI)",
            "GET /rankings/tv": "Ratings de TV (Instar)",
            "GET /health": "Estado del servicio"
        }
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


# ============== RADIO ENDPOINTS ==============

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    """
    Procesa un archivo Excel de IBOPE y devuelve un Excel con los cálculos de inversión.
    Endpoint de backwards compatibility - usa /process/radio para nuevas integraciones.
    """
    return await process_radio(file)


@app.post("/process/radio")
async def process_radio(file: UploadFile = File(...)):
    """
    Procesa un archivo Excel de IBOPE y devuelve un Excel con los cálculos de inversión en radio.

    El archivo debe contener las columnas:
    - MARCA
    - TIPO
    - EMISORA/SITE
    - MES
    - AÑO
    - Suma de SPOTS
    """
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")

    try:
        content = await file.read()
        result = process_radio_file(content, file.filename)

        base_name = os.path.splitext(file.filename)[0]
        output_filename = f"{base_name}_INVERSION_RADIO.xlsx"

        return StreamingResponse(
            result,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": f"attachment; filename={output_filename}"
            }
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando archivo: {str(e)}")


@app.post("/preview/radio")
async def preview_radio_file(file: UploadFile = File(...)):
    """
    Devuelve estadísticas básicas del archivo de radio sin procesarlo completamente.
    """
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")

    try:
        content = await file.read()
        stats = get_radio_summary_stats(content)
        return JSONResponse(content={
            "filename": file.filename,
            "type": "radio",
            "stats": stats
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo: {str(e)}")


@app.get("/rankings")
async def get_rankings():
    """
    Devuelve todos los rankings de CPI de radio disponibles.
    Endpoint de backwards compatibility - usa /rankings/radio para nuevas integraciones.
    """
    return await get_radio_rankings()


@app.get("/rankings/radio")
async def get_radio_rankings():
    """
    Devuelve todos los rankings de CPI de radio disponibles, organizados por año y mes.
    """
    rankings_organized = {}

    for (año, mes, emisora), valor in RANKINGS_RADIO.items():
        if año not in rankings_organized:
            rankings_organized[año] = {}
        if mes not in rankings_organized[año]:
            rankings_organized[año][mes] = []
        rankings_organized[año][mes].append({
            "emisora": emisora,
            "ranking": valor
        })

    for año in rankings_organized:
        for mes in rankings_organized[año]:
            rankings_organized[año][mes].sort(key=lambda x: x["ranking"], reverse=True)

    años = sorted(rankings_organized.keys())
    total_registros = len(RANKINGS_RADIO)
    emisoras_unicas = len(set(e for (_, _, e) in RANKINGS_RADIO.keys()))

    return {
        "type": "radio",
        "cpm": CPM_RADIO,
        "rankings": rankings_organized,
        "stats": {
            "años": años,
            "total_registros": total_registros,
            "emisoras_unicas": emisoras_unicas
        }
    }


# ============== TV ENDPOINTS ==============

@app.post("/process/tv")
async def process_tv(file: UploadFile = File(...)):
    """
    Procesa un archivo Excel de Instar y devuelve un Excel con los cálculos de inversión en TV.

    El archivo debe contener las columnas:
    - MARCA
    - TIPO
    - CANAL/SITE (o CANAL)
    - MES
    - AÑO
    - Suma de SPOTS o AVISOS
    - SEGUNDOS (opcional, default 30)
    """
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")

    try:
        content = await file.read()
        result = process_tv_file(content, file.filename)

        base_name = os.path.splitext(file.filename)[0]
        output_filename = f"{base_name}_INVERSION_TV.xlsx"

        return StreamingResponse(
            result,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": f"attachment; filename={output_filename}"
            }
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando archivo: {str(e)}")


@app.post("/preview/tv")
async def preview_tv_file(file: UploadFile = File(...)):
    """
    Devuelve estadísticas básicas del archivo de TV sin procesarlo completamente.
    """
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")

    try:
        content = await file.read()
        stats = get_tv_summary_stats(content)
        return JSONResponse(content={
            "filename": file.filename,
            "type": "tv",
            "stats": stats
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo: {str(e)}")


@app.get("/rankings/tv")
async def get_tv_rankings():
    """
    Devuelve todos los ratings de TV disponibles, organizados por año y mes.
    """
    rankings_organized = {}

    for (año, mes, canal), valor in RANKINGS_TV.items():
        if año not in rankings_organized:
            rankings_organized[año] = {}
        if mes not in rankings_organized[año]:
            rankings_organized[año][mes] = []
        rankings_organized[año][mes].append({
            "canal": canal,
            "rating": valor
        })

    for año in rankings_organized:
        for mes in rankings_organized[año]:
            rankings_organized[año][mes].sort(key=lambda x: x["rating"], reverse=True)

    años = sorted(rankings_organized.keys())
    total_registros = len(RANKINGS_TV)
    canales_unicos = len(set(c for (_, _, c) in RANKINGS_TV.keys()))

    # Organizar CPM/CPR por canal
    cpm_por_canal = {}
    for (canal, tipo), values in CPM_TV.items():
        if canal not in cpm_por_canal:
            cpm_por_canal[canal] = {}
        cpm_por_canal[canal][tipo] = values

    return {
        "type": "tv",
        "cpm_por_canal": cpm_por_canal,
        "default_cpm": DEFAULT_TV_CPM,
        "ratings": rankings_organized,
        "stats": {
            "años": años,
            "total_registros": total_registros,
            "canales_unicos": canales_unicos
        }
    }


# ============== BACKWARDS COMPATIBILITY ==============

@app.post("/preview")
async def preview_file(file: UploadFile = File(...)):
    """
    Devuelve estadísticas básicas del archivo sin procesarlo completamente.
    Endpoint de backwards compatibility - usa /preview/radio o /preview/tv.
    """
    return await preview_radio_file(file)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
