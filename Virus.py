#!/bin/bash

clear

figlet Virus
figlet Lengkap
echo "======================================"
echo "   Author :Muhammad Rizky "
echo "   YT     :PS        Rizky "
echo "======================================"
echo " macam-macam virus : "
echo " [1].Trojans"
echo " [2].malware"
echo " [3].sofware"
echo " [4].idiot"
echo "======================================"

read -p "pilih : " pilih
read -p "Masukan nomor Target :" pilih
read -p "Masukan Jumblah Virus maksimal 3 :" pilih

case $pilih in
*)
echo "Nomor Target Ditemukan"
sleep 3
echo "kirim virus akan di mulai 3 detik lagi..."
sleep 2
echo "[*]send Berhasil"
sleep 1
echo "[*]send berhasil"
sleep 1
echo "[*]send berhasil"
sleep 1
echo "Kirim Virus Berhasil"
;;
esac

