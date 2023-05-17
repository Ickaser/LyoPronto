def log_inputs():

    csvfile = open(out_loc + 'input_saved_'+current_time+'.csv', 'w')

    try:
        writer = csv.writer(csvfile)
        writer.writerow(['Tool:',sim['tool']])
        writer.writerow(['Kv known?:',sim['Kv_known']])
        writer.writerow(['Rp known?:',sim['Rp_known']])
        writer.writerow(['Variable Pch?:',sim['Variable_Pch']])
        writer.writerow(['Variable Tsh?:',sim['Variable_Tsh']])
        writer.writerow([''])
        
        writer.writerow(['Vial area [cm^2]',vial['Av']])
        writer.writerow(['Product area [cm^2]',vial['Ap']])
        writer.writerow(['Vial fill volume [mL]',vial['Vfill']])
        writer.writerow([''])
        
        writer.writerow(['Fractional solute concentration:',product['cSolid']])
        if sim['tool'] == 'Freezing Calculator':
            writer.writerow(['Intial product temperature [C]:',product['Tpr0']])
            writer.writerow(['Freezing temperature [C]:',product['Tf']])
            writer.writerow(['Nucleation temperature [C]:',product['Tn']])
        elif not(sim['tool'] == 'Primary Drying Calculator' and sim['Rp_known'] == 'N'):
            writer.writerow(['R0 [cm^2-hr-Torr/g]:',product['R0']])
            writer.writerow(['A1 [cm-hr-Torr/g]:',product['A1']])
            writer.writerow(['A2 [1/cm]:',product['A2']])
        if not(sim['tool'] == 'Freezing Calculator' and sim['tool'] == 'Primary Drying Calculator'):
            writer.writerow(['Critical product temperature [C]:', product['T_pr_crit']])
        writer.writerow([''])
        
        if sim['tool'] == 'Freezing Calculator':
            writer.writerow(['h_freezing [W/m^2/K]:',h_freezing])
        elif sim['Kv_known'] == 'Y':
            writer.writerow(['KC [cal/s/K/cm^2]:',ht['KC']])
            writer.writerow(['KP [cal/s/K/cm^2/Torr]:',ht['KP']])
            writer.writerow(['KD [1/Torr]:',ht['KD']])
        elif sim['Kv_known'] == 'N':
            writer.writerow(['Kv range [cal/s/K/cm^2]:',Kv_range[:]])
            writer.writerow(['Experimental drying time [hr]:',t_dry_exp])
        writer.writerow([''])
        
        if sim['tool'] == 'Freezing Calculator':
            0
        elif sim['tool'] == 'Design-Space-Generator':
            writer.writerow(['Chamber pressure set points [Torr]:',Pchamber['setpt'][:]])
        elif not(sim['tool'] == 'Optimizer' and sim['Variable_Pch'] == 'Y'):
            for i in range(len(Pchamber['setpt'])):
                writer.writerow(['Chamber pressure setpoint [Torr]:',Pchamber['setpt'][i],'Duration [min]:',Pchamber['dt_setpt'][i]])
            writer.writerow(['Chamber pressure ramping rate [Torr/min]:',Pchamber['ramp_rate']])
        else:
            writer.writerow(['Minimum chamber pressure [Torr]:',Pchamber['min']])
            writer.writerow(['Maximum chamber pressure [Torr]:',Pchamber['max']])
        writer.writerow([''])
        
        if sim['tool'] == 'Design-Space-Generator':
            writer.writerow(['Intial shelf temperature [C]:',Tshelf['init']])
            writer.writerow(['Shelf temperature set points [C]:',Tshelf['setpt'][:]])
            writer.writerow(['Shelf temperature ramping rate [C/min]:',Tshelf['ramp_rate']])
        elif not(sim['tool'] == 'Optimizer' and sim['Variable_Tsh'] == 'Y'):
            for i in range(len(Tshelf['setpt'])):
                writer.writerow(['Shelf temperature setpoint [C]:',Tshelf['setpt'][i],'Duration [min]:',Tshelf['dt_setpt'][i]])
            writer.writerow(['Shelf temperature ramping rate [C/min]:',Tshelf['ramp_rate']])
        else:
            writer.writerow(['Minimum shelf temperature [C]:',Tshelf['min']])
            writer.writerow(['Maximum shelf temperature [C]:',Tshelf['max']])
        writer.writerow([''])
        
        writer.writerow(['Time step [hr]:',dt])
        writer.writerow([''])
        
        if not (sim['tool'] == 'Freezing Calculator' and sim['tool'] == 'Primary Drying Calculator'):
            writer.writerow(['Equipment capability parameters:','a [kg/hr]:',eq_cap['a'],'b [kg/hr/Torr]:',eq_cap['b']])
            writer.writerow(['Number of vials:',nVial])    

    finally:
        csvfile.close()