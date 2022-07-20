import os

exclude_words = [
    'bond_stereo_count', 
    'undefined_atom_stereocenter_count',
    'supersweetdb_id',
    'fema_number',
    'fooddb_id',
    'hba_count',
    'synthetic',
    'isotope_atom_count',
    'bitterdb_id',
    'covalently_bonded_unit_count',
    'molecular_weight',
    'super_sweet',
    'charge',
    'flavornet_id',
    'fenoroli_and_os',
    'exact_mass',
    'pubchem_id',
    'bitter',
    'volume3d',
    'unknown_natural',
    'num_rotatablebonds',
    'smile',
    'inchi',
    'undefined_bond_stereocenter_count',
    'defined_bond_stereocenter_count',
    'xlogp',
    'topological_polor_surfacearea',
    'cas_id',
    'natural',
    'hbd_count',
    'fema_flavor_profile',
    'complexity',
    'heavy_atom_count',
    'defined_atom_stereocenter_count',
    'monoisotopic_mass',
    'atom_stereo_count',
    'naughty']

dir_path = r"C:\Users\sciam\Downloads\cibus"
files = os.listdir(dir_path)
for file in files:
    c = 0
    with open(os.path.join(dir_path,file),'r') as oldfile, open(file, 'w') as nf:
        lines = oldfile.readlines()
        for line in lines:
            if not any(bad_word in line for bad_word in exclude_words):
                formatted = "false"
                if c==0:
                    prev = line
                if c>1:
                    if "}" in line:
                        formatted = prev.replace(",", "")
                if formatted == "false":
                    if c>=1:
                        nf.write(prev)
                else:
                    nf.write(formatted)
                prev = line   
                c+=1
        for l in lines:
            pass
        last_line = l
        nf.write(last_line)
            
