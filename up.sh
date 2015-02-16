#!/bin/bash -x

echo `date +%F-%H%M`  "<br>" >> test.php
git add .
git commit -m "$1"
git push
