
$outputZipFile = "彩虹帽子v0.1.zip"
# 使用 7zip 压缩
& 7z a -tzip "$outputZipFile" "assets" "data" "pack.mcmeta" "pack.png"