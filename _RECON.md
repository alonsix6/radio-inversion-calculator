# Reconocimiento: Radio Inversión Calculator
Fecha: 2026-01-07

---

## 1. Estructura del Proyecto

```
radio-inversion-calculator/
├── .git/
├── .gitignore
├── README.md
├── netlify.toml
├── backend/
│   ├── .python-version
│   ├── requirements.txt
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── radio_config.py
│   │   └── tv_config.py
│   └── processors/
│       ├── __init__.py
│       ├── radio_processor.py
│       └── tv_processor.py
└── frontend/
    ├── index.html
    ├── app.js
    └── styles.css
```

**Total líneas de código:** ~3,594

---

## 2. Stack Tecnológico

```
STACK:
├── Lenguaje Backend: Python 3.12
├── Framework Backend: FastAPI 0.115.5
├── Servidor ASGI: Uvicorn 0.32.1
├── Lenguaje Frontend: JavaScript (Vanilla)
├── Framework Frontend: Ninguno (HTML/CSS/JS puro)
├── Procesamiento Datos: Pandas 2.2.3 + OpenPyXL 3.1.5
├── Base de datos: Ninguna (datos hardcodeados en config)
├── Auth: Ninguna
└── Deploy:
    ├── Backend: Railway (railway.app)
    └── Frontend: Netlify (configurado en netlify.toml)
```

---

## 3. Archivos Clave

### Backend

| Archivo | Descripción |
|---------|-------------|
| `backend/main.py` | API FastAPI con endpoints para Radio y TV (398 líneas) |
| `backend/config/radio_config.py` | CPM, rankings CPI de emisoras de radio (159 líneas) |
| `backend/config/tv_config.py` | CPM/CPR, ratings de canales de TV (484 líneas) |
| `backend/processors/radio_processor.py` | Procesa Excel IBOPE y calcula inversión radio (178 líneas) |
| `backend/processors/tv_processor.py` | Procesa Excel Instar y calcula inversión TV (221 líneas) |
| `backend/requirements.txt` | Dependencias Python |
| `backend/.python-version` | Especifica Python 3.12 |

### Frontend

| Archivo | Descripción |
|---------|-------------|
| `frontend/index.html` | UI con tabs para Radio y TV, modals de rankings (430 líneas) |
| `frontend/app.js` | Lógica de upload, procesamiento y descarga (708 líneas) |
| `frontend/styles.css` | Estilos dark theme, responsive (1013 líneas) |

### Configuración

| Archivo | Descripción |
|---------|-------------|
| `netlify.toml` | Config de deploy Netlify (frontend) |
| `.gitignore` | Ignora archivos Python, IDE, Excel de prueba |
| `README.md` | Documentación del proyecto |

---

## 4. Dependencias

### Backend (requirements.txt)

| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| fastapi | 0.115.5 | Framework API REST |
| uvicorn | 0.32.1 | Servidor ASGI para FastAPI |
| python-multipart | 0.0.17 | Manejo de uploads de archivos |
| pandas | 2.2.3 | Procesamiento de datos tabular |
| openpyxl | 3.1.5 | Lectura/escritura de archivos Excel |

### Frontend

| Dependencia | Tipo | Propósito |
|-------------|------|-----------|
| DM Sans (Google Fonts) | CDN | Tipografía principal |
| Vanilla JS | Nativo | Sin frameworks, JS puro |

---

## 5. Propósito de la Herramienta

### ¿Qué hace esta herramienta?

Calculadora de inversión publicitaria estimada para medios tradicionales (Radio y TV) en el mercado peruano. Procesa archivos Excel exportados de IBOPE (radio) e Instar (TV), aplica fórmulas de CPM/CPR y rankings de audiencia, y genera reportes Excel con cálculos de inversión desglosados por marca, tipo de pauta, emisora/canal y período.

### ¿Quién la usa?

