build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf build
	rm -rf data_parse.egg-info
	rm -rf dist

install:
	cd dist
	pip3 install data_parse-*.whl
