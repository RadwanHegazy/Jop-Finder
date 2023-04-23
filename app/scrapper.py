import requests
from bs4 import BeautifulSoup
import json




def ScrapMainSite( link ) :
    req = requests.get( link , headers =  {"Content-Type": "application/json" ,"Cookie":"abcdefgh",'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})

    soup = BeautifulSoup( req.text, 'html.parser' )

    return soup





class GetJops ():

    def __init__(self, keyword) :
        
        # saved jops
        self.jops = []
        
        # verfied websites
        self.websites = [self.Mostaql, self.Guru, self.PeoplePerHour, self.Freelancer]
        
        # scrap data from websites
        for website in self.websites :
            website(keyword)

    
    def AppendDataToJops (self, **data) : 
        
        self.jops.append({
            'title' : data['title'],
            'description' : data['description'],
            'website' : data['website'],
            'url' : data['url'],
            'publish_in' : data['publish_in'],
        })


    def Mostaql ( self, keyword ) :

        search_link = 'https://mostaql.com/projects?keyword=' + keyword

        info = ScrapMainSite( search_link )
        
        jops = info.find_all('tr',{'class':'project-row'})

        website = 'https://mostaql.com/'

        for jop in jops :
            title = jop.find('h2',{'class':'mrg--bt-reset'}).find('a').text 
            time_delay = jop.find('time').text
            description = jop.find('p',{'class':'project__brief'}).text
            jop_link = jop.find('a',{'class':'details-url'}).get('href')

            # Save Recived Jops
            self.AppendDataToJops(title=title,description=description
                                  ,url=jop_link,website=website,publish_in=time_delay)

        


    def Guru ( self, keyword) : 

        search_link = f'https://www.guru.com/d/jobs/skill/{ keyword }/'

        info = ScrapMainSite( link = search_link )

        ul = info.find_all( 'div',{'class':'record jobRecord'} )

        website = 'https://www.guru.com/'

        for jop in ul :
            
            publish_in = jop.find('div',{'class':'jobRecord__meta'}).find('strong').text
            info_ = jop.find('h2',{'class':'jobRecord__title jobRecord__title--changeVisited'}).find('a')
            title = info_.text
            url = "https://www.guru.com" + info_.get('href')
            description = jop.find('p',{'class':'jobRecord__desc'}).text
            
            # Save Recived Jops
            self.AppendDataToJops(title=title,description=description
                                  ,url=url,website=website,publish_in=publish_in)

    



    def PeoplePerHour ( self, keyword ) :
        
        search_url = f'https://www.peopleperhour.com/freelance-{ keyword }-jobs'

        info = ScrapMainSite( search_url )

        jops = info.find_all( 'li', {'class':'list__item⤍List⤚2ytmm'} )
        
        website = 'https://www.peopleperhour.com/'

        for jop in jops : 
            
            a = jop.find('a', {'class':'item__url⤍ListItem⤚20ULx'})
            title = a.text
            url = a.get('href')
            publish_in = jop.find('time').text

            # Save Recived Jops
            self.AppendDataToJops(title=title,description=None
                                  ,url=url,website=website,publish_in=publish_in)






    def Freelancer ( self, keyword ) :

        data = ScrapMainSite(f'https://www.freelancer.com/jobs/{keyword}?keyword={keyword}/')

        jops = data.find_all('div',{'class':'JobSearchCard-item'})

        website = 'https://www.freelancer.com/'
        
        for jop in jops :

            a = jop.find('a',{'class':'JobSearchCard-primary-heading-link'})
            
            
            title = a.text
            url = "https://www.freelancer.com" + a.get('href')
            publish_in = jop.find('span',{'class':'JobSearchCard-primary-heading-days'}).text
            description = jop.find('p',{'class':'JobSearchCard-primary-description'}).text

            # Save Recived Jops
            self.AppendDataToJops(title=title,description=description
                                  ,url=url,website=website,publish_in=publish_in)



