[app]
title = Tejas Browser
package.name = tejasbrowser
package.domain = org.tejas
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0
requirements = python3,kivy,flask,requests
orientation = portrait
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
