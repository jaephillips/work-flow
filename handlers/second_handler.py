
import jinja_env
import logging
import webapp2

from models import form_model
from models import book

class SecondHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("SecondHandler")
    	books = book.Book.query().fetch()
    	# do stuff with books...
        html_params = {
            "title": "Second Title",
            "content": "Goodbye"
        }
        template = jinja_env.env.get_template('templates/input.html')
        self.response.out.write(template.render(html_params))



    def post(self):
        logging.info("USER SAID POST")
        r_name =self.request.get("form_name")
        r_task =self.request.get("form_task")
        r_level =self.request.get("form_level")
        r_date= self.request.get("form_date")
        r_instructions= self.request.get("form_instructions")



        new_form = form_model.FormModel(
                form_name= r_name,
                form_task= r_task,
                form_level= r_level,
                user_email="FIX ME LATER",

            )

        new_form.put()
        self.redirect("/formlist")

        