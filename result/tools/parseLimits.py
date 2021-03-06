#!/cvmfs/cms.cern.ch/slc6_amd64_gcc491/cms/cmssw/CMSSW_7_4_7/external/slc6_amd64_gcc491/bin/python


# Example input
# v8.04_tttt_July26/card_tttt_12.9ifb-all.txt
#lim_tttt = """
# -- Asymptotic --
# Observed Limit: r < 6.2128
# Expected  2.5%: r < 2.5093
# Expected 16.0%: r < 3.4626
# Expected 50.0%: r < 5.0781
# Expected 84.0%: r < 7.6083
# Expected 97.5%: r < 10.9437
#"""
# v6.02-tttt/card_tttt_2.3ifb-all.txt
#lim_tttt = """
# -- Asymptotic -- 
# Observed Limit: r < 13.0276
# Expected  2.5%: r < 5.0485
# Expected 16.0%: r < 7.2446
# Expected 50.0%: r < 11.0938
# Expected 84.0%: r < 17.3288
# Expected 97.5%: r < 25.9161
#"""

import argparse
import json
import sys

xsec_tttt = 0.009201 # pb

def get_lim(lim_str, xsec, name, format='txt', json_filename=None, ch=''):
    """
	Convert combine tool output to different format.
	lim_str: raw combine output string with Observed or Expected strings only.
	xsec: constant SM cross section prediction.
	name: Process label (e.g. 'TTTT').
	format: target format [txt,tex,json and combinations thereof].
	out_filename: json output file name
    """
    d = {}
    for line in lim_str.splitlines():
        if "Observed" in line: d["obs"] = float(line.split("<")[-1])
        elif "Expected" in line: d["exp_"+line.split("%")[0].replace("Expected","").strip()] = float(line.split("<")[-1])
        elif "Significance" in line: d["signif"] = float(line.split(":")[-1])
        elif "Best" in line: 
		d["bestfit"] = float(line.split(":")[-1].split()[0])
		d["bestfit_16.0"] = float(line.split(":")[-1].split()[1].split("/")[0])
		d["bestfit_64.0"] = float(line.split(":")[-1].split()[1].split("/")[1])

    unit = "pb"
    if d["exp_50.0"]*xsec < 0.9:
        xsec *= 1000.0
        unit = "fb"
    obs = -1.
    if 'obs' in d: obs = d["obs"]*xsec
    exp = d["exp_50.0"]*xsec
    exp_sm1 = d["exp_16.0"]*xsec
    exp_sp1 = d["exp_84.0"]*xsec

    json_array = json.dumps(d)

    if 'txt' in format:
	print "Limits for %s" % name
    	if obs > 0.: print "  Obs: %.2f %s" % (obs, unit)
    	print "%s %.2f + %.2f - %.2f %s" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], "xSM")
    	print "%s %.2f + %.2f - %.2f %s" % (ch, exp, exp_sp1-exp, exp-exp_sm1, unit)
    if 'tex' in format:
	if ch == 'Mu': ch = '\mu'
	if ch == 'El': ch = 'e'
        print "Limits for %s" % name
        if obs > 0.: print "  Obs: %.2f \%s" % (obs, unit)
        print "$%s$ & $%.1f^{+%.1f}_{-%.1f}$ & $%.0f^{+%.0f}_{-%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], exp, exp_sp1-exp, exp-exp_sm1, unit)
        #print "$%s$ & $%.5f^{+%.5f}_{-%.5f}$ & $%.0f^{+%.0f}_{-%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["exp_50.0"], d["exp_84.0"]-d["exp_50.0"], d["exp_50.0"]-d["exp_16.0"], exp, exp_sp1-exp, exp-exp_sm1, unit)
	if 'signif' in d and 'bestfit' in d:
		print "$%s$ & $%.2f$ & $%.0f^{+%.1f}_{%.1f}$ & $%.1f^{+%.0f}_{%.0f}$ \%s \T\B\\\\ \n\\hline" % (ch, d["signif"], d['bestfit'], d['bestfit_64.0'], d['bestfit_16.0'], d['bestfit']*xsec, d['bestfit_64.0']*xsec, d['bestfit_16.0']*xsec, unit)
    if 'json' in format:
	if json_filename is not None:
		with open(json_filename, 'w') as outfile:
    			json.dump(d, outfile, sort_keys=True, indent=4)

def parse_args():
	parser = argparse.ArgumentParser(description='Combine limit output parser')
	parser.add_argument('-i','--input', help='Input file name',required=True)
	parser.add_argument('-f','--format', help='Output format', required=False)
	parser.add_argument('-j','--jsonoutput',help='Output json file name', required=False)
	args = parser.parse_args()
	return args

def main():
	args = parse_args()
	
	lim_tttt = ""

	with open( args.input ) as f:
		for line in f:
			if line.startswith('Expected') or line.startswith('Observed') or line.startswith('Best') or line.startswith('Significance'):
				print(line.strip())
				lim_tttt += line

	if not any(fmt in args.format for fmt in ['txt','tex','json']):
		error_msg = 'Format ' + args.format + ' not recognised! Terminating...'
		sys.exit(error_msg)

	ch = ''
	if 'card_mu' in args.input: ch = "Mu"
	if 'card_el' in args.input: ch = "El"
	if 'datacard_elmu' in args.input: ch = "SL combined"
	get_lim(lim_tttt, xsec_tttt, "TTTT", args.format, args.jsonoutput, ch)


if __name__ == '__main__':
	main()
