
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
        r_name =self.request.get("name")
        r_task =self.request.get("task")
        r_level =self.request.get("level")
        r_date= self.request.get("date")
        r_instructions= self.request.get("instructions")
        r_assign= self.request.get("assignBy")
        r_email = self.request.get("email")



        new_form = form_model.FormModel(
                name= r_name,
                task= r_task,
                level= r_level,
                date= r_date,
                instructions=r_instructions,
                assignBy= r_assign,
                email=r_email,

            )

        new_form.put()
        self.redirect("/second")