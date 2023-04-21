fmt:
	pdm fmt

test: fmt
	pdm test

tag: test
	git pull
	pdm build
	git tag $(shell svu next)
