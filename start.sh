echo installing packages..
pip -q install -r requirements.txt;
echo running tests..
python tester.py &>unittest.txt;
if grep -q "FAIL" unittest.txt ; then
  echo TESTS FAILED!;
  echo exit;
  exit;
else
  echo tests succeeded
  echo ChatApp has been started!;
fi;
python -m ChatApp