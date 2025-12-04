# PowerShell script to convert text to PDF using Word COM object
$inputFile = "c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\autonomous-it-troubleshooting-agent\datasets\IT_Support_QA.txt"
$outputFile = "c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\autonomous-it-troubleshooting-agent\datasets\IT_Support_QA.pdf"

try {
    # Create Word application object
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    
    # Open the text file
    $doc = $word.Documents.Open($inputFile)
    
    # Save as PDF (format 17 is PDF)
    $doc.SaveAs([ref]$outputFile, [ref]17)
    
    # Close document and quit Word
    $doc.Close()
    $word.Quit()
    
    # Release COM objects
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($doc) | Out-Null
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
    
    Write-Host "PDF created successfully: $outputFile" -ForegroundColor Green
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host "Microsoft Word may not be installed or accessible." -ForegroundColor Yellow
}
