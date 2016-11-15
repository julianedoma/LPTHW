states = {
    'Bayern' : 'BR',
    'Thüringen' : 'TH',
    'Hessen' : 'HE',
    'Saarland' : 'SA',
    'Rheinland-Pfalz' : 'RLP',
    'Nordrhein-Westfalen' : 'NRW',
    'Sachsen' : 'S',
    'Sachsen-Anhalt' : 'SA',
    'Mecklenburg-Vorpommern' : 'MKVP',
    'Schleswigholstein' : 'SGH',
    'Niedersachsen' : 'NSN'
}

cities = {
    'BR' : 'München',
    'TH': 'Erfurt',
    'HE': 'Wiesbaden',
    'SA' : 'Saarbrücken',
    'RLP': 'Mainz',
    'NRW': 'Düsseldorf',
    'S' : 'Dresden',
    'SA' : 'Magdeburg',
    'MKVP': 'Schwerin',
    'SGH': 'Kiel',
    'NSN' : 'Hannover'
}

print "Die Landeshauptstadt von Sachsen ist: ", cities[states['Sachsen']]
