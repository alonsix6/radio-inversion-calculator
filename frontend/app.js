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

// Initialize
checkAPIHealth();
