#! /usr/bin/bash
HOST="10.0.107.22"
MSG="support-contact testagain \r\n"

telnet $HOST
echo send {$MSG}



