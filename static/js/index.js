// URL-адрес API сервера
const API_BASE_URL = "http://127.0.0.1:8000";


// Функция для регистрации пользователя
async function register(username, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            console.log("Пользователь успешно зарегистрирован.");
        } else {
            const errorData = await response.json();
            console.error("Ошибка регистрации:", errorData.detail);
        }
    } catch (error) {
        console.error("Ошибка:", error);
    }
}

// Функция для получения токена
async function getToken(username, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Токен:", data.access_token);
            return data.access_token; // Возвращаем токен
        } else {
            const errorData = await response.json();
            console.error("Ошибка получения токена:", errorData.detail);
            return null;
        }
    } catch (error) {
        console.error("Ошибка:", error);
        return null;
    }
}

// Функция для доступа к защищенному ресурсу
async function accessProtectedResource(token) {
    try {
        const response = await fetch(`${API_BASE_URL}/check_access`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
            },
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Данные защищенного ресурса:", data);
        } else {
            const errorData = await response.json();
            console.error("Ошибка доступа:", errorData.detail);
        }
    } catch (error) {
        console.error("Ошибка:", error);
    }
}
