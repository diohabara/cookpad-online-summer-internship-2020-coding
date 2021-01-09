SRCS := $(wildcard *.py)

all: ${SRCS}
	make test1; make test2; make test3

test1:
	python3 q1.py

test2:
	python3 q2.py

test3:
	python3 q3.py

