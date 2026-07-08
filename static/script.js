function togglePassword() {

    let password = document.getElementById("password");
    let eye = document.getElementById("eye");

    if (password.type === "password") {
        password.type = "text";
        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");
    } else {
        password.type = "password";
        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");
    }
}

function copyPassword() {

    let generated = document.getElementById("generated");

    generated.select();
    generated.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(generated.value);

    let button = document.querySelector(".generated button");

    button.innerHTML = "Copied!";

    button.style.background = "#16a34a";

    setTimeout(function () {

        button.innerHTML = "Copy";

        button.style.background = "";

    }, 2000);
}

window.onload = function () {

    let bar = document.querySelector(".progress-bar");

    if (bar) {

        let width = bar.style.width;

        bar.style.width = "0%";

        setTimeout(function () {

            bar.style.width = width;

        }, 300);

    }

}
