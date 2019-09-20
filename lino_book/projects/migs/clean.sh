#!/usr/bin/env bash
set -e
rm -rf migrations/*
rm -f settings/default.db
touch migrations/__init__.py
echo "Removed migrations and database."
