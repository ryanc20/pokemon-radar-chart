# Pokemon Radar Chart
Pokemon Radar Chart that shows the amount of each type (Fire type, Water type, etc.) for each generation of the Pokemon series.
## Example Code
```python
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
 ```
 ## Motivation
 Pokemon has been one of my favorite games since I was child and I stumbled upon a dataset that contained each pokemon and their type. I thought it would be interesting to visualize the amount of pokemon of each type have been made per generation. This dataset is missing is the most recent 7th generation so I would like to create a model to attempt to predict the amount of each type that the 7th generation has based on the previous attempts. I do not expect good results, but I think it would be an interesting project.
 
 ## Reference
 The Pokemon dataset that I used was found off the website [Kaggle](https://www.kaggle.com/abcsds/pokemon) by the user 'abcsds'.
