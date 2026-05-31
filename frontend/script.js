document.getElementById("imageInput")
.addEventListener("change", function() {

    const file = this.files[0];

    if(file){
        document.getElementById("preview").src =
            URL.createObjectURL(file);
    }

});

async function uploadImage() {

    const fileInput = document.getElementById("imageInput");

    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    document.getElementById("result").innerHTML =
        "<h3>Analyzing...</h3>";

    const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();
    document.getElementById("result").innerHTML = `
        <div class="result-card">
            <h2>${data.prediction}</h2>
            <p>Confidence: ${data.confidence}</p>
            <p>File: ${data.filename}</p>
        </div>
    `;
}