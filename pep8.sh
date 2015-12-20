#!/bin/bash

XARGS="xargs -0 -J % pep8 %"

find ./pyomni -name '*.py' -print0 | ${XARGS} --ignore=E501
