import csv
import ast
from copy import deepcopy

country_array = []
attribute_array_main = []

cn = dict()
cc = dict()
p = dict()

threshold=0

class Attribute:
	def __init__(self):
		self.code = None
		self.keywords = []
		self.desc = None
		self.units = None
		self.values = []
		self.expect = 0

	def __init__(self,keywords,desc,code,units):
		self.code = code
		self.keywords = []
		self.keywords = keywords
		self.desc = desc
		self.units = units
		self.values = []
		self.expect = 0

class Country:
	def __init__(self,code,name):
		self.attribute_array = []
		self.code=code
		self.name_array = []
		self.name_array.append(name)

	def addCountry(self,name):
		self.name_array.append(name)

	def addAttribute(self):
		for i in range(len(attribute_array_main)):
			self.attribute_array.append(deepcopy(attribute_array_main[i]))

class Sentence:
	def __init__(self):
		self.words = None
		self.code = None
		self.values = []
		self.country_name = []

	def __init__(self,code,words,values,country_name):
		self.words = words
		self.code = code
		self.values = []
		self.values = deepcopy(values)
		self.country_name = []
		self.country_name = country_name

	def Score(self,Country,value,Attribute):
		score=0
		if ( float(value) <  0.1 * float(Country.attribute_array[p[Attribute.code]].expect) ) : return 0
		wordings = self.words.split(' ')
		for w in wordings:
			for key in Attribute.keywords:
				if(key==w): score=score+1
		return score

	def doAll(self):
		for c in self.country_name:
			while ((c not in cn.keys() ) and ( c!="")):
				c=c[:len(c)-1]
			if c!="":
				cntry=country_array[cn[c]]
				for v in self.values:
					if v!="":
						for a in cntry.attribute_array:
							score = self.Score(cntry,v,a)
							if score > threshold:
								print (self.code , c , a.code , v , score)

def main():
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
		i.addAttribute()

	country_array[0].attribute_array[2].expect=10

	with open('kb-facts-train_SI.tsv','r') as fact_cin:
		fact_cin=csv.reader(fact_cin, delimiter='\t')
		count=0;exp=0;prevc="";prevp="";
		for row in fact_cin:
			if count==0: 
				exp=exp+float(row[1])
				count=count+1
				prevc=row[0]
				prevp=row[2]
			else :
				if ( prevc==row[0] and prevp==row[2] ):
					exp=exp+float(row[1])
					count=count+1
				else :
					Expect=(exp/count)
					country_array[cc[prevc]].attribute_array[p[prevp]].expect=Expect
					prevp=row[2]; prevc=row[0];
					exp=float(row[1])
					count=1
			country_array[cc[row[0]]].attribute_array[p[row[2]]].values.append(row[1])
		Expect=(exp/count)
		country_array[cc[prevc]].attribute_array[p[prevp]].expect=Expect
					
	with open('sentences.tsv','r') as sent_cin:
		sent_cin=csv.reader(sent_cin, delimiter='\t')
		count=0
		for row in sent_cin:
			a= Sentence(row[0].strip(),row[1],map(str.strip,row[2].split(',')),map(str.strip,row[3].split(',')))
			a.doAll()

main()