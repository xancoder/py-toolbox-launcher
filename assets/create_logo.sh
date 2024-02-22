#!/usr/bin/env bash

inkscape -w 256 -h 256 -o 256.png logo.svg

convert -background transparent "256.png" -define icon:auto-resize=128,96,72,64,48,32,24,16 "logo.ico"

identify logo.ico

rm ./*.png
