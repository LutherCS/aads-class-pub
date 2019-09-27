# sudo apt-get install texlive-xetex

INPUT_FILE=$1
FORMAT=$2

if [ $# == 0 ]; then
    echo Usage: ./convert.sh INPUT_FILE.md OUTPUT_FORMAT
    exit
fi

if [ $FORMAT == "html" ]; then
    pandoc $INPUT_FILE variables.yaml -o "${INPUT_FILE%.*}.$FORMAT" --mathjax -s -i --slide-level=3 -t revealjs 
elif [ $FORMAT == "pdf" ]; then
    # pandoc $INPUT_FILE variables.yaml -s --latex-engine=xelatex --variable mainfont="FreeSerif" --variable sansfont="FreeSans" --variable monofont="FreeMono" -o "${INPUT_FILE%.*}.$FORMAT"
    pandoc $INPUT_FILE variables.yaml -o "${INPUT_FILE%.*}.$FORMAT" -s --pdf-engine=xelatex 
elif [ $FORMAT == "tex" ]; then
    pandoc $INPUT_FILE variables.yaml -o "${INPUT_FILE%.*}.$FORMAT" -s --pdf-engine=xelatex
fi
