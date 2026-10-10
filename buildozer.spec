[app]
title = Tejas Browser
package.name = tejasbrowser
package.domain = org.tejas
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
