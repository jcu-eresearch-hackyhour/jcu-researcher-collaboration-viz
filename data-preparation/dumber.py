

import csv
import pprint

pp = pprint.PrettyPrinter(indent=4)


# -------------------------------------------------------------------
def researcher_id(firstname, lastname="", id=""):
	"""turn a researcher's names and id into a single string"""
	return str(lastname)
	return "::".join([str(firstname), str(lastname), str(id)])
# -------------------------------------------------------------------
def researcher_record(firstname, lastname, login):
	return {
		'id': researcher_id(firstname, lastname, login),
		'name': firstname + " " + lastname,
		'abbrv': firstname[:1] + '. ' + lastname,
		'color': '#ff9900', # go wild here steve
		'collabs': {}
	}
# -------------------------------------------------------------------
# start a list of researchers
researchers = {}

# read in each line of the pubs list
with open('input/collabs.csv', 'r') as csvfile:

	pubs = csv.DictReader(csvfile)

	counter = 0

	for pub in pubs:

		counter += 1
		if counter > 300:
			break

		# identify researcher at each end
		res1 = researcher_record(pub['Given Name 1'], pub['Family Name 1'], pub['Login 1'])
		res2 = researcher_record(pub['Given Name 2'], pub['Family Name 2'], pub['Login 2'])
		collab_id = pub['Pub ID']

		# pp.pprint(pub)

		# make sure researcher is in researcher list
		if res1['id'] not in researchers:
			researchers[res1['id']] = res1

		if res2['id'] not in researchers:
			researchers[res2['id']] = res2

		# add this line's collab to each researcher's collab list
		researchers[res1['id']]['collabs'][collab_id + "::" + res2['id']] = { 'id': collab_id, 'other': res2['id'] }
		researchers[res2['id']]['collabs'][collab_id + "::" + res1['id']] = { 'id': collab_id, 'other': res1['id'] }


# add the 'co-authored' key to everyone
for res_id in researchers:
	researchers[res_id]['coauthored'] = len(researchers[res_id]['collabs'])


# pp.pprint(researchers)


# produce final researcher list
with open('../collab/graphs/James Cook University-graph-nodes.csv', 'w') as outnodes:
	writer = csv.DictWriter(outnodes, fieldnames=['name', 'abbrv', 'color', 'coauthored'], extrasaction='ignore')
	writer.writeheader()
	writer.writerows(researchers.values())

# produce grid of collabs (using same order of researchers as list)

# get researcher list we'll use for guaranteed ordering
reslist = list(researchers.keys())

grid = []
# grid.append(reslist[:])

for row_res in reslist:
	row = []
	# row.append(row_res.rjust(30))
	row_res_collabs = researchers[row_res]['collabs']

	for col_res in reslist:
		# count the collabs row_res has had with col_res
		matching_collabs = { cid: collab for cid, collab in row_res_collabs.items() if collab['other'] == col_res }
		row.append(len(matching_collabs))

	grid.append(row)


with open('../collab/graphs/James Cook University-graph-matrix.json', 'w') as outjson:
	outjson.write(str(grid))

