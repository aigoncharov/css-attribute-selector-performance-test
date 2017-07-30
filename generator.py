import argparse
import random

TEMPLATE = (
		'<!doctype html><html><head><title>CSS Tag Selctor Test</title></head><body>',
		'</body></html>',
	)
LINE_TEMPLATE = '{}\n'
TIMER_TEMPLATE = '<script type="text/javascript">var renderTime = Date.now();window.addEventListener("load", () => console.log(Date.now() - renderTime))</script>'
TEST_SELECTOR_TEMPLATE = (
		'test-selector-{}',
		'{} {{ background-color: {} }}',
	)
CSS_RULE_NAME_TEMPLATE = ('[{}]', '.{}')
DOM_ELEMENT_TEMPLATE = (
		'<div {}>{}</div>',
		'<div class="{}">{}</div>',
	)

def generate(is_tag: bool = True, block_num: int = 10, css_rule_num: int = 10, file_name: str = 'index.html'):
	with open(file_name, 'w') as f:
		f.write(LINE_TEMPLATE.format(TEMPLATE[0]))

		# generate CSS
		selector_name = CSS_RULE_NAME_TEMPLATE[0]
		if not is_tag:
			selector_name = CSS_RULE_NAME_TEMPLATE[1]
		selector_name = selector_name.format(TEST_SELECTOR_TEMPLATE[0])

		f.write(LINE_TEMPLATE.format('<style>'))
		for num in range(css_rule_num):
			selector_name_curr = selector_name.format(num)
			f.write(LINE_TEMPLATE.format(TEST_SELECTOR_TEMPLATE[1]).format(selector_name_curr, _get_rand_color()))
		f.write(LINE_TEMPLATE.format('</style>'))

		f.write(LINE_TEMPLATE.format(TIMER_TEMPLATE))

		# generate divs
		el = DOM_ELEMENT_TEMPLATE[0]
		if not is_tag:
			el = DOM_ELEMENT_TEMPLATE[1]
		
		css_rule_i = 0
		for num in range(block_num):
			selector_curr = TEST_SELECTOR_TEMPLATE[0].format(css_rule_i)
			css_rule_i += 1
			if css_rule_i >= css_rule_num:
				css_rule_i = 0

			f.write(LINE_TEMPLATE.format(el).format(selector_curr, num))

		f.write(LINE_TEMPLATE.format(TEMPLATE[1]))


def _get_rand_color():
	return 'rgb({}, {}, {})'.format(random.randrange(256), random.randrange(256), random.randrange(256))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--is_tag", action="store_true")
	parser.add_argument("--block_num", type=int, default=10)
	parser.add_argument("--css_rule_num", type=int, default=10)
	parser.add_argument("--file_name", type=str, default='index.html')
	args = parser.parse_args()
	generate(**vars(args))