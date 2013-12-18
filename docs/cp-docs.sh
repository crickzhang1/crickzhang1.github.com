#!/usr/bin/env bash

DOCS="zyh-cv-zh.pdf zyh-cv-en.pdf zyh-cv-zh.txt zyh-cv-en.txt zyh-qrcode-en-embedded.png zyh-qrcode-zh-embedded.png"
TARGET="."

for doc in $DOCS;
do
    cp -fp ../../jobhunting/resume/2013-find-a-new-job/general/$doc $TARGET
#    ls ../../jobhunting/resume/2013-find-a-new-job/general/$doc
done
