"use strict";

document.addEventListener('DOMContentLoaded', function () {
    const fileLabels = document.querySelectorAll('.file-label');
    
    fileLabels.forEach(function (fileLabel) {
        fileLabel.addEventListener('click', function () {
            fileLabel.classList.toggle('selected-file');
            const selectedFiles = document.querySelectorAll('.file-label.selected-file');
            updateButton(selectedFiles.length);
        });
    });
});

function downloadFiles() {
    const selectedFiles = document.querySelectorAll('.file-label.selected-file');

    if (selectedFiles.length > 0) {
        selectedFiles.forEach(
            function (filename) {
                filename = encodeURIComponent(filename.dataset.file)
                var downloadLink = '/downloadfile=' + filename;

                var link = document.createElement('a');
                link.href = downloadLink;

                link.download = filename;

                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            });
    } else {
        alert('Please select at least one file.');
    }
}

function updateButton(length) {
    const downloadButton = document.getElementById("downloadButton");
    if (length == 0) {
        downloadButton.disabled = true;
    } else {
        downloadButton.disabled = false;
    }
}