#top = open('./templates/top.html').read()
#bottom = open('./templates/bottom.html').read()
#index = open('./content/index.html').read()
#blog=open('./content/blog.html').read()
#contact=open('./content/contact.html').read()
#project=open('./content/projects.html').read()

#home_page = top + index + bottom
#my_blog= top + blog + bottom
#my_project =top + project + bottom
#my_contact = top + contact + bottom

#open('docs/index.html','w+').write(home_page)
#open('docs/blog.html','a+').write(my_blog)
#open('docs/project.html','a+').write(my_project)
#open('docs/contact.html','a+').write(my_contact)



pages=[
      {'filename':'./content/index.html',
       'output' :'docs/index.html',
       'title':'Homepege',
      },
      {'filename':'./content/blog.html',
       'output' :'docs/blog.html',
       'title':'My blog',
      },
      {'filename':'./content/contact.html',
       'output' :'docs/contact.html',
       'title':'About me',
      },
      {'filename':'./content/projects.html',
       'output' :'docs/project.html',
       'title':'My project',
      }

]
def main():
    top = open('./templates/top.html').read()
    bottom = open('./templates/bottom.html').read()
    for page in pages:
        #print(page)
        
        title = page['title']
        print(title)
        filename = page['filename']
        print(filename)
        output = page['output']
        print(output)


# Read in the entire template
template = open('base.html').read()

# Read in the content of the index HTML page

index = open('./content/index.html').read()
blog=open('./content/blog.html').read()
contact=open('./content/contact.html').read()
project=open('./content/projects.html').read()

# Use the string replace
finished_index_page = template.replace("{{content}}", index)
open("docs/index.html", "w+").write(finished_index_page)

finished_blog_page = template.replace("{{content}}", blog)
open("docs/blog.html", "w+").write(finished_blog_page)

finished_contact_page = template.replace("{{content}}", contact)
open("docs/contact.html", "w+").write(finished_contact_page)

finished_project_page = template.replace("{{content}}", project)
open("docs/project.html", "w+").write(finished_project_page)



