

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
		res1 = researcher_id(pub['Given Name 1'], pub['Family Name 1'], pub['Login 1'])
		res2 = researcher_id(pub['Given Name 2'], pub['Family Name 2'], pub['Login 2'])
		collab_id = pub['Pub ID']

		# pp.pprint(pub)

		# make sure researcher is in researcher list
		if res1 not in researchers:
			researchers[res1] = { 'id': res1, 'collabs': {} }

		if res2 not in researchers:
			researchers[res2] = { 'id': res2, 'collabs': {} }

		# add this line's collab to each researcher's collab list
		researchers[res1]['collabs'][collab_id] = { 'id': collab_id, 'other': res2 }
		researchers[res2]['collabs'][collab_id] = { 'id': collab_id, 'other': res1 }




pp.pprint(researchers)


# produce final researcher list
# produce grid of collabs (using same order of researchers as list)
