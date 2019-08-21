#!/usr/bin/env bash
cd /django-redis-sentinel/tests/

# Django 220
echo "<<<< Testing Django220 >>>"
alias python=python
echo "Switched to PY3K"
pip install -U 'Django>=2.2,<2.3'
python runtests-sentinel.py

echo "End of testing PY3K, Django>=2.2"
