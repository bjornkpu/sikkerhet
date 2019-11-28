inotifywait -m -e modify main.tex |
  while read file; do
    echo $file
    pdflatex --shell-escape $file
    rm -rf _minted-main *.aux *.log
  done
