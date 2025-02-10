import pytz

#Наименование базы данных паролей и пользователей
AUTH_DATABASE_STR = "sqlite:///./data/auth.db"

# Часовой пояс
LOCAL_TIMEZONE = pytz.timezone("Etc/GMT-2")

# Секретный ключ для подписи JWT
SECRET_KEY = "my test key"
 