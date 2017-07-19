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
            comment_str += '<div class = "comm">'
            comment_str += "<h2>Worker : " + str(FormModel.name) + "</h2>"
            comment_str += "<h3>Assigned By: </h4>" 
            comment_str += "<h4> " + str(FormModel.assignBy) + "</h5>"
            comment_str += "<h3>Task: </h4>"
            comment_str += "<h4> " + str(FormModel.task) + "</h5>"
            comment_str += "<h3>Difficulty level: </h4>"
            comment_str += "<h4> " + str(FormModel.level) + "</h5>"
            comment_str += "<h3>Due Date: </h4>"
            comment_str += "<h4> " + str(FormModel.date) + "</h5>"
            comment_str += "<h3>Instructions: </h4>" 
            comment_str += "<h4> " + str(FormModel.instructions) + "</h5>"
            comment_str += "<h3>Assigned By: </h4>" 
            comment_str += "<h4> " + str(FormModel.assignBy) + "</h5>"
            comment_str += "<h3>Contact them here: </h4>" 
            comment_str += "<h4> " + str(FormModel.email) + "</h5>"
            comment_str += "</div>"
            comment_str += "<br>"
           


    	
        html_params = {
            "html_comments": comment_str,
            "content": "Goodbye",
        }
        template = jinja_env.env.get_template('templates/taskboard.html')
        self.response.out.write(template.render(html_params))