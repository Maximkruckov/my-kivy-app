[app]
title = My App
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
android.accept_sdk_license = True
android.arch = armeabi-v7a

# ДОБАВЬ ЭТИ СТРОКИ:
android.build_tools = 33.0.0
android.sdk_version = 33
android.ndk_version = 25b
