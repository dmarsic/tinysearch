fmt:
	pdm fmt

test: fmt
	pdm test

build: test
	pdm build
