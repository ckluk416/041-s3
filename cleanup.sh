#!/bin/bash

USERS_CREATED="users-created.txt"
LOG_FILE="messages.log"

echo "[INFO] Mulai proses cleanup..." | tee -a "$LOG_FILE"

# Hapus user-user yang tercatat
if [ -f "$USERS_CREATED" ]; then
    cut -d: -f1 "$USERS_CREATED" | while read -r user; do
        if id "$user" &>/dev/null; then
            userdel -r "$user" 2>/dev/null
            echo "[INFO] User $user dihapus" | tee -a "$LOG_FILE"
        else
            echo "[WARNING] User $user tidak ditemukan" | tee -a "$LOG_FILE"
        fi
    done
else
    echo "[WARNING] File $USERS_CREATED tidak ditemukan, lewati penghapusan user" | tee -a "$LOG_FILE"
fi

# Hapus grup unik
if [ -f "$USERS_CREATED" ]; then
    cut -d: -f2 "$USERS_CREATED" | sort -u | while read -r group; do
        if getent group "$group" >/dev/null; then
            groupdel "$group" 2>/dev/null
            echo "[INFO] Group $group dihapus" | tee -a "$LOG_FILE"
        else
            echo "[WARNING] Group $group tidak ditemukan" | tee -a "$LOG_FILE"
        fi
    done
else
    echo "[WARNING] File $USERS_CREATED tidak ditemukan, lewati penghapusan grup" | tee -a "$LOG_FILE"
fi

# Hapus folder /company
if [ -d "/company" ]; then
    rm -rf /company
    echo "[INFO] Folder /company dihapus" | tee -a "$LOG_FILE"
else
    echo "[WARNING] Folder /company tidak ditemukan" | tee -a "$LOG_FILE"
fi

echo "[INFO] Cleanup selesai." | tee -a "$LOG_FILE"

# Reset file users-created
> "$USERS_CREATED"
