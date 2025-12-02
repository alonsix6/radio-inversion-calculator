# Radio Inversión Calculator

Herramienta para calcular inversión estimada en radio a partir de datos de IBOPE, usando CPM configurados y rankings de CPI.

## 📋 Descripción

Esta herramienta procesa archivos Excel exportados de tablas dinámicas de IBOPE y calcula automáticamente:
- Impactos (Spots × Ranking × 1000)
- Inversión estimada (Impactos × CPM / 1000)

Los resultados se entregan en un Excel con múltiples hojas de resumen.

## 🏗️ Estructura del Proyecto

```
radio-inversion-calculator/
├── backend/
│   ├── main.py              # API FastAPI
│   ├── processor.py         # Lógica de procesamiento
│   ├── data/
│   │   └── config.py        # CPM, Rankings, Mapeos
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── README.md
```

## 🚀 Deploy

### Backend (Railway o Render)

1. **Railway (recomendado):**
   ```bash
   # Instalar Railway CLI
   npm install -g @railway/cli
   
   # Login
   railway login
   
   # Desde la carpeta backend/
   cd backend
   railway init
   railway up
   ```

2. **Render:**
   - Conectar repo de GitHub
   - Crear nuevo Web Service
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend (Netlify)

1. Conectar repo de GitHub a Netlify
2. Configurar:
   - Base directory: `frontend`
   - Publish directory: `frontend`
3. **IMPORTANTE:** Actualizar `API_URL` en `app.js` con la URL real del backend

## 💻 Desarrollo Local

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
API disponible en http://localhost:8000

### Frontend
```bash
cd frontend
# Usar cualquier servidor HTTP local
python -m http.server 3000
# o
npx serve
```
Frontend disponible en http://localhost:3000

## 📊 Formato de Archivo de Entrada

El Excel de IBOPE debe tener estas columnas:

| Columna | Descripción |
|---------|-------------|
| MARCA | Nombre de la universidad (ej: UNIV TECNOLOGICA DEL PERU) |
| TIPO | Tipo de pauta (SPOT, MENCION, DESP.PROGRAMA, etc.) |
| EMISORA/SITE | Nombre de la emisora (ej: MODA FM) |
| MES | Mes en texto (ej: marzo, abril) |
| AÑO | Año numérico (ej: 2024, 2025) |
| Suma de SPOTS | Cantidad de spots |

## ⚙️ Configuración

### CPM (en `backend/data/config.py`)

```python
CPM_CONFIG = {
    "SPOT": 11.6,
    "MENCION": 39.8,
    "P/D": 1.74
}
```

### Rankings de CPI

Los rankings están en `backend/data/config.py`. Para actualizar:

1. Agregar nuevos registros al diccionario `RANKINGS`:
```python
RANKINGS = {
    # ...
    (2026, "Marzo", "MODA FM"): 400.0,  # Nuevo ranking
    # ...
}
```

2. Redesplegar el backend

## 📈 Fórmulas de Cálculo

```
Impactos = Spots × Ranking_Miles × 1000
Inversión (S/) = Impactos × CPM / 1000
```

Si no existe el mes exacto de ranking, se usa el promedio anual de la emisora.

## 🔧 Mantenimiento

### Actualizar Rankings de CPI

Cuando salgan nuevos estudios de CPI:

1. Editar `backend/data/config.py`
2. Agregar nuevos registros al diccionario `RANKINGS`
3. Commit y push
4. El deploy se actualiza automáticamente (si está configurado CI/CD)

### Agregar nuevas emisoras

Si aparecen nuevas emisoras en IBOPE que no están en los rankings:
1. Agregar la emisora al diccionario `RANKINGS` con sus valores por mes
2. Asegurar que el nombre coincida exactamente con el de IBOPE

## 📝 Notas

- Los cálculos son **estimados** basados en CPM promedio
- El target de los rankings es H+M 15-24 ABC Lima
- Si una emisora no tiene ranking, el sistema devuelve 0 para esa combinación

## 👥 Créditos

Desarrollado por **The Lab** (Reset) para el proyecto Laureate.
