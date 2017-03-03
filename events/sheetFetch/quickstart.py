from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1NzHrpx8FD2jpy1H8i9PJ-eKnhjfuNy5EnTYaUJawGuU/edit#gid=1378942415
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1NzHrpx8FD2jpy1H8i9PJ-eKnhjfuNy5EnTYaUJawGuU'
    rangeName = 'A1:O'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:        
        index_head = '<!doctype html><html lang="en" class="no-js"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">    <link href="http://fonts.googleapis.com/css?family=Vollkorn|Open+Sans:400,700" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">    <link href="event-details/min/plugin-min.css" type="text/css" rel="stylesheet">    <link href="event-details/min/custom-min.css" type="text/css" rel="stylesheet">    <link rel="stylesheet" href="css/reset.css">    <!-- CSS reset -->    <link rel="stylesheet" href="css/style.css">    <link rel="stylesheet" href="css/style_new.css">    <!-- Resource style -->    <script src="js/modernizr.js"></script>    <!-- Modernizr -->    <title>Events :AAYAAM 2017</title></head><body>    <main class="cd-main">        <header>            <h1>Aayaam 2017 Events</h1>            <div class="cd-nugget-info"><a href="https://aayaam.sgsits.ac.in"><span><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" ="0px" idth="16px" height="16px" viewBox="0 0 16 16" style="enable-background:new 0 0 16 16;" xml:space="preserve"><style type="text/css">.cd-nugget-info-arrow{fill:#383838;}</style><polygon lass="cd-nugget-info-arrow" points="15,7 4.4,7 8.4,3 7,1.6 0.6,8 0.6,8 0.6,8 7,14.4 8.4,13 4.4,9 15,9 "/>	</svg></span> BACK</a></div> <!-- cd-nugget-info -->    </header><ul class="cd-gallery" id="gallery-list">'

        index_foot = '</ul><!-- .cd-gallery --></main><!-- .cd-main --><div class="cd-folding-panel"><div class="fold-left"></div><!-- this is the left fold -->        <div class="fold-right"></div><!-- this is the right fold --><div class="cd-fold-content" style="padding:0px; overflow-x: hidden ">      <!-- content will be loaded using javascript -->            <!--COTENT START--><!--CONTENT END--></div>        <a class="cd-close" href="#0"></a>    </div>   <!-- cd-folding-panel -->    <script  src="js/jquery-2.1.1.js"></script>    <script src="js/main.js"></script>        <script src="event-details/min/plugin-min.js"></script><script src="event-details/min/custom-min.js"></script><!-- Resource jQuery --></body></html>'

        index_li = ''
        i=0
        for row in values:            
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
            if i==0:
                i = i+1
                continue            
            ename = row[1]
            dept = row[3]
            tags = row[2]
            ttg = tags.replace(",","|")
            
            head = u''.join(('<!doctype html><html lang="en" class="no-js"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="css/reset.css"><script src="js/modernizr.js"></script><link rel="stylesheet" href="css/style_new.css"><link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> <title>',ename,'</title><link href="event-details/min/plugin-min.css" type="text/css" rel="stylesheet"><link href="event-details/min/custom-min.css" type="text/css" rel="stylesheet"></head><body><div class="body-single cd-fold-content single-page" style="padding: 0;"><div class="banner section no-pad-bot">')).encode('utf-8').strip()
            #isrc = row[10]
            src = row[11]
            sec = u''.join(('<h1>',ename,'</h1><img src="',src,'" />        <div class="filter"></div>        </div>        <div id="intro" class="section scrollspy">            <div class="container">       <h4 class="promo-caption" style="text-align: center; font-weight: 800;font-weight: 1em;">',ttg,'</h4><br><br><div class="row"><div class="col s12 m4 l4"><div class="center promo promo-example">                            <i class="material-icons">date_range</i>')).encode('utf-8').strip()
            head = "".join((head,sec)).encode('utf-8').strip()
            venue ="SGSITS"
            venue = row[12]
            date = row[13]
            time = row[14]
            time = "".join(('<br><h5 class="promo-caption">',date,'</h5> <p class="light center">Time ',time,'</p> </div></div>'))
            time = "".join((time,'')).encode('utf-8').strip()
            head = "".join((head,time)).encode('utf-8').strip()        
            contact = row[6]
            email = row[7]
            name = row[5]
            link = row[9]
            desc = u''.join((row[4])).encode('utf-8').strip()
            desc = desc.replace("\n","<br>")
            reg = row[8]
            t =  "".join(('<div class="col s12 m4 l4"><div class="center promo promo-example"><i class="material-icons">location_on</i><br><h5 class="promo-caption">Venue</h5>                           <p class="light center">',venue,'</p>                        </div>                    </div>                    <div class="col s12 m4 l4">                        <div class="center promo promo-example">                            <i class="material-icons">call</i>                           <br><h5 class="promo-caption">',name,'</h5>                            <p class="light center">',contact,'<br>',email,'</p>                        </div>                    </div>                    <div class="col s12">                       <br> <p> ',desc,'</p>  <br>                  </div>                </div>    <!--button secton-->           <div class="row">    <div class="col s6" style="text-align:right"><a href="',reg,'" class="btn waves-effect waves-light red darken-1" >Register</a></div><div class="col s6" style="text-align:left"><a href="',link,'" class="btn aves-effect waves-light blue darken-1" >Website</a>                </div>            </div><!--utoon section ends-->        </div>        </div>    </div></body><script src="js/jquery-2.1.1.js"></script><script src="js/main.js"></script><script src="event-details/min/plugin-min.js"></script><script src="event-details/min/custom-min.js"></script><!-- Resource jQuery --></body></html>')).encode('utf-8').strip()  
            filename = ''.join(('../item-',str(i),'.html')).encode('utf-8').strip()
            head = "".join((head,t)).encode('utf-8').strip()
            index_li = "".join((index_li,'<li class="cd-item"><a class="dark-text" href="',''.join(('item-',str(i),'.html')).encode('utf-8'),'"><div><h2>',ename,'</h2><p>',ttg,'</p><b>View More</b></div></a></li>')).encode('utf-8').strip()
            i= i+1
            obj = open(filename, 'wb')
            obj.write(head)
            obj.close

        indexcon = "".join((index_head,index_li,index_foot)).encode('utf-8').strip()
        obj = open('../index.html', 'wb')
        obj.write(indexcon)
        obj.close


if __name__ == '__main__':
    main()
