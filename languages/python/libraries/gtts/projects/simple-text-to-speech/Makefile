# Makefile for running python

## Ingredients/Variables
CC = python
CFLAGS = 
SRC_DIR = src/
SRC_FILE = main.py
SRC_ARGS = 

## System
### Environment Variables
export PYGAME_HIDE_SUPPORT_PROMPT = '1'

.PHONY := help run
.DEFAULT_RULES := help

## Targets/Rules/Recipes
help:
	## Display help menu
	@echo -e "help : Display help menu"
	@echo -e "run  : Run application"

run:
	## Run application
	@${CC} ${CFLAGS} ${SRC_DIR}/${SRC_FILE} ${SRC_ARGS}




