from StringIO import StringIO
import os, app, unittest, tempfile

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        print "done"

    def test_upload(self):
    	message = "test message"
    	stream = StringIO(message)
    	data = {'file':(stream, 'output.txt')}
    	r = self.app.post('/upload', data=data)
    	assert r.data == message

if __name__ == '__main__':
    unittest.main()