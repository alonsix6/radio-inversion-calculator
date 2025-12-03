/**
 * Media Investment Calculator - Frontend Logic
 * Supports Radio (IBOPE) and TV (Instar) processing
 */

// Configuration
const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000'
    : 'https://radio-inversion-calculator-production.up.railway.app';

// ==================== TAB MANAGEMENT ====================
const tabs = document.querySelectorAll('.tab');
const tabContents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const targetTab = tab.dataset.tab;

        // Update tab buttons
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        // Update tab content
        tabContents.forEach(content => {
            content.classList.remove('active');
            if (content.id === `${targetTab}Content`) {
                content.classList.add('active');
            }
        });
    });
});

// ==================== RADIO FUNCTIONALITY ====================
const radioState = {
    selectedFile: null,
    processedBlob: null,
    processedFileName: null,
    rankingsData: null
};

// Radio DOM Elements
const uploadZoneRadio = document.getElementById('uploadZoneRadio');
const fileInputRadio = document.getElementById('fileInputRadio');
const selectBtnRadio = document.getElementById('selectBtnRadio');
const uploadProgressRadio = document.getElementById('uploadProgressRadio');
const filePreviewRadio = document.getElementById('filePreviewRadio');
const fileNameRadio = document.getElementById('fileNameRadio');
const fileStatsRadio = document.getElementById('fileStatsRadio');
const removeFileRadio = document.getElementById('removeFileRadio');
const actionsRadio = document.getElementById('actionsRadio');
const processBtnRadio = document.getElementById('processBtnRadio');
const resultsCardRadio = document.getElementById('resultsCardRadio');
const downloadBtnRadio = document.getElementById('downloadBtnRadio');
const newFileBtnRadio = document.getElementById('newFileBtnRadio');
const errorCardRadio = document.getElementById('errorCardRadio');
const errorMessageRadio = document.getElementById('errorMessageRadio');
const retryBtnRadio = document.getElementById('retryBtnRadio');

// Radio Event Listeners
selectBtnRadio.addEventListener('click', (e) => {
    e.stopPropagation();
    fileInputRadio.click();
});

uploadZoneRadio.addEventListener('click', () => {
    if (!radioState.selectedFile) {
        fileInputRadio.click();
    }
});

fileInputRadio.addEventListener('change', (e) => handleFileSelectRadio(e));

uploadZoneRadio.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadZoneRadio.classList.add('dragover');
});

uploadZoneRadio.addEventListener('dragleave', () => {
    uploadZoneRadio.classList.remove('dragover');
});

uploadZoneRadio.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadZoneRadio.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileRadio(files[0]);
    }
});

removeFileRadio.addEventListener('click', resetUploadRadio);
processBtnRadio.addEventListener('click', processFileRadio);
downloadBtnRadio.addEventListener('click', downloadResultRadio);
newFileBtnRadio.addEventListener('click', resetAllRadio);
retryBtnRadio.addEventListener('click', resetAllRadio);

// Radio Functions
function handleFileSelectRadio(e) {
    const file = e.target.files[0];
    if (file) {
        handleFileRadio(file);
    }
}

function handleFileRadio(file) {
    if (!file.name.endsWith('.xlsx') && !file.name.endsWith('.xls')) {
        showErrorRadio('Solo se aceptan archivos Excel (.xlsx, .xls)');
        return;
    }
    radioState.selectedFile = file;
    showFilePreviewRadio(file);
}

function showFilePreviewRadio(file) {
    fileNameRadio.textContent = file.name;
    fileStatsRadio.textContent = `${formatFileSize(file.size)}`;

    uploadZoneRadio.querySelector('.upload-content').hidden = true;
    filePreviewRadio.hidden = false;
    actionsRadio.hidden = false;
    resultsCardRadio.hidden = true;
    errorCardRadio.hidden = true;
}

function resetUploadRadio() {
    radioState.selectedFile = null;
    fileInputRadio.value = '';
    uploadZoneRadio.querySelector('.upload-content').hidden = false;
    filePreviewRadio.hidden = true;
    actionsRadio.hidden = true;
}

function resetAllRadio() {
    resetUploadRadio();
    radioState.processedBlob = null;
    radioState.processedFileName = null;
    resultsCardRadio.hidden = true;
    errorCardRadio.hidden = true;
}

