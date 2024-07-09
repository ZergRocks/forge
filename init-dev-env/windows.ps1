# 1. install powershell 7.4 as MSI package
# https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4#installing-the-msi-package

# 2. install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; `
  [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol `
  -bor 3072; `
  Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 3. install choco packages
# choco install microsoft-windows-terminal -y # no need to install
choco install ripgrep -y
choco install fd -y
choco install mingw -y
choco install lazygit -y
choco install make -y
choco install neovim -y
choco install nodejs-lts -y
choco install python -y


# 4. install lunarvim
pwsh -c "`$LV_BRANCH='release-1.3/neovim-0.9'; iwr https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.ps1 -UseBasicParsing | iex"

# 5. set git config
git config --global user.name "ZergeRocks Windows"
git config --global user.email forhelsinki21@gmail.com

<# 6. etc
- for windows set with KR language as main,
  => https://lazyren.github.io/devlog/keyboard-input-error-in-wt.html
#>
