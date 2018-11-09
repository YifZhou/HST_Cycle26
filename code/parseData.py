"""
parse apt file and save them to csv files
use untangle to parse the xml files
"""
import untangle
import glob
import pandas as pd

# interesting data
proposalID = []
PI_last = []
PI_first = []
PI_title = []
PI_country = []
PI_institution = []
n_orbit = []
n_people = []
size = []
category = []
sci_category = []
title = []
cycle_no = []

fnList = glob.glob('../DATA/*.apt')
for fn in fnList:
    aptFile = untangle.parse(fn)
    try:
        category_i = aptFile.HSTProposal.ProposalInformation.get_attribute(
            'Category')
    except AttributeError:
        category_i = 'None'
    if category_i == 'AR':
        continue
    cycle_i = int(
        aptFile.HSTProposal.ProposalInformation.get_attribute('Cycle'))
    title_i = aptFile.HSTProposal.ProposalInformation.Title.cdata
    PI = aptFile.HSTProposal.ProposalInformation.PrincipalInvestigator
    PI_last_i = PI.get_attribute('LastName')
    PI_first_i = PI.get_attribute('FirstName')
    PI_title_i = PI.get_attribute('Honorific')
    PI_insitution_i = PI.get_attribute('Institution')
    PI_country_i = PI.get_attribute('Country')
    try:
        coI = aptFile.HSTProposal.ProposalInformation.CoInvestigator
        n_CoI_i = len(coI)
    except AttributeError:
        n_CoI_i = 0
    n_people_i = n_CoI_i + 1
    try:
        n_orbit_i = int(aptFile.HSTProposal.ProposalInformation.Orbits.get_attribute(
            'ThisCycle2GyroPrimary'))
    except AttributeError:
        print(fn)
    size_i = aptFile.HSTProposal.ProposalInformation.Phase1ProposalInformation.get_attribute(
        'ProposalSize')
    try:
        sci_category_i = aptFile.HSTProposal.ProposalInformation.Phase1ProposalInformation.ScientificCategory.cdata
    except AttributeError:
        sci_category_i = 'None'
    proposalID_i = int(aptFile.HSTProposal.get_attribute('Phase2ID'))

    proposalID.append(proposalID_i)
    PI_last.append(PI_last_i)
    PI_first.append(PI_first_i)
    PI_title.append(PI_title_i)
    PI_country.append(PI_country_i)
    PI_institution.append(PI_insitution_i)
    n_orbit.append(n_orbit_i)
    n_people.append(n_people_i)
    size.append(size_i)
    category.append(category_i)
    sci_category.append(sci_category_i)
    title.append(title_i)
    cycle_no.append(cycle_i)

df = pd.DataFrame()
df['PID'] = proposalID
df['Cycle'] = cycle_no
df['Category'] = category
df['PI Last'] = PI_last
df['PI First'] = PI_first
df['PI Title'] = PI_title
df['PI Country'] = PI_country
df['PI Institution'] = PI_institution
df['Orbits'] = n_orbit
df['N People'] = n_people
df['Size'] = size
df['Science Category'] = sci_category
df['Title'] = title

df.sort_values('Cycle')
df.to_csv('Cycle26_Summary.csv', index=False)
