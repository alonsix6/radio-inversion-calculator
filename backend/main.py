"""
API FastAPI para el calculador de inversión en radio.
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
import os
from datetime import datetime

from processor import process_ibope_file, get_summary_stats

app = FastAPI(
    title="Radio Inversión Calculator",
    description="API para calcular inversión estimada en radio a partir de datos de IBOPE",
    version="1.0.0"
)

# CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Radio Inversión Calculator API",
        "version": "1.0.0",
        "endpoints": {
            "POST /process": "Procesar archivo IBOPE y obtener cálculos de inversión",
            "POST /preview": "Vista previa de estadísticas del archivo",
            "GET /health": "Estado del servicio"
        }
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/preview")
async def preview_file(file: UploadFile = File(...)):
    """
    Devuelve estadísticas básicas del archivo sin procesarlo completamente.
    """
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos Excel (.xlsx, .xls)")
    
    try:
        content = await file.read()
        stats = get_summary_stats(content)
        return JSONResponse(content={
            "filename": file.filename,
            "stats": stats
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo: {str(e)}")


@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    """
    Procesa un archivo Excel de IBOPE y devuelve un Excel con los cálculos de inversión.
    
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
        result = process_ibope_file(content, file.filename)
        
        # Generar nombre de archivo de salida
        base_name = os.path.splitext(file.filename)[0]
        output_filename = f"{base_name}_INVERSION_CALCULADA.xlsx"
        
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
