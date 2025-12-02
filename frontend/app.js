/**
 * Radio Inversión Calculator - Frontend Logic
 */

// Configuration
const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000'
    : 'https://radio-inversion-calculator-production.up.railway.app';  // URL pública de Railway

// DOM Elements
const uploadZone = document.getElementById('uploadZone');
const fileInput = document.getElementById('fileInput');
const selectBtn = document.getElementById('selectBtn');
const uploadProgress = document.getElementById('uploadProgress');
const filePreview = document.getElementById('filePreview');
const fileName = document.getElementById('fileName');
const fileStats = document.getElementById('fileStats');
const removeFile = document.getElementById('removeFile');
const actions = document.getElementById('actions');
const processBtn = document.getElementById('processBtn');
const resultsCard = document.getElementById('resultsCard');
const downloadBtn = document.getElementById('downloadBtn');
const newFileBtn = document.getElementById('newFileBtn');
const errorCard = document.getElementById('errorCard');
const errorMessage = document.getElementById('errorMessage');
const retryBtn = document.getElementById('retryBtn');

// State
let selectedFile = null;
let processedBlob = null;
let processedFileName = null;

// Event Listeners
selectBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    fileInput.click();
});

uploadZone.addEventListener('click', () => {
    if (!selectedFile) {
        fileInput.click();
    }
});

fileInput.addEventListener('change', handleFileSelect);

uploadZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadZone.classList.add('dragover');
});

uploadZone.addEventListener('dragleave', () => {
    uploadZone.classList.remove('dragover');
});

uploadZone.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
});

removeFile.addEventListener('click', resetUpload);
processBtn.addEventListener('click', processFile);
downloadBtn.addEventListener('click', downloadResult);
newFileBtn.addEventListener('click', resetAll);
retryBtn.addEventListener('click', resetAll);

// Functions
function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        handleFile(file);
    }
}

function handleFile(file) {
    // Validate file type
    if (!file.name.endsWith('.xlsx') && !file.name.endsWith('.xls')) {
        showError('Solo se aceptan archivos Excel (.xlsx, .xls)');
        return;
    }

    selectedFile = file;
    showFilePreview(file);
}

function showFilePreview(file) {
    fileName.textContent = file.name;
    fileStats.textContent = `${formatFileSize(file.size)}`;
    
    // Hide upload content, show preview
    document.querySelector('.upload-content').hidden = true;
    filePreview.hidden = false;
    actions.hidden = false;
    resultsCard.hidden = true;
    errorCard.hidden = true;
}

function formatFileSize(bytes) {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}

function resetUpload() {
    selectedFile = null;
    fileInput.value = '';
    document.querySelector('.upload-content').hidden = false;
    filePreview.hidden = true;
    actions.hidden = true;
}

function resetAll() {
    resetUpload();
    processedBlob = null;
    processedFileName = null;
    resultsCard.hidden = true;
    errorCard.hidden = true;
}

async function processFile() {
    if (!selectedFile) return;

    // Show progress
    document.querySelector('.upload-content').hidden = true;
    filePreview.hidden = true;
    actions.hidden = true;
    uploadProgress.hidden = false;
    errorCard.hidden = true;

    try {
        const formData = new FormData();
        formData.append('file', selectedFile);

        const response = await fetch(`${API_URL}/process`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Error procesando el archivo');
        }

        // Get the blob and filename
        processedBlob = await response.blob();
        const contentDisposition = response.headers.get('Content-Disposition');
        processedFileName = contentDisposition
            ? contentDisposition.split('filename=')[1]?.replace(/"/g, '')
            : `${selectedFile.name.replace('.xlsx', '')}_INVERSION_CALCULADA.xlsx`;

        // Show results
        uploadProgress.hidden = true;
        resultsCard.hidden = false;

    } catch (error) {
        console.error('Error:', error);
        showError(error.message);
    }
}

function showError(message) {
    uploadProgress.hidden = true;
    document.querySelector('.upload-content').hidden = false;
    filePreview.hidden = true;
    actions.hidden = true;
    errorCard.hidden = false;
    errorMessage.textContent = message;
}

function downloadResult() {
    if (!processedBlob) return;

    const url = URL.createObjectURL(processedBlob);
    const a = document.createElement('a');
    a.href = url;
    a.download = processedFileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Check API health on load
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (response.ok) {
            console.log('✅ API connected');
        }
    } catch (error) {
        console.warn('⚠️ API not available. Make sure the backend is running.');
    }
}

