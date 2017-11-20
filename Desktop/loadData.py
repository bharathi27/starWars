#!/usr/bin/env python
# -*- coding: utf-8 -*-


##------------------------------------------------------------##
# Import Libraries
##------------------------------------------------------------##

from __future__ import print_function
from dbConnection import config
from mysql.connector import errorcode
import mysql.connector, json, ast, requests

link = mysql.connector.connect(**config)
cursor = link.cursor(buffered=True)

##------------------------------------------------------------##
# Loading All of Film & Planets Data
##------------------------------------------------------------##

mainclass = ['planets','films']
	
for i in mainclass:

	url = "https://swapi.co/api/" + i 

	response = requests.get(url)

	if response.status_code != 200 :
		print('Resource Not Available')
	else:
		data = response.json()
		if i == 'planets':
			print('Planets Data loading...')
			count = 9
		elif i == 'films':
			print('Planets Data loading completed')
			print('Films Data loading....')
			count = 7


		for j in range(0,count):

			if i == 'planets':

				iter_data = (data['results'][j])
				iter_data = (ast.literal_eval(json.dumps(iter_data)))

				if iter_data['residents'] != []:
					res_iter_data = []
					for k in iter_data['residents']:
						res_response = requests.get(k)
						res_data = res_response.json()
						res_iter_data.append(ast.literal_eval(json.dumps(res_data['name'])))
				
				if iter_data['films'] != []:
					film_iter_data = []
					for k in iter_data['films']:
						film_response = requests.get(k)
						film_data = film_response.json()
						film_iter_data.append(ast.literal_eval(json.dumps(film_data['title'])))


				query = "INSERT INTO planets(name,rotation_period,orbital_period,diameter,climate,gravity,terrain,surface_water,population,residents,films,created,edited,url) VALUES (%s, %s ,%s, %s, %s,%s,%s,%s,%s,%s, %s,%s,%s,%s);"
				cursor.execute(query,(iter_data['name'],iter_data['rotation_period'],iter_data['orbital_period'],iter_data['diameter'],iter_data['climate'],iter_data['gravity'],iter_data['terrain'],iter_data['surface_water'],iter_data['population'],str(res_iter_data),str(film_iter_data),iter_data['created'],iter_data['edited'],iter_data['url'],))


			elif i == 'films':
				
				iter_data = (data['results'][j])
				iter_data = (ast.literal_eval(json.dumps(iter_data)))
				
				if iter_data['characters'] != []:
					characters_iter_data = []
					for k in iter_data['characters']:
						characters_response = requests.get(k)
						characters_data = characters_response.json()
						characters_iter_data.append(ast.literal_eval(json.dumps(characters_data['name'])))
				
				if iter_data['planets'] != []:
					planets_iter_data = []
					for k in iter_data['planets']:
						planets_response = requests.get(k)
						planets_data = planets_response.json()
						planets_iter_data.append(ast.literal_eval(json.dumps(planets_data['name'])))

				if iter_data['starships'] != []:
					starships_iter_data = []
					for k in iter_data['starships']:
						starships_response = requests.get(k)
						starships_data = starships_response.json()
						starships_iter_data.append(ast.literal_eval(json.dumps(starships_data['name'])))
				
				if iter_data['vehicles'] != []:
					vehicles_iter_data = []
					for k in iter_data['vehicles']:
						vehicles_response = requests.get(k)
						vehicles_data = vehicles_response.json()
						vehicles_iter_data.append(ast.literal_eval(json.dumps(vehicles_data['name'])))

				if iter_data['species'] != []:
					species_iter_data = []
					for k in iter_data['species']:
						species_response = requests.get(k)
						species_data = species_response.json()
						species_iter_data.append(ast.literal_eval(json.dumps(species_data['name'])))
			
				query = "INSERT INTO films(title,episode_id,opening_crawl,director,producer,release_date,characters,planets,starships,vehicles,species,created,edited,url) VALUES (%s, %s ,%s, %s, %s,%s,%s,%s,%s,%s, %s,%s,%s,%s);"
				cursor.execute(query,(iter_data['title'],iter_data['episode_id'],iter_data['opening_crawl'],iter_data['director'],iter_data['producer'],iter_data['release_date'],str(characters_iter_data),str(planets_iter_data),str(starships_iter_data),str(vehicles_iter_data),str(species_iter_data),iter_data['created'],iter_data['edited'],iter_data['url'],))

				
link.commit()

print('Data loading completed')

cursor.close()
link.close()

'''
##------------------------------------------------------------##
# SAMPLE Code : For fetching individual film/planet data
##------------------------------------------------------------##



# Receive User Input

print "Choose films/planets followed by their number :",
print "Eg : planets/1/ \n",

input_data = raw_input()
input_data = input_data.lower()
url = "https://swapi.co/api/" + input_data
print url

response = requests.get(url)
if response.status_code != 200 :
	print 'Resource Not Available'
else:
	data = response.json()
	data = ast.literal_eval(json.dumps(data))

##------------------------------------------------------------##
# Fetches column names from tables to avoid re-usability
##------------------------------------------------------------##


mainclass = ['planets']
	
for i in mainclass:

print (i)
	query = "SELECT column_name FROM information_schema.columns WHERE table_name = %s;"
	cursor.execute (query, (i,))  
	
	for column_name in cursor:
		if i == 'planets':
			planets_col_names.append(ast.literal_eval(json.dumps(column_name))[0])
		elif i == 'films':
			films_col_names.append(ast.literal_eval(json.dumps(column_name))[0])

	planets_col_names = planets_col_names[1:]
	films_col_names = films_col_names[1:]


'''
##------------------------------------------------------------##
##------------------------------------------------------------##