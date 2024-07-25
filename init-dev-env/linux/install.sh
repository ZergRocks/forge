sudo apt-get update -y

# git, curl, wget
# ===============
sudo apt-get install git curl wget -y
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin

# zsh
# ===
sudo apt install zsh -y
sudo chsh -s $(which zsh)
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/plugins/zsh-autosuggestions
ln -sf $HOME/forge/init-dev-env/linux/zshrc $HOME/.zshrc

# neovim
# ======
sudo apt-get install neovim -y
# git clone --depth 1 https://github.com/AstroNvim/template ~/.config/nvim
# rm -rf ~/.config/nvim/.git

# tmux
# ====
sudo apt-get install tmux -y
ln -sf $HOME/forge/init-dev-env/linux/tmux.conf $HOME/.tmux.conf

if test -d "$HOME/.tmux/plugins/tpm"; then
	cd $HOME/.tmux/plugins/tpm && git pull origin master && cd $HOME
else
	git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm
fi
