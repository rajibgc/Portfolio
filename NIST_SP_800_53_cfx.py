#==========================================================================================================================
'''
Author: Rajib GanChaudhuri, 16-Oct-2023
This Python program extracts the "families" of controls proposed by the publication NIST SP 800-53.

To run this program, download the source file "NIST_SP-800-53_rev5_catalog.xml" from location below, and save locally 
  https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/xml/NIST_SP-800-53_rev5_catalog.xml
'''
#==========================================================================================================================
try:
    fin = open('NIST_SP-800-53_rev5_catalog.xml', 'r')
    fout = open('ControlFamilies.html', 'w')
    fout.write('<html><head><title>NIST 800-53 - control families</title><style>h4{background-color: #eeee00;' + 
               ' font-size: 13;}</style></head><body><h3>NIST 800-53 - control families</h3>')
    FamilyCount = 0
    line = fin.readline()
    while line:        
        line = line.strip()
        # Process the line
        if line.find('<group class="family"') > -1:
            FamilyCount = FamilyCount + 1
            familyAcronym = line.replace('<group class="family" id="', '').replace('">', '').upper() + " - "
            line = fin.readline()
            line = line.strip().replace('<title>', '')
            line = '<title> Family ' + str(FamilyCount) + ' : ' + familyAcronym + line
            line = line.replace('title>', 'h4>')
            fout.write(line)
        '''
        if line.find('<control class="SP800-53"') > -1:
            controlId = line.replace('<control class="SP800-53" id="', '').replace('">', '').upper()
            line = fin.readline()
            line = line.strip().replace('<title>', '')
            line = '<title> Control ' + controlId + ' - ' + line.strip() 
            line = line.replace('title>', 'p>')
            fout.write(line)
        '''
        line = fin.readline()
    fout.write('</body></html>')
finally:
    fin.close()
    fout.close()
#==========================================================================================================================
