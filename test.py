

import os.path
import astor
import pprint

import WebRequest

import ChromeController.manager as mgr
import ChromeController





def test_func(self, expression, **kwargs):
	"""
	Python Function: Runtime_evaluate
		Domain: Runtime
		Method name: evaluate

		Parameters:
			'expression' (type: string) -> Expression to evaluate.
			'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
			'includeCommandLineAPI' (type: boolean) -> Determines whether Command Line API should be available during the evaluation.
			'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
			'contextId' (type: ExecutionContextId) -> Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
			'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
			'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
			'userGesture' (type: boolean) -> Whether execution should be treated as initiated by user in the UI.
			'awaitPromise' (type: boolean) -> Whether execution should wait for promise to be resolved. If the result of evaluation is not a Promise, it's considered to be an error.
		Returns:
			'result' (type: RemoteObject) -> Evaluation result.
			'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		Description: Evaluates expression on global object.
	"""
	assert isinstance(expression, (str,)
		), 'Argument expression must be of type (str, ). Received type: %s' % type(
		expression)

	expected = [
		'objectGroup',
		'includeCommandLineAPI',
		'silent',
		'contextId',
		'returnByValue',
		'generatePreview',
		'userGesture',
		'awaitPromise',
	]



	if 'objectGroup' in kwargs:
		assert isinstance(kwargs['objectGroup'], (str,)
			), 'Argument objectGroup must be of type (str, ). Received type: %s' % type(
			kwargs['objectGroup'])
	if 'includeCommandLineAPI' in kwargs:
		assert isinstance(kwargs['includeCommandLineAPI'], (bool,)
			), 'Argument includeCommandLineAPI must be of type (bool, ). Received type: %s' % type(
			kwargs['includeCommandLineAPI'])
	if 'silent' in kwargs:
		assert isinstance(kwargs['silent'], (bool,)
			), 'Argument silent must be of type (bool, ). Received type: %s' % type(
			kwargs['silent'])
	if 'returnByValue' in kwargs:
		assert isinstance(kwargs['returnByValue'], (bool,)
			), 'Argument returnByValue must be of type (bool, ). Received type: %s' % type(
			kwargs['returnByValue'])
	if 'generatePreview' in kwargs:
		assert isinstance(kwargs['generatePreview'], (bool,)
			), 'Argument generatePreview must be of type (bool, ). Received type: %s' % type(
			kwargs['generatePreview'])
	if 'userGesture' in kwargs:
		assert isinstance(kwargs['userGesture'], (bool,)
			), 'Argument userGesture must be of type (bool, ). Received type: %s' % type(
			kwargs['userGesture'])
	if 'awaitPromise' in kwargs:
		assert isinstance(kwargs['awaitPromise'], (bool,)
			), 'Argument awaitPromise must be of type (bool, ). Received type: %s' % type(
			kwargs['awaitPromise'])

	passed_keys = list(kwargs.keys())
	assert all([key in expected for key in kwargs.keys()]), "Passed: %s" % passed_keys


	subdom_funcs = self.synchronous_command('Runtime.evaluate', expression=expression, **kwargs)
	return subdom_funcs




def docstring_dbg():
	print(astor.dump_tree(astor.code_to_ast(test_func)))


def test():

	ua = dict(WebRequest.getUserAgent())
	# print(ua)

	crbin = os.path.abspath("../AutoTriever/Headless/headless_shell")
	cr = ChromeController.CromeRemoteDebugInterface(binary=crbin)

	# print(cr)
	resp = cr.set_viewport_size(1500, 1000)
	# print("Viewport size", resp)

	resp = cr.set_user_agent_string(ua.pop('User-Agent'))
	# print("Set user agent: ", resp)
	ua['X-Devtools-Emulate-Network-Conditions-Client-Id'] = None
	resp = cr.set_headers(ua)
	# print("Set extra headers: ", resp)

	# resp = cr.blocking_navigate("http://www.google.com")
	resp = cr.blocking_navigate_and_get_source("http://10.1.1.8:33507/index")
	resp = cr.blocking_navigate_and_get_source("http://10.1.1.8:33507/index")

	cr.click_link_containing_url("/test")
	print("Page.navigate", resp['content'])
	img = cr.take_screeshot()
	with open("screenshot.png", "wb") as fp:
		fp.write(img)
	# resp = cr.synchronous_command("Page.captureScreenshot", {})
	# print("Page.captureScreenshot", resp)


	ctnt = cr.get_rendered_page_source()
	# print("Source:")
	# print(ctnt)

	wait_time = 5
	for x in range(wait_time):
		data = cr.drain_transport()
		# pprint.pprint(data)
		print("Sleeping: ", wait_time-x)

	# print("Draining!")
	# pprint.pprint(cr.drain_transport())

def gen():
	# print("Manager: ", mgr)
	cls_def = mgr.gen.get_source()
	with open("class.py", "w") as fp:
		fp.write(cls_def)
	# print(cls_def)
	# pass
	# ChromeController.test()


if __name__ == '__main__':
	test()
	# gen()
	# docstring_dbg()