async function processFileRadio() {
    if (!radioState.selectedFile) return;

    uploadZoneRadio.querySelector('.upload-content').hidden = true;
    filePreviewRadio.hidden = true;
    actionsRadio.hidden = true;
    uploadProgressRadio.hidden = false;
    errorCardRadio.hidden = true;

    try {
        const formData = new FormData();
        formData.append('file', radioState.selectedFile);

        const response = await fetch(`${API_URL}/process/radio`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Error procesando el archivo');
        }

        radioState.processedBlob = await response.blob();
        const contentDisposition = response.headers.get('Content-Disposition');
        radioState.processedFileName = contentDisposition
            ? contentDisposition.split('filename=')[1]?.replace(/"/g, '')
            : `${radioState.selectedFile.name.replace('.xlsx', '')}_INVERSION_RADIO.xlsx`;

        uploadProgressRadio.hidden = true;
        resultsCardRadio.hidden = false;

    } catch (error) {
        console.error('Error:', error);
        showErrorRadio(error.message);
    }
}

function showErrorRadio(message) {
    uploadProgressRadio.hidden = true;
    uploadZoneRadio.querySelector('.upload-content').hidden = false;
    filePreviewRadio.hidden = true;
    actionsRadio.hidden = true;
    errorCardRadio.hidden = false;
    errorMessageRadio.textContent = message;
}

function downloadResultRadio() {
    if (!radioState.processedBlob) return;

    const url = URL.createObjectURL(radioState.processedBlob);
    const a = document.createElement('a');
    a.href = url;
    a.download = radioState.processedFileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// ==================== TV FUNCTIONALITY ====================
const tvState = {
    selectedFile: null,
    processedBlob: null,
    processedFileName: null,
    rankingsData: null
};

// TV DOM Elements
const uploadZoneTV = document.getElementById('uploadZoneTV');
const fileInputTV = document.getElementById('fileInputTV');
const selectBtnTV = document.getElementById('selectBtnTV');
const uploadProgressTV = document.getElementById('uploadProgressTV');
const filePreviewTV = document.getElementById('filePreviewTV');
const fileNameTV = document.getElementById('fileNameTV');
const fileStatsTV = document.getElementById('fileStatsTV');
const removeFileTV = document.getElementById('removeFileTV');
const actionsTV = document.getElementById('actionsTV');
const processBtnTV = document.getElementById('processBtnTV');
const resultsCardTV = document.getElementById('resultsCardTV');
const downloadBtnTV = document.getElementById('downloadBtnTV');
const newFileBtnTV = document.getElementById('newFileBtnTV');
const errorCardTV = document.getElementById('errorCardTV');
const errorMessageTV = document.getElementById('errorMessageTV');
const retryBtnTV = document.getElementById('retryBtnTV');

// TV Event Listeners
selectBtnTV.addEventListener('click', (e) => {
    e.stopPropagation();
    fileInputTV.click();
});

uploadZoneTV.addEventListener('click', () => {
    if (!tvState.selectedFile) {
        fileInputTV.click();
    }
});

fileInputTV.addEventListener('change', (e) => handleFileSelectTV(e));

uploadZoneTV.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadZoneTV.classList.add('dragover');
});

uploadZoneTV.addEventListener('dragleave', () => {
    uploadZoneTV.classList.remove('dragover');
});

uploadZoneTV.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadZoneTV.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileTV(files[0]);
    }
});

removeFileTV.addEventListener('click', resetUploadTV);
processBtnTV.addEventListener('click', processFileTV);
downloadBtnTV.addEventListener('click', downloadResultTV);
newFileBtnTV.addEventListener('click', resetAllTV);
retryBtnTV.addEventListener('click', resetAllTV);

// TV Functions
function handleFileSelectTV(e) {
    const file = e.target.files[0];
    if (file) {
        handleFileTV(file);
    }
}

function handleFileTV(file) {
    if (!file.name.endsWith('.xlsx') && !file.name.endsWith('.xls')) {
        showErrorTV('Solo se aceptan archivos Excel (.xlsx, .xls)');
        return;
    }
    tvState.selectedFile = file;
    showFilePreviewTV(file);
}

