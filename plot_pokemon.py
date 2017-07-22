import pygal
from pygal.style import Style

#import my pokemon.py file to retrieve the dictionaries.
import pokemon as poke

#style for the radar chart
custom_style = Style(
	background='transparent',
	plot_background='#ffffff',
	opacity='0.1',
	opacity_hover='0.9',
	transition='400ms ease-out',
	colors=('#d22800', '#00aad2', '#000000', '#d3d3d3', '#008000', '11006c'),
	font_family='googlefont:VT323',
	major_label_font_size=16,
	label_font_size=16,
	title_font_size=40,
	legend_font_size=24,
	tooltip_font_size=16)

radar_chart = pygal.Radar(fill=True, style=custom_style)
radar_chart.title = 'Number of Each Type Per Generation'

#set the x labels
radar_chart.x_labels = ['Psychic', 'Ice', 'Flying', 'Ground', 'Electric',
    'Normal', 'Water', 'Fire', 'Fairy', 'Rock', 'Dark', 'Bug', 'Poison', 
    'Ghost', 'Fighting', 'Dragon', 'Grass', 'Steel']

#add the data from each generation corresponding to the x labels
radar_chart.add('Gen 1: Kanto', [poke.generation_1['Psychic'],
	poke.generation_1['Ice'], poke.generation_1['Flying'], 
	poke.generation_1['Ground'], poke.generation_1['Electric'],
	poke.generation_1['Normal'], poke.generation_1['Water'],
	poke.generation_1['Fire'], poke.generation_1['Fairy'],
	poke.generation_1['Rock'], poke.generation_1['Dark'],
	poke.generation_1['Bug'], poke.generation_1['Poison'],
	poke.generation_1['Ghost'], poke.generation_1['Fighting'],
	poke.generation_1['Dragon'], poke.generation_1['Grass'],
	poke.generation_1['Steel']])

radar_chart.add('Gen 2: Johto', [poke.generation_2['Psychic'],
	poke.generation_2['Ice'], poke.generation_2['Flying'], 
	poke.generation_2['Ground'], poke.generation_2['Electric'],
	poke.generation_2['Normal'], poke.generation_2['Water'],
	poke.generation_2['Fire'], poke.generation_2['Fairy'],
	poke.generation_2['Rock'], poke.generation_2['Dark'],
	poke.generation_2['Bug'], poke.generation_2['Poison'],
	poke.generation_2['Ghost'], poke.generation_2['Fighting'],
	poke.generation_2['Dragon'], poke.generation_2['Grass'],
	poke.generation_2['Steel']])

radar_chart.add('Gen 3: Hoenn', [poke.generation_3['Psychic'],
	poke.generation_3['Ice'], poke.generation_3['Flying'], 
	poke.generation_3['Ground'], poke.generation_3['Electric'],
	poke.generation_3['Normal'], poke.generation_3['Water'],
	poke.generation_3['Fire'], poke.generation_3['Fairy'],
	poke.generation_3['Rock'], poke.generation_3['Dark'],
	poke.generation_3['Bug'], poke.generation_3['Poison'],
	poke.generation_3['Ghost'], poke.generation_3['Fighting'],
	poke.generation_3['Dragon'], poke.generation_3['Grass'],
	poke.generation_3['Steel']])

radar_chart.add('Gen 4: Sinnoh', [poke.generation_4['Psychic'],
	poke.generation_4['Ice'], poke.generation_4['Flying'], 
	poke.generation_4['Ground'], poke.generation_4['Electric'],
	poke.generation_4['Normal'], poke.generation_4['Water'],
	poke.generation_4['Fire'], poke.generation_4['Fairy'],
	poke.generation_4['Rock'], poke.generation_4['Dark'],
	poke.generation_4['Bug'], poke.generation_4['Poison'],
	poke.generation_4['Ghost'], poke.generation_4['Fighting'],
	poke.generation_4['Dragon'], poke.generation_4['Grass'],
	poke.generation_4['Steel']])

radar_chart.add('Gen 5: Unova', [poke.generation_5['Psychic'],
	poke.generation_5['Ice'], poke.generation_5['Flying'], 
	poke.generation_5['Ground'], poke.generation_5['Electric'],
	poke.generation_5['Normal'], poke.generation_5['Water'],
	poke.generation_5['Fire'], poke.generation_5['Fairy'],
	poke.generation_5['Rock'], poke.generation_5['Dark'],
	poke.generation_5['Bug'], poke.generation_5['Poison'],
	poke.generation_5['Ghost'], poke.generation_5['Fighting'],
	poke.generation_5['Dragon'], poke.generation_5['Grass'],
	poke.generation_5['Steel']])

radar_chart.add('Gen 6: Kalos', [poke.generation_6['Psychic'],
	poke.generation_6['Ice'], poke.generation_6['Flying'], 
	poke.generation_6['Ground'], poke.generation_6['Electric'],
	poke.generation_6['Normal'], poke.generation_6['Water'],
	poke.generation_6['Fire'], poke.generation_6['Fairy'],
	poke.generation_6['Rock'], poke.generation_6['Dark'],
	poke.generation_6['Bug'], poke.generation_6['Poison'],
	poke.generation_6['Ghost'], poke.generation_6['Fighting'],
	poke.generation_6['Dragon'], poke.generation_6['Grass'],
	poke.generation_6['Steel']])

#output the file as an svg file
radar_chart.render_to_file('poke_radar_chart.svg')