postpip.playwright:
	python -m playwright install

docs:
	pdoc tolha

publish:
	poetry publish --build