# PowerShell Script to Convert Markdown to PDF using Pandoc
# Prerequisites: Install Pandoc from https://pandoc.org/installing.html

param(
    [string]$SourceFolder = ".",
    [string]$OutputFolder = ".",
    [switch]$InstallPandoc
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  IT Support KB Markdown to PDF Converter" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Pandoc is installed
function Test-PandocInstalled {
    try {
        $version = pandoc --version 2>$null
        if ($version) {
            Write-Host "✓ Pandoc is installed" -ForegroundColor Green
            Write-Host "  Version: $($version[0])" -ForegroundColor Gray
            return $true
        }
    }
    catch {
        return $false
    }
    return $false
}

# Install Pandoc using Chocolatey
function Install-PandocWithChoco {
    Write-Host "Attempting to install Pandoc using Chocolatey..." -ForegroundColor Yellow
    
    # Check if Chocolatey is installed
    try {
        choco --version | Out-Null
        Write-Host "✓ Chocolatey is installed" -ForegroundColor Green
        
        Write-Host "Installing Pandoc..." -ForegroundColor Yellow
        choco install pandoc -y
        
        Write-Host "✓ Pandoc installed successfully" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "✗ Chocolatey is not installed" -ForegroundColor Red
        Write-Host "  Please install Pandoc manually from: https://pandoc.org/installing.html" -ForegroundColor Yellow
        return $false
    }
}

# Main conversion function
function Convert-MarkdownToPDF {
    param(
        [string]$InputFile,
        [string]$OutputFile
    )
    
    Write-Host "Converting: $InputFile" -ForegroundColor Cyan
    
    try {
        # Run Pandoc conversion
        $result = pandoc $InputFile -o $OutputFile --pdf-engine=wkhtmltopdf 2>&1
        
        if (Test-Path $OutputFile) {
            $fileSize = (Get-Item $OutputFile).Length / 1MB
            Write-Host "  ✓ Success: $OutputFile ($([math]::Round($fileSize, 2)) MB)" -ForegroundColor Green
            return $true
        }
        else {
            Write-Host "  ✗ Failed to create PDF" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "  ✗ Error: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Check Pandoc installation
if (-not (Test-PandocInstalled)) {
    Write-Host "✗ Pandoc is not installed" -ForegroundColor Red
    Write-Host ""
    
    if ($InstallPandoc) {
        if (Install-PandocWithChoco) {
            Write-Host ""
        }
        else {
            Write-Host "Please install Pandoc manually and run this script again." -ForegroundColor Yellow
            Write-Host "Download from: https://pandoc.org/installing.html" -ForegroundColor Yellow
            exit 1
        }
    }
    else {
        Write-Host "Run this script with -InstallPandoc to attempt automatic installation" -ForegroundColor Yellow
        Write-Host "Or install manually from: https://pandoc.org/installing.html" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host ""
Write-Host "Starting conversion process..." -ForegroundColor Cyan
Write-Host ""

# Define files to convert
$filesToConvert = @(
    "IT_Support_FAQ_Password_Reset.md",
    "IT_Support_SOP_VPN_Issues.md",
    "IT_Support_SOP_Slow_Laptop.md",
    "IT_Support_SOP_Printer_Issues.md"
)

$successCount = 0
$failCount = 0

foreach ($file in $filesToConvert) {
    $inputPath = Join-Path $SourceFolder $file
    $outputPath = Join-Path $OutputFolder ($file -replace '\.md$', '.pdf')
    
    if (Test-Path $inputPath) {
        if (Convert-MarkdownToPDF -InputFile $inputPath -OutputFile $outputPath) {
            $successCount++
        }
        else {
            $failCount++
        }
    }
    else {
        Write-Host "✗ File not found: $inputPath" -ForegroundColor Red
        $failCount++
    }
    
    Write-Host ""
}

# Summary
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Conversion Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total files: $($filesToConvert.Count)" -ForegroundColor White
Write-Host "Successful: $successCount" -ForegroundColor Green
Write-Host "Failed: $failCount" -ForegroundColor $(if ($failCount -gt 0) { "Red" } else { "Green" })
Write-Host ""

if ($successCount -gt 0) {
    Write-Host "✓ PDF files are ready to upload to Copilot Studio!" -ForegroundColor Green
    Write-Host "  Location: $OutputFolder" -ForegroundColor Gray
}

# List created PDFs
if ($successCount -gt 0) {
    Write-Host ""
    Write-Host "Created PDF files:" -ForegroundColor Cyan
    Get-ChildItem -Path $OutputFolder -Filter "*.pdf" | ForEach-Object {
        $size = [math]::Round($_.Length / 1MB, 2)
        Write-Host "  - $($_.Name) ($size MB)" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Open Microsoft Copilot Studio (https://copilotstudio.microsoft.com)" -ForegroundColor White
Write-Host "2. Navigate to Knowledge → Add knowledge → Files" -ForegroundColor White
Write-Host "3. Upload all 4 PDF files" -ForegroundColor White
Write-Host "4. Wait for indexing to complete" -ForegroundColor White
Write-Host "5. Enable Generative AI in Settings" -ForegroundColor White
Write-Host ""

# Alternative method suggestion
if ($failCount -gt 0) {
    Write-Host "Alternative conversion methods:" -ForegroundColor Yellow
    Write-Host "1. Use VS Code with 'Markdown PDF' extension" -ForegroundColor White
    Write-Host "2. Use online converter: https://www.markdowntopdf.com/" -ForegroundColor White
    Write-Host "3. Copy content to Microsoft Word and save as PDF" -ForegroundColor White
    Write-Host ""
}
