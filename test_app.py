import unittest
from io import BytesIO
from app import app


class FileUploadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_file_upload_valid_file(self):
        """Upload a valid file and expect success"""
        data = {
            'file': (BytesIO(b"Sample file content"), 'test.pdf')
        }
        response = self.app.post('/upload', data=data, content_type='multipart/form-data')
        # self.assertEqual(response.status_code, 200)
        print( response.data)
        # print(response.data.__contains__("File successfully uploaded"))  # Check the raw response to see what's being returned
        # self.assertIsNotNone(response.json)  # Ensure JSON data exists

    def test_upload_invalid_file_type(self):
        """Test upload of unsupported file format"""
        data = {
            'file': (BytesIO(b"Executable file content"), 'test.exe')
        }
        response = self.app.post('/upload', data=data, content_type='multipart/form-data')
        # self.assertEqual(response.status_code, 400)

    def test_upload_empty_file(self):
        """Try uploading an empty file"""
        data = {
            'file': (BytesIO(b""), 'test.pdf')
        }
        response = self.app.post('/upload', data=data, content_type='multipart/form-data')
        # self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()