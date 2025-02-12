#Основные константы
import pytz

#Наименование базы данных паролей и пользователей
AUTH_DATABASE_LOC = "sqlite:///./auth.db"

# Часовой пояс
LOCAL_TIMEZONE = pytz.timezone("Etc/GMT-2")

# Секретный ключ для подписи JWT
SECRET_KEY = "my test key"

# Директория статичных файлов фронтенда
STATIC_DIR = "/static"
 
# Директория размещения templates (HTML-шаблонов и документов)
TEMPLATE_DIR = "templates"

# Разрешенные точки входа (запросы)
ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000"
]