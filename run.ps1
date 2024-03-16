# Create logfile directory
New-Item -Type Directory -Force "logs"

# Iterate over all data files
$files = Get-ChildItem -Path ".\data\test_audio"
foreach ($f in $files){
    $filename = $f.FullName
    write-output $filename

    $shortname = $f.Name
    write-output $shortname

    $logfile = ".\logs\" + $shortname + ".log"

    python .\src\transcribe.py $filename 2>&1 `
        | ForEach-Object ToString | `
        Tee-Object $logfile
}