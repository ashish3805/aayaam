import json
from pprint import pprint

with open('file.json') as data_file:    
    data = json.load(data_file)

index_head = '<!doctype html><html lang="en" class="no-js"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">    <link href="http://fonts.googleapis.com/css?family=Vollkorn|Open+Sans:400,700" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">    <link href="event-details/min/plugin-min.css" type="text/css" rel="stylesheet">    <link href="event-details/min/custom-min.css" type="text/css" rel="stylesheet">    <link rel="stylesheet" href="css/reset.css">    <!-- CSS reset -->    <link rel="stylesheet" href="css/style.css">    <link rel="stylesheet" href="css/style_new.css">    <!-- Resource style -->    <script src="js/modernizr.js"></script>    <!-- Modernizr -->    <title>Events :AAYAAM 2017</title></head><body>    <main class="cd-main">        <header>            <h1>Aayaam 2017 Events</h1>            <div class="cd-nugget-info"><a href="https://aayaam.sgsits.ac.in"><span><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" ="0px" idth="16px" height="16px" viewBox="0 0 16 16" style="enable-background:new 0 0 16 16;" xml:space="preserve"><style type="text/css">.cd-nugget-info-arrow{fill:#383838;}</style><polygon lass="cd-nugget-info-arrow" points="15,7 4.4,7 8.4,3 7,1.6 0.6,8 0.6,8 0.6,8 7,14.4 8.4,13 4.4,9 15,9 "/>	</svg></span> BACK</a></div> <!-- cd-nugget-info -->    </header><ul class="cd-gallery" id="gallery-list">'

index_foot = '</ul><!-- .cd-gallery --></main><!-- .cd-main --><div class="cd-folding-panel"><div class="fold-left"></div><!-- this is the left fold -->        <div class="fold-right"></div><!-- this is the right fold --><div class="cd-fold-content" style="padding:0px; overflow-x: hidden ">      <!-- content will be loaded using javascript -->            <!--COTENT START--><!--CONTENT END--></div>        <a class="cd-close" href="#0"></a>    </div>   <!-- cd-folding-panel -->    <script  src="js/jquery-2.1.1.js"></script>    <script src="js/main.js"></script>        <script src="event-details/min/plugin-min.js"></script><script src="event-details/min/custom-min.js"></script><!-- Resource jQuery --></body></html>'

index_li = ''

for x in data:
    len_x = len(data[x])
    for i in range(0,len_x):
        ename = data[x][i]["eventName"]
        dept = data[x][i]["clubdept"]
        tags = data[x][i]["tags"]
        ttg = tags.replace(",","|")
        
        head = ''.join(('<!doctype html><html lang="en" class="no-js"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="css/reset.css"><script src="js/modernizr.js"></script><link rel="stylesheet" href="css/style_new.css"><link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> <title>',ename,'</title><link href="event-details/min/plugin-min.css" type="text/css" rel="stylesheet"><link href="event-details/min/custom-min.css" type="text/css" rel="stylesheet"></head><body><div class="body-single cd-fold-content single-page" style="padding: 0;"><div class="banner section no-pad-bot">'))
        #isrc = data[x][i]["posterUrl"]
        src = data[x][i]["posterHostedUrl"]
        sec = ''.join(('<h1>',ename,'</h1><img src="',src,'" />        <div class="filter"></div>        </div>        <div id="intro" class="section scrollspy">            <div class="container">       <h4 class="promo-caption" style="text-align: center; font-weight: 800;font-weight: 1em;">',ttg,'</h4><br><br><div class="row"><div class="col s12 m4 l4"><div class="center promo promo-example">                            <i class="material-icons">date_range</i>'))
        head = "".join((head,sec))
        
        venue = "Cafeteria"
        time = '<br><h5 class="promo-caption">10 March</h5> <p class="light center">Time 11:00 AM to 12:00 PM</p> </div></div>'
        #time = "".join((time,''))
        head = "".join((head,time))        
        contact = str(data[x][i]["contactMobile"])
        email = data[x][i]["email"]
        name = data[x][i]["nameOfContactPerson"]
        #link = data[x][i]["websiteOfTheEvent"]        
        desc = data[x][i]["description"]
        desc = desc.replace("\n","<br>")
        #reg = data[x][i]["onlineRegistrationDetails"]
        t =  "".join(('<div class="col s12 m4 l4"><div class="center promo promo-example"><i class="material-icons">location_on</i><br><h5 class="promo-caption">Venue</h5>                           <p class="light center">',venue,'</p>                        </div>                    </div>                    <div class="col s12 m4 l4">                        <div class="center promo promo-example">                            <i class="material-icons">call</i>                           <br><h5 class="promo-caption">',name,'</h5>                            <p class="light center">',contact,'<br>',email,'</p>                        </div>                    </div>                    <div class="col s12">                        <h2 class="center header text_h2"> ',desc,'</h2>                    </div>                </div>            </div>        </div>    </div></body><script src="js/jquery-2.1.1.js"></script><script src="js/main.js"></script><script src="event-details/min/plugin-min.js"></script><script src="event-details/min/custom-min.js"></script><!-- Resource jQuery --></body></html>'))  
        filename = ''.join(('item-',str(i+1),'.html'))
        head = "".join((head,t))
        index_li = "".join((index_li,'<li class="cd-item"><a class="dark-text" href="',filename,'"><div><h2>',ename,'</h2><p>',ttg,'</p><b>View More</b></div></a></li>'))
        obj = open(filename, 'wb')
        obj.write(head)
        obj.close

indexcon = "".join((index_head,index_li,index_foot))
obj = open('index.html', 'wb')
obj.write(indexcon)
obj.close