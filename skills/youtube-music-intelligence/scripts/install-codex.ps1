param(
    [string]$Destination = (Join-Path $env:USERPROFILE ".codex\skills\youtube-music-intelligence"),
    [string]$Repository = "https://github.com/uwavecom/agent-skills.git"
)

$ErrorActionPreference = "Stop"
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw "Git is required." }
if (Test-Path -LiteralPath $Destination) { throw "Destination exists: $Destination. Review it manually; nothing was overwritten." }
$temporary = Join-Path ([System.IO.Path]::GetTempPath()) ("agent-skills-" + [guid]::NewGuid().ToString("N"))
try {
    git clone --quiet --depth 1 --filter=blob:none --sparse $Repository $temporary
    if ($LASTEXITCODE -ne 0) { throw "Clone failed" }
    git -C $temporary sparse-checkout set skills/youtube-music-intelligence
    if ($LASTEXITCODE -ne 0) { throw "Sparse checkout failed" }
    $source = Join-Path $temporary "skills\youtube-music-intelligence"
    if (-not (Test-Path (Join-Path $source "SKILL.md"))) { throw "SKILL.md not found" }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Destination) | Out-Null
    Copy-Item -LiteralPath $source -Destination $Destination -Recurse
    Write-Host "Installed skill to: $Destination"
    Write-Host 'Restart Codex and invoke: Use $youtube-music-intelligence to analyze a music channel.'
} finally {
    if (Test-Path -LiteralPath $temporary) { Remove-Item -LiteralPath $temporary -Recurse -Force }
}
