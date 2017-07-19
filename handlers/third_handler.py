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
            comment_str += "<h2>Worker : " + str(FormModel.name) + "</h2>"
            comment_str += "<h3>Assigned By: </h3>" 
            comment_str += "<h5> " + str(FormModel.assignBy) + "</h5>"
            comment_str += "<h2>Task:" + str(FormModel.task) + "</h2>"
            comment_str += "</div>"
            comment_str += "<h2>Difficulty level: " + str(FormModel.level) + "</h2>"
            comment_str += "<h2>Due Date: "+ str(FormModel.date) + "</h2>"
            comment_str += "<h2>Instructions: </h2>" 
            comment_str += "<h3> " + str(FormModel.instructions) + "</h3>"
            comment_str += "<h2>Assigned By: " + str(FormModel.assignBy) + "</h2>"
            comment_str += "<h2>Contact them here: " + str(FormModel.email) + "</h2>"


    	
        html_params = {
            "html_comments": comment_str,
            "content": "Goodbye",
        }
        template = jinja_env.env.get_template('templates/taskboard.html')
        self.response.out.write(template.render(html_params))