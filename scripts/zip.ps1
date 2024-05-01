
$outputZipFile = "帽子戏法1.0.zip"
# 使用 7zip 压缩
& 7z a -tzip "$outputZipFile" "assets" "data" "pack.mcmeta" "pack.png"