# 修复项目中的YAML文件格式
$yamls = Get-ChildItem .github/workflows/*.yml -Recurse
foreach ($file in $yamls) {
    $content = (Get-Content $file.FullName -Raw) -replace "(?m)^\s+$","`n"
    [IO.File]::WriteAllText($file.FullName, $content.Trim() + "`n", [Text.Encoding]::UTF8)
    Write-Host "已修复: $($file.FullName)"
}
