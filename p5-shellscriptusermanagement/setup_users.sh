#!/bin/bash

INPUT_FILE="users.txt"
USERS_CREATED="users-created.txt"
LOG_FILE="messages.log"

> "$USERS_CREATED"
> "$LOG_FILE"

if [ ! -d "/company" ]; then
    sudo mkdir /company
    echo "[INFO] Folder /company dibuat" | tee -a "$LOG_FILE"
fi

if [ ! -d "/company/shared" ]; then
    sudo mkdir /company/shared
    sudo chmod 755 /company/shared
    echo "[INFO] Folder shared dibuat dengan permission 755" | tee -a "$LOG_FILE"
fi

while IFS=":" read -r username group <&3; do
    [ -z "$username" ] && continue

    if ! getent group "$group" > /dev/null; then
        sudo groupadd "$group"
        sudo mkdir -p "/company/$group"
        sudo chown :$group "/company/$group"
        sudo chmod 770 "/company/$group"
        echo "[INFO] Group $group dan folder /company/$group dibuat dengan permission 770" | tee -a "$LOG_FILE"
    fi

    if id "$username" &>/dev/null; then
        echo "[WARNING] User $username sudah ada!" | tee -a "$LOG_FILE"
        read -p "Masukkan username baru untuk $username: " newusername
        username="$newusername"
    fi

    if sudo useradd -m -s /bin/bash -g "$group" "$username" 2>/dev/null; then
        echo "[INFO] User $username berhasil dibuat dan ditambahkan ke group $group" | tee -a "$LOG_FILE"
        echo "$username:$group" >> "$USERS_CREATED"
    else
        echo "[ERROR] Gagal membuat user $username:$group" | tee -a "$LOG_FILE"
    fi

done 3< "$INPUT_FILE"
