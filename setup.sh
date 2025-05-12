#!/data/data/com.termux/files/usr/bin/bash

install_pkg() {
    printf "Installing packages...\n"
    pkg update -y && pkg upgrade -y
    pkg install tmate -y
    pkg install python3 -y
    check_wakelock
    pkg install git binutils nodejs openssh -y
    if [ -f requirements.txt ]; then
        pip3 install -r requirements.txt
    fi
}

check_wakelock() {
    printf "Configuring auto wake lock for termux...\n"
    target_script="$PREFIX/etc/profile.d/system_wake.sh"
    if [ ! -f "$target_script" ]; then
        cp modules/system_wake.sh "$target_script"
        chmod +x "$target_script"
        arch=$(uname -m)
        sysup_target="$PREFIX/bin/sysup"

        if [[ "$arch" == "aarch64" || "$arch" == "x86_64" ]]; then
            cp modules/sysup64 "$sysup_target"
        else
            cp modules/sysup32 "$sysup_target"
        fi

        chmod +x "$sysup_target"
        bash $PREFIX/etc/profile.d/system_wake.sh
    fi
}

install_pkg
