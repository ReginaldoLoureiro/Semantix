#!/bin/bash

sh descompactar.sh $1
python semantix_nasa.py $1
rm ./NASA*
