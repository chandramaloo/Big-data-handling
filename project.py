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
		self.words = None
		self.code = None
		self.values = []
		self.country_name = []

	def __init__(self,code,words,values,country_name):
		self.words = words
		self.code = None
		self.values = []
		self.values = values
		self.country_name = []
		self.country_name = country_name

	def Score(Country,value,Attribute):
		pass
# 		for w in words
# 			compare with country.Attribute[k].keywords 
# 		and find the score
#		if > cutoff print in a file all the needed fields

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
	
	for i in country_array:
		i.addAttribute(attribute_array_main)

	with open('kb-facts-train_SI.tsv','r') as fact_cin:
		fact_cin=csv.reader(fact_cin, delimiter='\t')
		count=0
		for row in fact_cin:
			country_array[cc[row[0]]].attribute_array[p[row[2]]].values.append(row[1])
	
	with open('sentences.tsv','r') as sent_cin:
		sent_cin=csv.reader(sent_cin, delimiter='\t')
		count=0
		for row in sent_cin:
			a= Sentence(row[0],row[1],map(str.strip,row[2].split(',')),map(str.strip,row[3].split(',')))
			a.doAll()

if __name__ == "__main__": main()