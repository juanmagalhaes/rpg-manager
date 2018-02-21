#!/bin/bash
set -e

psql -h localhost -v ON_ERROR_STOP=1 -U postgres -c 'CREATE DATABASE rpg_manager;'
