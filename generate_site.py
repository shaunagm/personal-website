from mako.template import Template
from mako.lookup import TemplateLookup

# fullpath = "http://0.0.0.0:8000/site/"
fullpath = "http://www.shaunagm.net/"

# Specify template directory
lookup = TemplateLookup(["./templates"])

# Generate index page, talks, publications, project index page
for page in ["index.html", "talks.html", "publications.html", "projects.html", "cv.html", "about.html"]:
    template = lookup.get_template("/" + page)
    with open("./site/" + page, "w") as newFile:
        newFile.write(template.render(fullpath=fullpath))

# Generate individual project pages
for page in ["bongardcards.html", "eureka.html", "littler.html", "open-government-boston.html",
    "open-science-collaboration-blog.html", "open-source-recommendation-letter.html",
    "smalltalk.html", "welcomebot.html", "when-women-refuse.html", "interface.html", "kybern.html"]:
    template = lookup.get_template("/projects/" + page)
    with open("./site/projects/" + page, "w") as newFile:
        newFile.write(template.render(fullpath=fullpath))

# Generate misc pages
for page in ["cakes.html"]:
    template = lookup.get_template("/misc/" + page)
    with open("./site/misc/" + page, "w") as newFile:
        newFile.write(template.render(fullpath=fullpath))
