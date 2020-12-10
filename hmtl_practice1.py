from bs4 import BeautifulSoup
import urllib.request as req
from  configparser import ConfigParser
#import pymysql


baseURL="https://www.babynames.com/blogs/names-blog/100-trending-names-of-2020/"
res=req.urlopen(baseURL)
soup = BeautifulSoup(res,'html.parser')

table=soup.find(class_="namos").find('td')

for name in table:
    print('\n\n')
    print(name)
    print('\n\n')
    #n_rank=name.find
    #name_count=0
    # for name in names:
    #     temp=[]
    #     name_number =name.attrs['id']
    #     title=name.find("span",attrs={"class":"col-xs-12 col-sm-3"}).find("a",attrs={"class":"expand"}).text.strip()
    #     c_info =name.find_all("span",attrs={"class":"col-xs-12 col-sm-2"})
        
    #     instructor_tmp = c_info[0].text.lstrip()
    #     instructor_tmp_a= instructor_tmp.replace("Office Hours","").lstrip()
    #     instructor = instructor_tmp_a.replace("\n","").lstrip()
    #     meeting_times_tmp= c_info[1].text.lstrip()
    #     meeting_times= meeting_times_tmp.replace("\n","")
    #     class_type= c_info[2].text.lstrip()
    #     if "CANCELLED" in instructor:
    #         instructor= ""
    #         meeting_times = ""
    #         class_type =""
    #         cancellation = "CANCELLED"
    #     else: 
    #         cancellation = "NOT CANCELLED"
        
    #     if class_type!="ONLINE":
    #         location=class_type
    #         class_type="OFFLINE"
    #     else:
    #         location=""
    #     #name_count=name_count+1;
        
    #     #PART-3 EXTRACTING DATA , SEEN TRHOUGH PRINT(CONTENTS)
    #     #instead of printing we should insert 
    #     # insert_name(conn,name_num,',',join(profs))
    #     print("------------------------")
    #     print("semester:    ",semester)
    #     print("name_number:   ",name_number)
    #     print("name_title:    ",title)
    #     print("instructor:  ",instructor)
    #     print("meeting_times:   ",meeting_times)
    #     print("class_type:  ",class_type)
    #     print("cancellation_status: ",cancellation)
    #     print("location:    ",location)
        
        #Part 1-6 
        #insert_names(conn,semester,name_number,title,instructor,meeting_times,class_type,location,cancellation)
    #print(name_count
