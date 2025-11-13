[app]
title = MyDela
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21

# Разрешаем автоматическую загрузку с принятием лицензий
android.accept_sdk_license = True

# Используем стабильные версии
android.build_tools = 33.0.0
android.ndk = 25.1.8937393

# Только одна архитектура
android.arch = armeabi-v7a

# Увеличиваем таймауты
android.sdk_manager_timeout = 120