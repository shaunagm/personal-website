from mako.template import Template
from mako.lookup import TemplateLookup

# fullpath = "file:///home/shauna/Desktop/temp/shared/git/public-misc/shaunagm-newsite/site/"
fullpath = "http://0.0.0.0:8000/"

# Specify template directory

lookup = TemplateLookup(["./templates"])

# Generate index page, talks, publications, project index page
for page in ["index.html", "talks.html", "publications.html", "projects.html", "cv.html"]:
    template = lookup.get_template("/" + page)
    with open("./site/" + page, "wb") as newFile:
        newFile.write(template.render(fullpath=fullpath))

# Generate individual project pages
for page in ["bongardcards.html", "eureka.html", "littler.html", "open-government-boston.html",
    "open-science-collaboration-blog.html", "open-source-recommendation-letter.html",
    "smalltalk.html", "welcomebot.html", "when-women-refuse.html"]:
    template = lookup.get_template("/projects/" + page)
    with open("./site/projects/" + page, "wb") as newFile:
        newFile.write(template.render(fullpath=fullpath))

# Generate misc pages
for page in ["cakes.html"]:
    template = lookup.get_template("/misc/" + page)
    with open("./site/misc/" + page, "wb") as newFile:
        newFile.write(template.render(fullpath=fullpath))
