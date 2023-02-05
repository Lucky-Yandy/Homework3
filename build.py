






#################################################################


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




template = open('./templates/base.html').read() 



def handle_filename(page):
    
      
        filename = page['filename']
        print(filename)
        return filename

def handle_output(page):     
        output = page['output']
        print(output)
        return output



def main():
    
     for page in pages:
         filename=handle_filename(page)
         output=handle_output(page)
         
         handle_filename(page)# invoke the function
         handle_output(page)
         content = open(filename).read() 
        
         finished_page = template.replace("{{content}}", content)

         open(output, "w+").write(finished_page)
         
      
main()


