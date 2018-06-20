#!/bin/bash

echo "[INFO] --Descompactacao de arquivos"
echo "[INFO] Arquivo: "$1


arquivo=$1
origem="./"$1
destino="./"$1

echo "[INFO] Inicio da descompactacao do arquivo: "$1
echo "[INFO] cat ${origem}*gz | gzip -d > ${destino}"
cat ${origem}*gz | gzip -d -f > ${destino}
echo "[INFO] Fim da descompactacao do arquivo: "$1
