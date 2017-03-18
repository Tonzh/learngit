#coding-utf-8
from fontTools import ttx

#define chars
# Consonants (classes C, CB, CN)
Consonants = ['uni0918',
            'uni0919',
			'uni091A',
			'uni091B',
			'uni091D',
			'uni091E',
			'uni091F',
			'uni0920',
			'uni0923',
			'uni0924',
			'uni0925',
			'uni0926',
			'uni0927',
			'uni092A',
			'uni092C',
			'uni092D',
			'uni092E',
			'uni0932',
			'uni0935',
			'uni0936',
			'uni0937',
			'uni0938',
			'uni0939',
			'uni0915',
			'uni0916',
			'uni0917',
			'uni091C',
			'uni0921',
			'uni0922',
			'uni0928',
			'uni092B',
			'uni092F',
			'uni0930',
			'uni0933',
			'uni0929',
			'uni0931',
			'uni0934',
			'uni0958',
			'uni0959',
			'uni095A',
			'uni095B',
			'uni095C',
			'uni095D',
			'uni095E',
			'uni095F'] 

# Independent vowels (class V)
Vowels = ['uni0905',
		'uni0906',
		'uni0907',
		'uni0908',
		'uni0909',
		'uni090A',
		'uni090B',
		'uni0960',
		'uni090C',
		'uni0961',
		'uni090F',
		'uni0910',
		'uni0913',
		'uni0914',
		'uni0904',
		'uni090E',
		'uni0912',
		'uni090D',
		'uni0911,'] 

# Dependent vowel signs (class M)
Matras = ['uni093E',
		'uni093F',
		'uni0940',
		'uni0941',
		'uni0942',
		'uni0943',
		'uni0944',
		'uni0962',
		'uni0963',
		'uni0947',
		'uni0948',
		'uni094B',
		'uni094C',
		'uni0946',
		'uni094A',
		'uni0945',
		'uni0949']

# Modifiers (class D)
Dodifiers = ['uni0901',
			'uni0902',
			'uni0903']
			
# Virama (class H)
Halant = ['uni094D']

# Nukta (class N)
Nukta = ['uni093C'] 

# Return lookuplist as the langsys
def GetLookupIdx(langsys): 
	featureIndex = langsys.FeatureIndex
	featureRecords = featureList.FeatureRecord
	lookuplist = []
	for i in featureIndex:
		featureRecord = featureRecords[i]
		lookuplist.extend(featureRecord.Feature.LookupListIndex)
	return lookuplist

def ReadLookup(lookup):
	# print 'LookupType = ',lookup.LookupType
	# print 'SubTableCount = ',lookup.SubTableCount
	if lookup.LookupType == 1: 
		for i in range(lookup.SubTableCount):
			print 'SubTable ',i,', Format = ',lookup.SubTable[i].Format
			print lookup.SubTable[i].mapping
	if lookup.LookupType == 2:
		for i in range(lookup.SubTableCount):
			print 'SubTable ',i,', Format = ',lookup.SubTable[i].Format
			print lookup.SubTable[i].mapping
	if lookup.LookupType == 3:
		pass
	if lookup.LookupType == 4:
		for i in range(lookup.SubTableCount):
			print 'SubTable ',i,', Format = ',lookup.SubTable[i].Format
			for key,ligatures in lookup.SubTable[i].ligatures.items():
				print 'keys Glyph ',key
				for lig in ligatures:
					print "components = ",lig.Component,' LigGlyph = ',lig.LigGlyph
	if lookup.LookupType == 5:
		lookuplist = set()
		for i in range(lookup.SubTableCount):
			subTable = lookup.SubTable[i]
			if subTable.Format == 1:
				# print 'SubTable ',i,', Format = ',subTable.Format
				# print "Coverage Glyphs", subTable.Coverage.glyphs
				for subRuleSet in subTable.SubRuleSet:
					for subRule in subRuleSet.SubRule:
						# print "Input: ", subRule.Input
						for LookupRecord in subRule.SubstLookupRecord:
							# print "Seqindex: ",LookupRecord.SequenceIndex,' LookupIndex: ',LookupRecord.LookupListIndex
							lookuplist.add(LookupRecord.LookupListIndex)
			elif subTable.Format == 2:
				# print 'SubTable ',i,', Format = ',subTable.Format
				# print "Coverage Glyphs", subTable.Coverage.glyphs
				# print "ClassDef: ", subTable.ClassDef.classDefs
				for subClassSet in subTable.SubClassSet:				
					if subClassSet!= None:
						for subRule in subClassSet.SubClassRule:
							# print "Class: ", subRule.Class
							for LookupRecord in subRule.SubstLookupRecord:
								# print "Seqindex: ",LookupRecord.SequenceIndex,' LookupIndex: ',LookupRecord.LookupListIndex
								lookuplist.add(LookupRecord.LookupListIndex)
		return lookuplist
	
	if lookup.LookupType == 6:
		lookuplist = set()
		for i in range(lookup.SubTableCount):
			subTable = lookup.SubTable[i]
			if subTable.Format == 2:
				# print 'SubTable ',i,', Format = ',subTable.Format
				# print "Coverage Glyphs", subTable.Coverage.glyphs
				# print "BacktrackClassDef: ", subTable.BacktrackClassDef.classDefs
				# print "InputClassDef: ", subTable.InputClassDef.classDefs
				# print "LookAheadClassDef: ", subTable.LookAheadClassDef.classDefs
				for chainSubClassSet in subTable.ChainSubClassSet:				
					if chainSubClassSet!= None:
						for ChainSubClassRule in chainSubClassSet.ChainSubClassRule:
							# if ChainSubClassRule.BacktrackGlyphCount > 0:
								# print "BacktrackGlyph: ", ChainSubClassRule.Backtrack
							# if ChainSubClassRule.InputGlyphCount > 0:
								# print "InputGlyph: ", ChainSubClassRule.Input
							# if ChainSubClassRule.LookAheadGlyphCount > 0:
								# print "LookAheadGlyph: ", ChainSubClassRule.LookAhead
							for LookupRecord in ChainSubClassRule.SubstLookupRecord:
								# print "Seqindex: ",LookupRecord.SequenceIndex,' LookupIndex: ',LookupRecord.LookupListIndex
								lookuplist.add(LookupRecord.LookupListIndex)
		return lookuplist

