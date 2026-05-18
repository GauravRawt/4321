import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 11):
            self.response.write("10 x {} = {}<br>".format(i, 10 * i))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)