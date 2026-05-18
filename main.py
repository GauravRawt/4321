import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1,11):
            a = 10*i
            self.response.write('10 * {i} = {a} <br>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
