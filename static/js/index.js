
async function registerUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();
    const registerResult = document.getElementById("result");
    registerResult.textContent = response.ok ? result.message : result.detail;
}

async function loginUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();
    const loginResult = document.getElementById("result");
    loginResult.textContent = response.ok ? "Успешный вход! Получен токен:\n" + result.access_token : result.detail;
    if (response.ok) {
        localStorage.setItem("token", result.access_token);
    }
}

async function checkAccess() {
    const token = localStorage.getItem("token");

    const response = await fetch("/check_access", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const result = await response.json();
    const accessResult = document.getElementById("result");
    accessResult.textContent = response.ok ? "Доступ разрешён! Payload: \n" + JSON.stringify(result.payload) : "Доступ запрещён";
}

