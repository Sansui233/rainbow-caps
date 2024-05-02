
$outputZipFile = "彩虹帽子v0.1.1.zip"
# 使用 7zip 压缩
& 7z a -tzip "$outputZipFile" "assets" "data" "pack.mcmeta" "pack.png"

Copy-Item -Force $outputZipFile "C:\Users\lingn\Documents\Minecraft\Default\.minecraft\versions\1.20.4\resourcepacks\"

Move-Item -Force $outputZipFile "C:\Users\lingn\Documents\Minecraft\Default\.minecraft\versions\1.20.4\saves\新的世界\datapacks\"