function showFilePreviewTV(file) {
    fileNameTV.textContent = file.name;
    fileStatsTV.textContent = `${formatFileSize(file.size)}`;

    uploadZoneTV.querySelector('.upload-content').hidden = true;
    filePreviewTV.hidden = false;
    actionsTV.hidden = false;
    resultsCardTV.hidden = true;
    errorCardTV.hidden = true;
}

function resetUploadTV() {
    tvState.selectedFile = null;
    fileInputTV.value = '';
    uploadZoneTV.querySelector('.upload-content').hidden = false;
    filePreviewTV.hidden = true;
    actionsTV.hidden = true;
}

function resetAllTV() {
    resetUploadTV();
    tvState.processedBlob = null;
    tvState.processedFileName = null;
    resultsCardTV.hidden = true;
    errorCardTV.hidden = true;
}

async function processFileTV() {
    if (!tvState.selectedFile) return;

    uploadZoneTV.querySelector('.upload-content').hidden = true;
    filePreviewTV.hidden = true;
    actionsTV.hidden = true;
    uploadProgressTV.hidden = false;
    errorCardTV.hidden = true;

    try {
        const formData = new FormData();
        formData.append('file', tvState.selectedFile);

        const response = await fetch(`${API_URL}/process/tv`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Error procesando el archivo');
        }

        tvState.processedBlob = await response.blob();
        const contentDisposition = response.headers.get('Content-Disposition');
        tvState.processedFileName = contentDisposition
            ? contentDisposition.split('filename=')[1]?.replace(/"/g, '')
            : `${tvState.selectedFile.name.replace('.xlsx', '')}_INVERSION_TV.xlsx`;

        uploadProgressTV.hidden = true;
        resultsCardTV.hidden = false;

    } catch (error) {
        console.error('Error:', error);
        showErrorTV(error.message);
    }
}

function showErrorTV(message) {
    uploadProgressTV.hidden = true;
    uploadZoneTV.querySelector('.upload-content').hidden = false;
    filePreviewTV.hidden = true;
    actionsTV.hidden = true;
    errorCardTV.hidden = false;
    errorMessageTV.textContent = message;
}

function downloadResultTV() {
    if (!tvState.processedBlob) return;

    const url = URL.createObjectURL(tvState.processedBlob);
    const a = document.createElement('a');
    a.href = url;
    a.download = tvState.processedFileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// ==================== RADIO RANKINGS MODAL ====================
const viewRankingsBtnRadio = document.getElementById('viewRankingsBtnRadio');
const rankingsModalRadio = document.getElementById('rankingsModalRadio');
const closeModalBtnRadio = document.getElementById('closeModalBtnRadio');
const modalStatsRadio = document.getElementById('modalStatsRadio');
const rankingsContentRadio = document.getElementById('rankingsContentRadio');
const yearFilterRadio = document.getElementById('yearFilterRadio');
const monthFilterRadio = document.getElementById('monthFilterRadio');

viewRankingsBtnRadio.addEventListener('click', openRankingsModalRadio);
closeModalBtnRadio.addEventListener('click', closeRankingsModalRadio);
rankingsModalRadio.addEventListener('click', (e) => {
    if (e.target === rankingsModalRadio) closeRankingsModalRadio();
});
yearFilterRadio.addEventListener('change', renderRankingsRadio);
monthFilterRadio.addEventListener('change', renderRankingsRadio);

async function openRankingsModalRadio() {
    rankingsModalRadio.hidden = false;
    document.body.style.overflow = 'hidden';

    if (!radioState.rankingsData) {
        await loadRankingsRadio();
    } else {
        renderRankingsRadio();
    }
}

function closeRankingsModalRadio() {
    rankingsModalRadio.hidden = true;
    document.body.style.overflow = '';
}

async function loadRankingsRadio() {
    try {
        const response = await fetch(`${API_URL}/rankings/radio`);
        if (!response.ok) throw new Error('Error cargando rankings');

        radioState.rankingsData = await response.json();

        modalStatsRadio.innerHTML = `
            <div class="modal-stat">
                <span class="modal-stat-value">${radioState.rankingsData.stats.total_registros}</span>
                <span class="modal-stat-label">Registros</span>
            </div>
            <div class="modal-stat">
                <span class="modal-stat-value">${radioState.rankingsData.stats.emisoras_unicas}</span>
                <span class="modal-stat-label">Emisoras</span>
            </div>
            <div class="modal-stat">
                <span class="modal-stat-value">${radioState.rankingsData.stats.años.length}</span>
                <span class="modal-stat-label">Años</span>
            </div>
        `;

        yearFilterRadio.innerHTML = radioState.rankingsData.stats.años
            .sort((a, b) => b - a)
            .map((year, i) => `<option value="${year}" ${i === 0 ? 'selected' : ''}>${year}</option>`)
            .join('');

        updateMonthFilterRadio();
        renderRankingsRadio();

    } catch (error) {
        console.error('Error loading rankings:', error);
        rankingsContentRadio.innerHTML = `
            <div class="loading-rankings">
                <p>Error cargando rankings. Intenta de nuevo.</p>
            </div>
        `;
    }
}

function updateMonthFilterRadio() {
    const selectedYear = yearFilterRadio.value;
    const months = Object.keys(radioState.rankingsData.rankings[selectedYear] || {});

    const monthOrder = ['Marzo', 'Junio', 'Agosto', 'Septiembre', 'Noviembre'];
    months.sort((a, b) => monthOrder.indexOf(a) - monthOrder.indexOf(b));

    monthFilterRadio.innerHTML = `
        <option value="">Todos los meses</option>
        ${months.map(month => `<option value="${month}">${month}</option>`).join('')}
    `;
}

function renderRankingsRadio() {
    const selectedYear = yearFilterRadio.value;
    const selectedMonth = monthFilterRadio.value;

    if (!radioState.rankingsData || !radioState.rankingsData.rankings[selectedYear]) {
        rankingsContentRadio.innerHTML = '<p>No hay datos disponibles</p>';
        return;
    }

    updateMonthFilterRadio();

    const yearData = radioState.rankingsData.rankings[selectedYear];
    const monthsToShow = selectedMonth ? [selectedMonth] : Object.keys(yearData);

    const monthOrder = ['Marzo', 'Junio', 'Agosto', 'Septiembre', 'Noviembre'];
    monthsToShow.sort((a, b) => monthOrder.indexOf(a) - monthOrder.indexOf(b));

    let html = '';

    monthsToShow.forEach(month => {
        const emisoras = yearData[month];
        if (!emisoras) return;

        html += `
            <div class="rankings-section">
                <div class="rankings-section-title">${month} ${selectedYear}</div>
                <table class="rankings-table">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Emisora</th>
                            <th style="text-align: right">Rating (miles)</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${emisoras.map((e, i) => `
                            <tr>
                                <td class="rank-position">${i + 1}</td>
                                <td class="rank-emisora">${e.emisora}</td>
                                <td class="rank-value">${e.ranking.toFixed(1)}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    });

    rankingsContentRadio.innerHTML = html;
}

// ==================== TV RANKINGS MODAL ====================
const viewRankingsBtnTV = document.getElementById('viewRankingsBtnTV');
const rankingsModalTV = document.getElementById('rankingsModalTV');
const closeModalBtnTV = document.getElementById('closeModalBtnTV');
const modalStatsTV = document.getElementById('modalStatsTV');
const rankingsContentTV = document.getElementById('rankingsContentTV');
const yearFilterTV = document.getElementById('yearFilterTV');
const monthFilterTV = document.getElementById('monthFilterTV');

viewRankingsBtnTV.addEventListener('click', openRankingsModalTV);
closeModalBtnTV.addEventListener('click', closeRankingsModalTV);
rankingsModalTV.addEventListener('click', (e) => {
    if (e.target === rankingsModalTV) closeRankingsModalTV();
});
yearFilterTV.addEventListener('change', renderRankingsTV);
monthFilterTV.addEventListener('change', renderRankingsTV);

async function openRankingsModalTV() {
    rankingsModalTV.hidden = false;
    document.body.style.overflow = 'hidden';

    if (!tvState.rankingsData) {
        await loadRankingsTV();
    } else {
        renderRankingsTV();
    }
}

function closeRankingsModalTV() {
    rankingsModalTV.hidden = true;
    document.body.style.overflow = '';
}

async function loadRankingsTV() {
    try {
        const response = await fetch(`${API_URL}/rankings/tv`);
        if (!response.ok) throw new Error('Error cargando ratings');

        tvState.rankingsData = await response.json();

        modalStatsTV.innerHTML = `
            <div class="modal-stat">
                <span class="modal-stat-value">${tvState.rankingsData.stats.total_registros}</span>
                <span class="modal-stat-label">Registros</span>
            </div>
            <div class="modal-stat">
                <span class="modal-stat-value">${tvState.rankingsData.stats.canales_unicos}</span>
                <span class="modal-stat-label">Canales</span>
            </div>
            <div class="modal-stat">
                <span class="modal-stat-value">${tvState.rankingsData.stats.años.length}</span>
                <span class="modal-stat-label">Años</span>
            </div>
        `;

        yearFilterTV.innerHTML = tvState.rankingsData.stats.años
            .sort((a, b) => b - a)
            .map((year, i) => `<option value="${year}" ${i === 0 ? 'selected' : ''}>${year}</option>`)
            .join('');

        updateMonthFilterTV();
        renderRankingsTV();

    } catch (error) {
        console.error('Error loading ratings:', error);
        rankingsContentTV.innerHTML = `
            <div class="loading-rankings">
                <p>Error cargando ratings. Intenta de nuevo.</p>
            </div>
        `;
    }
}

function updateMonthFilterTV() {
    const selectedYear = yearFilterTV.value;
    const months = Object.keys(tvState.rankingsData.ratings[selectedYear] || {});

    const monthOrder = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    months.sort((a, b) => monthOrder.indexOf(a) - monthOrder.indexOf(b));

    monthFilterTV.innerHTML = `
        <option value="">Todos los meses</option>
        ${months.map(month => `<option value="${month}">${month}</option>`).join('')}
    `;
}

function renderRankingsTV() {
    const selectedYear = yearFilterTV.value;
    const selectedMonth = monthFilterTV.value;

    if (!tvState.rankingsData || !tvState.rankingsData.ratings[selectedYear]) {
        rankingsContentTV.innerHTML = '<p>No hay datos disponibles</p>';
        return;
    }

    updateMonthFilterTV();

    const yearData = tvState.rankingsData.ratings[selectedYear];
    const monthsToShow = selectedMonth ? [selectedMonth] : Object.keys(yearData);

    const monthOrder = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    monthsToShow.sort((a, b) => monthOrder.indexOf(a) - monthOrder.indexOf(b));

    let html = '';

    monthsToShow.forEach(month => {
        const canales = yearData[month];
        if (!canales) return;

        html += `
            <div class="rankings-section">
                <div class="rankings-section-title">${month} ${selectedYear}</div>
                <table class="rankings-table">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Canal</th>
                            <th style="text-align: right">Rating (puntos)</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${canales.map((c, i) => `
                            <tr>
                                <td class="rank-position">${i + 1}</td>
                                <td class="rank-emisora">${c.canal}</td>
                                <td class="rank-value">${c.rating.toFixed(1)}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    });

    rankingsContentTV.innerHTML = html;
}

// ==================== UTILITY FUNCTIONS ====================
function formatFileSize(bytes) {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}

// Keyboard support for modals
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (!rankingsModalRadio.hidden) closeRankingsModalRadio();
        if (!rankingsModalTV.hidden) closeRankingsModalTV();
    }
});

