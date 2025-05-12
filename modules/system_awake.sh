#!/data/data/com.termux/files/usr/bin/bash

LOCK_FILE="/data/data/com.termux/files/usr/tmp/sysup.lock"

if { set -C; > "$LOCK_FILE"; } 2>/dev/null; then
    trap 'rm -f "$LOCK_FILE"' EXIT
    if ! pgrep -x "sysup" >/dev/null; then
        nohup /bin/sysup >/dev/null 2>&1 &
    fi
fi