// Rankings Modal
const viewRankingsBtn = document.getElementById('viewRankingsBtn');
const rankingsModal = document.getElementById('rankingsModal');
const closeModalBtn = document.getElementById('closeModalBtn');
const modalStats = document.getElementById('modalStats');
const rankingsContent = document.getElementById('rankingsContent');
const yearFilter = document.getElementById('yearFilter');
const monthFilter = document.getElementById('monthFilter');

let rankingsData = null;

viewRankingsBtn.addEventListener('click', openRankingsModal);
closeModalBtn.addEventListener('click', closeRankingsModal);
rankingsModal.addEventListener('click', (e) => {
    if (e.target === rankingsModal) closeRankingsModal();
});
yearFilter.addEventListener('change', renderRankings);
monthFilter.addEventListener('change', renderRankings);

async function openRankingsModal() {
    rankingsModal.hidden = false;
    document.body.style.overflow = 'hidden';

    if (!rankingsData) {
        await loadRankings();
    } else {
        renderRankings();
    }
}

function closeRankingsModal() {
    rankingsModal.hidden = true;
    document.body.style.overflow = '';
}

async function loadRankings() {
    try {
        const response = await fetch(`${API_URL}/rankings`);
        if (!response.ok) throw new Error('Error cargando rankings');

        rankingsData = await response.json();

        // Populate stats
        modalStats.innerHTML = `
            <div class="modal-stat">
                <span class="modal-stat-value">${rankingsData.stats.total_registros}</span>
                <span class="modal-stat-label">Registros</span>
            </div>
            <div class="modal-stat">
                <span class="modal-stat-value">${rankingsData.stats.emisoras_unicas}</span>
                <span class="modal-stat-label">Emisoras</span>
            </div>
            <div class="modal-stat">
                <span class="modal-stat-value">${rankingsData.stats.años.length}</span>
                <span class="modal-stat-label">Años</span>
            </div>
        `;

        // Populate year filter
        yearFilter.innerHTML = rankingsData.stats.años
            .sort((a, b) => b - a)
            .map((year, i) => `<option value="${year}" ${i === 0 ? 'selected' : ''}>${year}</option>`)
            .join('');

        updateMonthFilter();
        renderRankings();

    } catch (error) {
        console.error('Error loading rankings:', error);
        rankingsContent.innerHTML = `
            <div class="loading-rankings">
                <p>Error cargando rankings. Intenta de nuevo.</p>
            </div>
        `;
    }
}

function updateMonthFilter() {
    const selectedYear = yearFilter.value;
    const months = Object.keys(rankingsData.rankings[selectedYear] || {});

    const monthOrder = ['Marzo', 'Junio', 'Agosto', 'Septiembre', 'Noviembre'];
    months.sort((a, b) => monthOrder.indexOf(a) - monthOrder.indexOf(b));

    monthFilter.innerHTML = `
        <option value="">Todos los meses</option>
        ${months.map(month => `<option value="${month}">${month}</option>`).join('')}
    `;
}

function renderRankings() {
    const selectedYear = yearFilter.value;
    const selectedMonth = monthFilter.value;

    if (!rankingsData || !rankingsData.rankings[selectedYear]) {
        rankingsContent.innerHTML = '<p>No hay datos disponibles</p>';
        return;
    }

    updateMonthFilter();

    const yearData = rankingsData.rankings[selectedYear];
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

    rankingsContent.innerHTML = html;
}

// Keyboard support for modal
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !rankingsModal.hidden) {
        closeRankingsModal();
    }
});

// Initialize
checkAPIHealth();
