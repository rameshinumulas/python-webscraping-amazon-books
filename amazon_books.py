from bs4 import BeautifulSoup
import requests, pprint

page=requests.get("https://www.iplt20.com/stats/2019/")
soup=BeautifulSoup(page.text,"html.parser")
# print(soup)

main_div=soup.find("div",class_="col-10 col-9-wide col-12-tab stats-content")
main_div2=main_div.find("h1").text
# print(main_div2)

table_data=main_div.find("tr",class_="standings-table__header")
table_tr=table_data.find_all("th")
# print(table_tr)

title_list=[]
count=1
for j in table_tr:
	if count>1:
		title_list.append(j.text)
	count+=1



table_row_1=main_div.find("table",class_="standings-table standings-table--full")
team_1=table_row_1.find_all("tr")



match_data=[]
list_of_matches=[]
list_of_points=[]
teams_names=[]
count=1
for i in team_1:
	if count>1:
		team_data=i.find("span",class_="standings-table__team-name js-team").text
		teams_names.append(team_data)
		team_data_2=i.find_all("td",class_="standings-table__optional")
		for one in team_data_2:
			match_data.append(one.text)

		played_matches=i.find("td",class_="standings-table__padded").text
		list_of_matches.append(played_matches)

		team_points=i.find("td",class_="standings-table__highlight js-points").text
		list_of_points.append(team_points)
	count+=1
pprint.pprint(match_data)
pprint.pprint(list_of_matches)
pprint.pprint(list_of_points)
pprint.pprint(title_list)
pprint.pprint(teams_names)


# batting=soup.find("header",class_="widget__header stats-content__header widget__header--no-link-to")
# batting_leader=batting.find("h1").text
# print(batting_leader)

