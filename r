#!/bin/bash

if g++ main.cpp -o main; then
	./main < $1
fi
