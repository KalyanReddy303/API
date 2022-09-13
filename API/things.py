from wsgiref.simple_server import make_server

import falcon



class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_OK  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            '\n My name is kalyan '
            'iam 22 .\n'
            '\n'
            '    ~ Kalyann\n\n'
        )



app = falcon.App()


things = ThingsResource()


app.add_route('/things', things)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')


        httpd.serve_forever()