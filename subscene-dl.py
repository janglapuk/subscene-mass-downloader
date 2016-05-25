import httplib2, sys, os

# lxml for parsing HTML
from lxml import html

def download(urlfile):
  # link lists
  links = []

  # open links file
  with open(urlfile) as f:
    # read link line by line and store into variable
    links = f.readlines()

  # iterate every links  
  for link in links:
    # normalize link, remove newline character and trim
    link = link.replace('\r', '').replace('\n', '').strip()

    # make request to the link
    resp, content = httplib2.Http().request(link)
    
    # if response status is OK
    if resp.status == 200:
      # create lxml HTML object by content
      objlxml = html.fromstring(content)  

      # get release name text for a good file name
      releaseName = objlxml.xpath("//li[@class='release']/div/text()")

      # if releasename is exist
      if len(releaseName):
        # normalize release name text
        filename = ''.join([x for x in releaseName]).replace('\r', '').replace('\n', '').strip()

        # print usefull info
        print('Downloading %s ...' % filename)

        # get download button element
        btnEl = objlxml.xpath("//a[@id='downloadButton']")

        # if button exist
        if len(btnEl):
          # get href attribute to get download URL
          downloadUrl = btnEl[0].get('href')

          #print(downloadUrl)
          
          # make second request to download URL
          resp, zipcontent = httplib2.Http().request('http://subscene.com' + downloadUrl)

          #print(resp)

          # if response status is OK
          if resp.status == 200:
            # create pre-download file as binary, because it's a zip file
            with open(filename + '.zip', 'wb') as fw:
              # and write downloaded content
              fw.write(zipcontent)

            # finally, print usefull info
            print('...%s done!\n' % filename)
          else:
            print('Error: cannot download %s.zip! (HTTP status: %d)\n' % (filename, resp.status))
    else:
      print('Error: cannot download %s! (HTTP status: %d)\n' % (link, resp.status))

def usage(argv):
  print('Usage: %s <links file>\n' % argv[0])

# main call
if __name__ == '__main__':
  # if filename given
  if len(sys.argv) is 2:
    # save file name
    textfile = sys.argv[1]

    # is right file?
    if os.path.isfile(textfile):

      # download!
      download(textfile)

    else:
      print('Error: wrong parameter!\n')
      usage(sys.argv)
  else:
    usage(sys.argv)