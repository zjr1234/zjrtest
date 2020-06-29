#!/bin/bash
ARGS=`getopt -a -o A:LMSsth -l test: -- "$@"`
eval set -- "${ARGS}"
while true
do
      case "$1" in
      -t|--test)
              arg="$2"
              shift
              ;;
      --)
              shift
              break
              ;;
      esac
shift
done
if [ -z "${arg}" ]; then
  echo "Missing parameter:-t|--test"
  exit 2
fi
echo "$arg"