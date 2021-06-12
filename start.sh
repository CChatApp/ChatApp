if [[ $1 == "-Q" ]]; then
  quiet=true;
else
  quiet=false;
fi
function echo(){
  # shellcheck disable=SC2154
  if ! $quiet; then
    command echo "$@";
  fi
}
echo installing packages..
pip -q install -r requirements.txt;
echo running tests..
python tester.py &>unittest.txt;
if grep -q "FAIL" unittest.txt ; then
  echo TESTS FAILED! check file unittest.txt;
  echo exit;
  exit;
else
  echo tests succeeded
  echo ChatApp has been started!;
fi;
python -m ChatApp