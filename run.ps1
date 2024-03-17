if ($args.Count -ne 1) {
    write-output "Error: Script takes exactly 1 argument!"
    exit
}

$data_directory=$args[0]
write-output "Parsing files in directory '$data_directory' ..."

# Create logfile directory
$null = New-Item -Type Directory -Force "logs"

# Iterate over all data files
$files = Get-ChildItem -Path $data_directory
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