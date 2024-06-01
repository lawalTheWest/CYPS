document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript file loaded");

    const cropSelect = document.getElementById('crop-select');
    if (cropSelect) {
        console.log("Dropdown element found");
        cropSelect.addEventListener('change', function() {
            console.log("Dropdown changed");
            if (this.value) {
                console.log("Selected value:", this.value);
                window.location.href = "/crops/" + this.value;
            }
        });
    } else {
        console.log("Dropdown element not found");
    }
});
