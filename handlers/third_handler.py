import jinja_env
import logging
import webapp2

from models import book
from models import form_model

class FormListHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("ThirdHandler")
        forms = form_model.FormModel.query().fetch()
        logging.info(forms)
        comment_str = ""
        for FormModel in forms:
            comment_str += "<div>"
            comment_str += "<h3>Author : " + FormModel.form_name + "</h3>"
            comment_str += "<p>" + FormModel.form_task + "</p>"
            comment_str += "</div>"



    	
        html_params = {
            "html_comments": comment_str,
            "content": "Goodbye",
        }
        template = jinja_env.env.get_template('templates/taskboard.html')
        self.response.out.write(template.render(html_params))