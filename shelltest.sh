#!/bin/bash
ARGS=$(getopt -a -o T:O:LMSsth -l test:,output: -- "$@")
eval set -- "${ARGS}"
while true; do
  case "$1" in
  -T | --test)
    test="$2"
    shift
    ;;
  -O | --output)
    output="$2"
    shift
    ;;
  --)
    shift
    break
    ;;
  esac
  shift
done
if [ -z "${test}" ]; then
  echo "Missing parameter:-I|--input"
  exit 2
fi
if [ -z "${output}" ]; then
  echo "Missing parameter:-O|--output"
  exit 2
fi
if [ -f ${output} ];then
        echo ""
else
        path=`echo ${output%/*}`
        echo $path
        mkdir -p $path
        touch -f $output
fi
echo ${test} >${output}