// ==================== TEMPLATE DOWNLOADS ====================
const downloadTemplateRadio = document.getElementById('downloadTemplateRadio');
const downloadTemplateTV = document.getElementById('downloadTemplateTV');

downloadTemplateRadio.addEventListener('click', () => downloadTemplate('radio'));
downloadTemplateTV.addEventListener('click', () => downloadTemplate('tv'));

async function downloadTemplate(type) {
    try {
        const response = await fetch(`${API_URL}/template/${type}`);
        if (!response.ok) {
            throw new Error('Error descargando plantilla');
        }

        const blob = await response.blob();
        const contentDisposition = response.headers.get('Content-Disposition');
        const filename = contentDisposition
            ? contentDisposition.split('filename=')[1]?.replace(/"/g, '')
            : `Plantilla_${type === 'radio' ? 'Radio_IBOPE' : 'TV_Instar'}.xlsx`;

        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    } catch (error) {
        console.error('Error downloading template:', error);
        alert('Error al descargar la plantilla. Verifica tu conexión.');
    }
}

// Check API health on load
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (response.ok) {
            console.log('API connected - v2.0.0 (Radio + TV)');
        }
    } catch (error) {
        console.warn('API not available. Make sure the backend is running.');
    }
}

// Initialize
checkAPIHealth();
