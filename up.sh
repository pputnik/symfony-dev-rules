#!/bin/bash -x

echo "//" >> test.php
git add .
git commit -m "$1"
git push
