

template = open('./templates/base.html').read() 

pages=[
      
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
    for page in pages:
        title = page['title']
        print(title)
        filename = page['filename']
        print(filename)
        output = page['output']
        print(output)
        content = open(filename).read() 
        finished_page = template.replace("{{content}}", content)

        open(output, "w+").write(finished_page)
      

main()

    
    
    



