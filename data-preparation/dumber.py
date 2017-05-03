

import csv
import pprint

pp = pprint.PrettyPrinter(indent=4)


def researcher_id(firstname, lastname="", id=""):
	"""turn a researcher's names and id into a single string"""
	return "::".join([str(firstname), str(lastname), str(id)])


# start a list of researchers
researchers = {}


# read in each line of the pubs list
with open('input/testcollabs.csv', 'r') as csvfile:
	pubs = csv.DictReader(csvfile)

	for pub in pubs:

		# identify researcher at each end
		res1_id = researcher_id(pub['Given Name 1'], pub['Family Name 1'], pub['Login 1'])
		res2_id = researcher_id(pub['Given Name 2'], pub['Family Name 2'], pub['Login 2'])
		collab_id = pub['Pub ID']

		# pp.pprint(pub)

		# make sure researcher is in researcher list
		if res1_id not in researchers:
			researchers[res1_id] = { 
				'name': res1_id, 
				'abbrev': pub['Family Name 1'], 
				'color': '#ff9900', 
				'collabs': {} 
			}

		if res2_id not in researchers:
			researchers[res2_id] = { 
				'name': res2_id, 
				'abbrev': pub['Family Name 2'], 
				'color': '#ff9900', 
				'collabs': {} 
			}

		# add this line's collab to each researcher's collab list
		researchers[res1_id]['collabs'][collab_id] = { 'id': collab_id, 'other': res2_id }
		researchers[res2_id]['collabs'][collab_id] = { 'id': collab_id, 'other': res1_id }


# add the 'co-authored' key to everyone
for res_id in researchers:
	researchers[res_id]['coauthored'] = len(researchers[res_id]['collabs'])


pp.pprint(researchers)


# produce final researcher list
with open('dumbnodes.csv', 'w') as outnodes:
	writer = csv.DictWriter(outnodes, fieldnames=['name', 'abbrev', 'color', 'coauthored'], extrasaction='ignore')
	writer.writeheader()
	writer.writerows(researchers.values())

# produce grid of collabs (using same order of researchers as list)
