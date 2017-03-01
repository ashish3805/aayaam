import json
from pprint import pprint

with open('file.json') as data_file:    
    data = json.load(data_file)

for x in data:
    for i in range(0,len(x)):
        ename = data[x][i]["eventName"]
        dept = data[x][i]["clubdept"]
        tags = data[x][i]["tags"].split(", ")
        ttg = ""
        for gg in tags:
            ttg = "".join((gg,'|',ttg))
        
        head = ''.join(('<!doctype html><html lang="en" class="no-js"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="css/reset.css"><script src="js/modernizr.js"></script><link rel="stylesheet" href="css/style_new.css"><link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> <title>',ename,'</title><link href="event-details/min/plugin-min.css" type="text/css" rel="stylesheet"><link href="event-details/min/custom-min.css" type="text/css" rel="stylesheet"></head><body><div class="body-single cd-fold-content single-page" style="padding: 0;"><div class="banner section no-pad-bot">'))
        #isrc = data[x][i]["posterUrl"]
        src = data[x][i]["posterHostedUrl"]
        sec = ''.join(('<h1>',ename,'</h1><img src="',src,'" />        <div class="filter"></div>        </div>        <div id="intro" class="section scrollspy">            <div class="container">       <h4 class="promo-caption" style="text-align: center; font-weight: 800;font-weight: 1em;">',ttg,'',dept,'</h4><br><br><div class="row"><div class="col s12 m4 l4"><div class="center promo promo-example">                            <i class="material-icons">date_range</i>'))
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
        #reg = data[x][i]["onlineRegistrationDetails"]
        t =  "".join(('<div class="col s12 m4 l4"><div class="center promo promo-example"><i class="material-icons">location_on</i><br><h5 class="promo-caption">Venue</h5>                           <p class="light center">',venue,'</p>                        </div>                    </div>                    <div class="col s12 m4 l4">                        <div class="center promo promo-example">                            <i class="material-icons">call</i>                           <br><h5 class="promo-caption">',name,'</h5>                            <p class="light center">',contact,'<br>',email,'</p>                        </div>                    </div>                    <div class="col s12">                        <h2 class="center header text_h2"> ',desc,'</h2>                    </div>                </div>            </div>        </div>    </div></body><script src="js/jquery-2.1.1.js"></script><script src="js/main.js"></script><script src="event-details/min/plugin-min.js"></script><script src="event-details/min/custom-min.js"></script><!-- Resource jQuery --></body></html>'))  
        filename = ''.join(('item-',str(i+1),'.html'))
        head = "".join((head,t))
        obj = open(filename, 'wb')
        obj.write(head)
        obj.close