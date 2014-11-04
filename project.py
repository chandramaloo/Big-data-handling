import csv

country_array = []

cn = dict()
cc = dict()
p = dict()

class Attribute:
	def __init__(self):
		self.code = None
		self.keywords = []
		self.desc = None
		self.units = None
		self.values = []

	def __init__(self,keywords,desc,code,units):
		self.code = code
		self.keywords = []
		self.keywords = keywords
		self.desc = desc
		self.units = units
		self.values = []

attribute_array_main = []

class Country:
	
	def __init__(self,code,name):
		self.attribute_array = []
		self.code=code
		self.name_array = []
		self.name_array.append(name)

	def addCountry(self,name):
		self.name_array.append(name)

	def addAttribute(self,attribute = []):
		for i in range(len(attribute)):
			self.attribute_array.append(attribute[i])

	def setValue(self,code,value):
		self.attribute_array[p[code]].values.append(value)


class Sentence:
	def __init__(self):
		self.words = []
		self.code = None
		self.values = []
		self.country_name = []

	def Score(Country,value,Attribute):
		pass
# 		for w in words
# 			compare with country.Attribute[k].keywords 

	def doAll(self):
		for c in country_array[cn[self.country_name]]:
			for v in values:
				for a in country_array[cn[self.country_name]].attribute_array:
					self.Score(c,v,a)

def main():
	#reading countries_id_map
	with open('countries_id_map.txt','r') as country_cin:
		country_cin=csv.reader(country_cin, delimiter='\t')
		count=0	
		for row in country_cin:
			if(count>0):
				if (country_array[count-1].code) == row[0]:
					country_array[count-1].name_array.append(row[1])
					cn[row[1]]=count-1
				else:
					ct=Country(row[0], row[1])
					country_array.append(ct)
					cn[row[1]]=count
					cc[row[0]]=count
					count=count+1
			else:
				ct=Country(row[0], row[1])
				country_array.append(ct)
				cn[row[1]]=count
				cc[row[0]]=count
				count=count+1
	
	# with open('text.csv', 'w') as cin:
	# 	cin=csv.writer(cin, delimiter='\t')
	# 	for i in country_array:
	# 		cin.writerow([i.code,i.name_array])
	# #make attribute array - selected_indicators / target-relations.tsv; p[code]=integer
		with open('selected_indicators','r') as attrib_cin:
			attrib_cin=csv.reader(attrib_cin, delimiter='\t')
			count=0
			for row in attrib_cin:
				key=row[0].split('_')
				if len(row)==3:	ext=""
				else: ext=row[3]
				ct=Attribute(key, row[1], row[2], ext)
				attribute_array_main.append(ct)
				p[row[2]]=count
				count=count+1
		
		with open('text.csv', 'w') as cin:
		 	cin=csv.writer(cin, delimiter='\t')
		 	for i in attribute_array_main:
		 		cin.writerow([i.code,i.keywords,i.desc,i.units])
# 	#copy into each country and populate values - kb-facts-train_SI.tsv

# 	#create output.csv
# 	#iterate through sentences

if __name__ == "__main__": main()