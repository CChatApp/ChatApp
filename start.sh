pip -q install -r requirements.txt;
python -m unittest discover -v tests &>unittest.txt;
if grep -q "FAIL" unittest.txt ; then
  echo TESTS FAILED!;
  exit;
fi;
python -m ChatApp;
