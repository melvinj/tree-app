import cgi
from google.appengine.api import users
import webapp2
import process
import os


def makeSelect(name, values):
    SEL = '<select name="{0}">\n{1}</select>\n'
    OPT = '<option value="{0}">{0}</option>\n'
    return SEL.format(name, ''.join(OPT.format(v) for v in values))

people = process.getList("family.json")


select = makeSelect("person_name", people)

MAIN_PAGE_HTML = """\
<html>
<body>
<form action="/sign" method="post">
<div>""" + select + """</div>
<div>
<select name="action">
<option value="edit">Edit Name</option>
<option value="add_children">Add children</option>
<option value="add_spouse">Add Spouse</option>
</select>
</div>
<div><input type="submit" value="Choose person"></div>
</form>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>You chose:<pre>')
        self.response.write(cgi.escape(self.request.get('person_name')))
        self.response.write('</pre><br>Action:<pre>')
        self.response.write(cgi.escape(self.request.get('action')))
        self.response.write('</pre></body></html>')

            
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
