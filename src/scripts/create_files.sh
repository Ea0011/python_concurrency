# creates source files for mac

for i in {1..1000}
do
  mkfile -n 5m ~/Programming/HPC/python_concurency/source/file_$i.txt
done