- **Media Planners** de la agencia Reset / The Lab
- **Analistas de medios** del cliente Laureate (universidades)
- Target específico: análisis competitivo de inversión publicitaria en el segmento educación superior

### ¿Qué recibe?

**Radio (IBOPE):**
- Excel con columnas: MARCA, TIPO, EMISORA/SITE, MES, AÑO, Suma de SPOTS

**TV (Instar):**
- Excel con columnas: MARCA, TIPO COMERCIAL, CANAL, MES, AÑO, TOTAL SPOTS, DURACIÓN, GRP#, GRP%

### ¿Qué produce?

Excel de salida con múltiples hojas:
1. **Detalle** - Todas las filas con cálculos de impactos e inversión
2. **Resumen por Marca** - Totales agregados por anunciante
3. **Resumen por Tipo** - Desglose SPOT/MENCIÓN/P&D (radio) o SPOT/BANNER/L/MENCIÓN (TV)
4. **Resumen por Mes** - Evolución mensual
5. **Resumen por Emisora/Canal** - Distribución por medio

---

## 6. Endpoints API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Info de la API |
| GET | `/health` | Health check |
| POST | `/process/radio` | Procesa archivo IBOPE |
| POST | `/process/tv` | Procesa archivo Instar |
| POST | `/preview/radio` | Preview de archivo radio |
| POST | `/preview/tv` | Preview de archivo TV |
| GET | `/rankings/radio` | Rankings CPI radio |
| GET | `/rankings/tv` | Ratings TV |
| GET | `/template/radio` | Descarga plantilla radio |
| GET | `/template/tv` | Descarga plantilla TV |
| POST | `/process` | Backwards compatible (radio) |
| GET | `/rankings` | Backwards compatible (radio) |

---

## 7. Fórmulas de Cálculo

### Radio
```
Impactos = Spots × Ranking_Miles
Inversión (S/) = Impactos × CPM
```

CPM calibrados con optimización (mínimos cuadrados) vs data SEMCO 2023-2025:
- SPOT: S/ 16.30
- MENCIÓN: S/ 81.40
- P&D: S/ 181.80

### TV
```
SPOTS: Inversión = GRP% × CPR × Segundos
Otros: Inversión = GRP# × CPM
```

CPR varía por canal (ej: Latina S/120.5, América S/115.0, ATV S/95.0)

---

## 8. Datos Hardcodeados

### Radio Rankings (CPI)
- **2023:** Septiembre (23 emisoras)
- **2024:** Julio (23 emisoras)
- **2025:** Julio (24 emisoras)
- Target: H+M 15-24 ABC Lima

### TV Ratings (Instar)
- **2024:** Enero a Diciembre (10 canales)
- **2025:** Enero a Noviembre (11 canales)

---

## 9. Arquitectura

```
┌─────────────────┐     ┌─────────────────┐
│   Frontend      │     │   Backend       │
│   (Netlify)     │────▶│   (Railway)     │
│                 │     │                 │
│  HTML/CSS/JS    │     │  FastAPI        │
│  Vanilla        │     │  Python 3.12   │
└─────────────────┘     └─────────────────┘
        │                       │
        │                       ▼
        │               ┌───────────────┐
        │               │  Processors   │
        │               │  radio/tv     │
        │               └───────────────┘
        │                       │
        ▼                       ▼
┌─────────────────┐     ┌───────────────┐
│  Upload Excel   │     │  Config       │
│  (IBOPE/Instar) │     │  CPM/Rankings │
└─────────────────┘     └───────────────┘
```

---

## 10. Notas Adicionales

- **Sin base de datos:** Todos los rankings y CPM están hardcodeados en archivos Python
- **API pública:** CORS habilitado para todos los orígenes (`*`)
- **Versión actual:** 2.0.0 (soporta Radio + TV)
- **Mantenimiento:** Actualizar `config/radio_config.py` y `config/tv_config.py` cuando salgan nuevos estudios de CPI/ratings
- **Cálculos estimados:** Los valores son aproximaciones basadas en CPM promedio del mercado
