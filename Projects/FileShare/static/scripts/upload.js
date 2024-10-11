"use strict";

function uploadFiles() {
    const closeButton = document.getElementById('closeButton');
    const fileInput = document.getElementById('customFile');
    const progressBar = document.getElementById('progressBar');
    const filesUploadedSpan = document.getElementById('filesUploaded');
    const totalFilesSpan = document.getElementById('totalFiles');

    const Modal = new bootstrap.Modal(document.getElementById('overlayModal'));
    Modal.show();

    document.getElementById("status").innerHTML = "";
    closeButton.style.display = 'none';

    const files = fileInput.files;
    const length = files.length;

    if (length === 0) {
        alert('Please select at least one file.');
        return;
    }

    let currentFileIndex = 0;

    function uploadNextFile() {
        if (currentFileIndex < length) {
            const formData = new FormData();
            formData.append('files', files[currentFileIndex]);

            const xhr = new XMLHttpRequest();

            xhr.upload.addEventListener('progress', (event) => {
                if (event.lengthComputable) {
                    const percent = (event.loaded / event.total) * 100;

                    progressBar.style.width = percent + '%';
                    progressBar.setAttribute('aria-valuenow', percent);
                    progressBar.innerHTML = percent.toFixed(2) + '%';

                    filesUploadedSpan.textContent = currentFileIndex + 1;
                    totalFilesSpan.textContent = length;
                }
            });

            xhr.onreadystatechange = () => {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        progressBar.style.width = 0 + '%';
                        progressBar.setAttribute('aria-valuenow', '0%');

                        currentFileIndex++;
                        uploadNextFile();

                    } else {
                        filesUploadedSpan.textContent = `Error: ${xhr.status}`;
                        progressBar.style.display = 'none';
                        closeButton.disabled = false;
                    }
                }
            };

            xhr.open('POST', '/uploadfile');
            xhr.send(formData);
        } else {
            document.getElementById("status").innerHTML = "Upload Complete. Thank you for using our service.";
            closeButton.style.display = 'block';
        }
    }
    uploadNextFile();
}


function changeButton() {
    const uploadButton = document.getElementById("uploadButton");
    const fileInput = document.getElementById('customFile');

    if (fileInput.files.length > 0) {
        uploadButton.disabled = false;
    } else {
        uploadButton.disabled = true;
    }
}