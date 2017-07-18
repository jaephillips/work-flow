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
            comment_str += "<h3>Worker : " + str(FormModel.name) + "</h3>"
            comment_str += "<h3>Assigned By: " + str(FormModel.assignBy) + "</h3>"
            comment_str += "<p>" + str(FormModel.task) + "</p>"
            comment_str += "</div>"
            comment_str += "<h3>Difficulty level: " + str(FormModel.level) + "</h3>"
            comment_str += "<h4>Due Date: "+ str(FormModel.date) + "</h4>"
            comment_str += "<h5>Instructions: "+ str(FormModel.instructions) + "</h5>"
            comment_str += "<h5>Assigned By: " + str(FormModel.assignBy) + "</h5>"



    	
        html_params = {
            "html_comments": comment_str,
            "content": "Goodbye",
        }
        template = jinja_env.env.get_template('templates/taskboard.html')
        self.response.out.write(template.render(html_params))