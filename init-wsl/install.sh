sudo apt-get update

# zsh
# ===
sudo apt-get install zsh -y
if test -d "$HOME/.oh-my-zsh"; then
  echo ".oh-my-zsh found in the system, update existing repository..."
  cd $HOME/.oh-my-zsh && git pull origin master && cd $HOME
else
  echo "Installing .oh-my-zsh..."
  sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
fi
if ! test -d "$HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting"; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting
fi
if ! test -d "$HOME/.oh-my-zsh/plugins/zsh-autosuggestions"; then
  git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/plugins/zsh-autosuggestions
fi
ln -sf $HOME/forge/init-wsl/zshrc $HOME/.zshrc

# tmux
# ====
ln -sf $HOME/forge/init-wsl/tmux.conf $HOME/.tmux.conf
if test -d "$HOME/.tmux/plugins/tpm"; then
	cd $HOME/.tmux/plugins/tpm && git pull origin master && cd $HOME
else
	git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm
fi

# gcc, g++
sudo apt-get install gcc -y
sudo apt-get install g++ -y

# cmake
sudo apt-get install cmake -y

# nvim + astronvim
if command -v nvim &> /dev/null
then
    echo "Neovim is installed"
else
    echo "Neovim is not installed"
    # sudo add-apt-repository --remove ppa:neovim-ppa/stable
    sudo add-apt-repository ppa:neovim-ppa/unstable # to install neovim >= 0.8
    sudo apt update
    sudo apt install neovim -y
    mv ~/.local/share/nvim ~/.local/share/nvim.bak
    mv ~/.local/state/nvim ~/.local/state/nvim.bak
    mv ~/.cache/nvim ~/.cache/nvim.bak
    git clone --depth 1 https://github.com/AstroNvim/template ~/.config/nvim
    rm -rf ~/.config/nvim/.git
fi

# lazygit
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin
rm -rf lazygit lazygit.tar.gz

