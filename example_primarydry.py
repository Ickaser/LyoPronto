import argparse
import os
import time
import csv


# Depends on LyoPronto.calc_knownRp. Import that somehow. 
# If executed inside LyoPronto folder, this will fail.
import LyoPronto

# ------------- Handle a folder input from command line

parser = argparse.ArgumentParser()
parser.add_argument("out_folder", help="local folder name for storing output ('./out_folder' assumed)")
out_loc = os.getcwd() + "/" + parser.parse_args().out_folder + "/"
os.makedirs(out_loc, exist_ok=True)
print(f"Saving output files to {out_loc} .")

#-------------- LyoPronto setup

sim = dict([('tool','Primary Drying Calculator'),('Kv_known','Y'),('Rp_known','Y'),('Variable_Pch','N'),('Variable_Tsh','N')])

vial = dict([('Av',3.80),('Ap',3.14),('Vfill',2.0)]) # 6R vial
# Rp known
product = dict([('cSolid',0.05),('R0',1.4),('A1',16.0),('A2',0.0)])
# Kv known
ht = dict([('KC',2.75e-4),('KP',8.93e-4),('KD',0.46)])
# Fixed Pchamber
Pchamber = dict([('setpt',[0.15]),('dt_setpt',[1800.0]),('ramp_rate',0.5)])
# Fixed Tshelf
Tshelf = dict([('init',-35.0),('setpt',[20.0]),('dt_setpt',[1800.0]),('ramp_rate',1.0)])

dt = 0.001    # hr

# -------------- Call input logger, which looks at globals...? TODO fix

LyoPronto.io_funcs.log_inputs()

# -------------- LyoPronto excution

output_saved = LyoPronto.calc_knownRp.dry(vial,product,ht,Pchamber,Tshelf,dt)

# --------------- Save output
current_time = time.strftime("%y%m%d_%H%M",time.localtime())

csvfile = open(out_loc + 'output_saved_'+current_time+'.csv', 'w')
try:
    writer = csv.writer(csvfile)
    writer.writerow(['Time [hr]','Sublimation Temperature [C]','Vial Bottom Temperature [C]', 'Shelf Temperature [C]','Chamber Pressure [mTorr]','Sublimation Flux [kg/hr/m^2]','Percent Dried'])
    for i in range(0,len(output_saved)):
        writer.writerow(output_saved[i])
finally:
    csvfile.close()