document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('buylinkButton').addEventListener('click', function() {
        window.location.href = "/buy";
    });

    document.getElementById('stamplinkButton').addEventListener('click', function() {
        window.location.href = "/stampcard";
    });
});
