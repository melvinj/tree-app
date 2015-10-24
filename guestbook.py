import cgi
from google.appengine.api import users
import webapp2
import process
import os


# function to create select button with all the names in the tree
def makeSelect(name, values):
    SEL = '<select name="{0}">\n{1}</select>\n'
    OPT = '<option value="{0}">{0}</option>\n'
    return SEL.format(name, ''.join(OPT.format(v) for v in values))

# call getList to get all the names
people = process.getList("family.json")

# create select button
select = makeSelect("person_name", people)

# form sytax
# TODO(melvin): Consider replacing this with jinja templates
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