# name2uni = {type:{namestring:[namestring]}}
def read_name2uni(lookupidList):
	name2uni = {}
	for i in lookupidList:
		lookup = lookuplists.Lookup[i]
		if lookup.LookupType in [1,2,3,4]:#Basic sub type
			if lookup.LookupType == 1: 
				if 1 not in name2uni.keys():
					name2uni[1] = {}
				for i in range(lookup.SubTableCount):
					#print 'SubTable ',i,', Format = ',lookup.SubTable[i].Format
					#print lookup.SubTable[i].mapping
					for k,v in lookup.SubTable[i].mapping.items():
						if v not in name2uni[1].keys():
							name2uni[1][v] = [k]
						else:
							if k not in name2uni[1][v]:
								name2uni[1][v].append(k)				
			if lookup.LookupType == 2:
				if 2 not in name2uni.keys():
					name2uni[2] = {}
				for i in range(lookup.SubTableCount):
					#print 'SubTable ',i,', Format = ',lookup.SubTable[i].Format
					#print lookup.SubTable[i].mapping
					for k,v in lookup.SubTable[i].mapping.items():
						v_srt = ''
						for name in v:
							v_srt += name + ' '
						v_srt = v_srt[:-1]
						if v_srt not in name2uni[2].keys():
							name2uni[2][v_srt] = [k]
						else:
							if k not in name2uni[1][v_srt]:
								name2uni[1][v_srt].append(k)							
			if lookup.LookupType == 3:
				pass
			if lookup.LookupType == 4:
				if 4 not in name2uni.keys():
					name2uni[4] = {}
				for i in range(lookup.SubTableCount):
					#print 'SubTable ',i,', Format = ',lookup.SubTable[i].Format
					for key,ligatures in lookup.SubTable[i].ligatures.items():
						#print 'keys Glyph ',key
						for lig in ligatures:
							#print "components = ",lig.Component,' LigGlyph = ',lig.LigGlyph
							k_srt = key + ' '
							for c in lig.Component:
								k_srt += c + ' '
							k_srt = k_srt[:-1]
							if lig.LigGlyph not in name2uni[4].keys():
								name2uni[4][lig.LigGlyph] = [k_srt]
							else:
								if k_srt not in name2uni[4][lig.LigGlyph]:
									name2uni[4][lig.LigGlyph].append(k_srt)
	
	return name2uni					

# Check the uni_List wether a syllable 
# Def state: 0-no char before, 1-C befor, 2-V before, 3-M before, 4-D before, 5-H before, 6, N before
def check_syllable(str1):
	state = 0 
	char_list = str1.split(' ')
	count = len(char_list)
	current_i = 0
	for i in range(count):
		current_i = i
		char = char_list[i]
		if char in Consonants and state in [0,5]:
			state = 1
			continue
		elif char in Vowels and state in [0]:#????
			state = 2
			continue
		elif char in Matras and state in [1,5,6]:
			state = 3
			continue
		elif char in Dodifiers and state in [1,2,3,6]:
			state = 4
			break
		elif char in Halant and state in [1,6]:
			state = 5
			continue
		elif char in Nukta and state in [1]:
			state = 6
			continue
		break
	if current_i == count - 1:
		return True
	else:
		return False
		
#import GSUB info
font = ttx.TTFont("NotoSansDevanagari-Regular.ttf")
gsub_table = font["GSUB"].table
lookuplists = gsub_table.LookupList
scriptList = gsub_table.ScriptList
featureList = gsub_table.FeatureList

lookuplst = set()

syllable_list = []

for i in range(scriptList.ScriptCount):
	script = scriptList.ScriptRecord[i].Script
	langsyslist = [script.DefaultLangSys]
	for LangSysRecord in script.LangSysRecord:
		langsyslist.append(LangSysRecord.LangSys)
		
	
	for langsys in langsyslist:
		lookupidx = []
		lookupidx = GetLookupIdx(langsys)
		
		for j in [67]:#lookupidx:
			#print "Lookup Index = ", j
			
			lookuplst.add(j)
			lookup = lookuplists.Lookup[j]
			if lookup.LookupType in [5,6]:
				lookuplst = lookuplst | ReadLookup(lookup)
		print lookuplst
		input1 = raw_input("input")
		
		# Read lookup, get name2uni dict
		lookupidx = list(lookuplst)
		name2uni = read_name2uni(lookupidx)
		for k,v in name2uni.items():
			if k == 2:
				for k1 in v.keys():
					if 'glyph00535' in k1:
						print "Type", k, k1,v[k1]
						
			else:
				if 'glyph00535' in v.keys():
					print "Type", k, 'glyph00535', v['glyph00535']
					
		# print name2uni[2]['glyph00534']
		input1 = raw_input("input")
		syllable = []
		for j in lookupidx:
			# print "Lookup Index = ", j
			lookup = lookuplists.Lookup[j]
		
		# print name2uni 
		# for k,v in name2uni.items():
			# for k1,v1 in v.items():
				# print "key: ", k1
				# print "value: ", v1
			# print "type: ",k
			# input1 = raw_input("input")
		
'''
for i in range(lookuplists.LookupCount):
	lookup = lookuplists[i]
'''
