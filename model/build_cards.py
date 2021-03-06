import os

if __name__ == "__main__":
    params = [('21', 'cW'),
        ('24', 'cHbox'),
        ('25', 'cHDD'),
        ('28', 'cHW'),
        ('30', 'cHB'),
        ('32', 'cHWB'),
        ('45', 'cHl1'),
        ('46', 'cHl3'),
        ('47', 'cHe'),
        ('48', 'cHq1'),
        ('49', 'cHq3'),
        ('50', 'cHu'),
        ('51', 'cHd'),
        ('53', 'cll'),
        ('54', 'cll1'),
        ('55', 'cqq1'),
        ('56', 'cqq11'),
        ('57', 'cqq3'),
        ('58', 'cqq31'),
    ]

    extramodels_content=""
    extramodels_content+="# customized model for EWdim6 EFT in 5f\n"
    extramodels_content+="SMEFTsim_A_U35_MwScheme_UFO_v3.tar.gz"
    proc_card_0=""
    proc_card_0+="set group_subprocesses Auto\n"
    proc_card_0+="set ignore_six_quark_processes False\n"
    proc_card_0+="set loop_optimized_output True\n"
    proc_card_0+="set complex_mass_scheme False\n"

    proc_card_1=""
    proc_card_1+="define p = g u c d s b u~ c~ d~ s~ \n"
    proc_card_1+="define j = p\n"
    proc_card_1+="define l+ = e+ mu+ ta+\n"
    proc_card_1+="define l- = e- mu- ta-\n"
    proc_card_1+="define vl = ve vm vt\n"
    proc_card_1+="define vl~ = ve~ vm~ vt~\n"
    proc_card_1+="\n"
    # loop over parameters to be restricted
    for ipar,param in enumerate(params):
        # 1D cards
        # int
        process='VBS_SSWW_'+ params[ipar][1]+'_LL'
        os.makedirs(process)
        with open(process+'/'+process+'_extramodels.dat','w') as outfile:
            outfile.write(extramodels_content)
        with open(process+'/'+process+'_proc_card.dat','w') as outfile:
            outfile.write(proc_card_0)
            outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-'+params[ipar][1]+ '_massless\n')
            outfile.write(proc_card_1)
            outfile.write("generate p p > w+{0} w+{0} j j QCD=0 SMHLOOP=0 NP=1  , w+ > l+ vl  @ 1\n")
            outfile.write("add process p p > w-{0} w-{0} j j QCD=0 SMHLOOP=0 NP=1  , w- > l- vl~ @ 2\n")
            outfile.write("output "+process)
        os.system("curl http://stash.osgconnect.net/+jiexiao/run_card.dat -o "+process+'/'+process+'_run_card.dat')
        os.system("cp restrictcard"+'/'+'restrict_'+ params[ipar][1] + '_massless.dat'+' '+'./'+ process+ '/'+ process +'_restrict'+'_massless.dat')

        # bsm
        process='VBS_SSWW_'+ params[ipar][1]+'_TL'
        os.makedirs(process)
        with open(process+'/'+process+'_extramodels.dat','w') as outfile:
            outfile.write(extramodels_content)
        with open(process+'/'+process+'_proc_card.dat','w') as outfile:
            outfile.write(proc_card_0)
            outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-'+params[ipar][1]+ '_massless\n')
            outfile.write(proc_card_1)
            outfile.write("generate p p > w+{T} w+{0} j j QCD=0 SMHLOOP=0 NP=1  , w+ > l+ vl @ 1\n")
            outfile.write("add process p p > w-{T} w-{0}  j j QCD=0 SMHLOOP=0 NP=1 , w- > l- vl~  @ 2\n")
            outfile.write("output "+process)
        os.system("curl http://stash.osgconnect.net/+jiexiao/run_card.dat -o "+process+'/'+process+'_run_card.dat')
        os.system("cp restrictcard"+'/'+'restrict_'+ params[ipar][1] + '_massless.dat'+' '+'./'+ process+ '/'+ process +'_restrict'+'_massless.dat')

        #TT
        process='VBS_SSWW_'+ params[ipar][1]+'_TT'
        os.makedirs(process)
        with open(process+'/'+process+'_extramodels.dat','w') as outfile:
            outfile.write(extramodels_content)
        with open(process+'/'+process+'_proc_card.dat','w') as outfile:
            outfile.write(proc_card_0)
            outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-'+params[ipar][1]+ '_massless\n')
            outfile.write(proc_card_1)
            outfile.write("generate p p > w+{T} w+{T} j j QCD=0 SMHLOOP=0 NP=1 , w+ > l+ vl  @ 1\n")
            outfile.write(" add process p p > w-{T} w-{T}  j j QCD=0 SMHLOOP=0 NP=1 , w- > l- vl~@ 2\n")
            outfile.write("output "+process)
        os.system("curl http://stash.osgconnect.net/+jiexiao/run_card.dat -o "+process+'/'+process+'_run_card.dat')
        os.system("cp restrictcard"+'/'+'restrict_'+ params[ipar][1] + '_massless.dat'+' '+'./'+ process+ '/'+ process +'_restrict'+'_massless.dat')

        # 2D cards
'''
        for jpar in range(ipar+1,len(params)):
            process='VBS_SSWW_'+ params[ipar][1] + '_' + params[jpar][1]
            os.makedirs(process)
            with open(process+'/'+process+'_extramodels.dat','w') as outfile:
                outfile.write(extramodels_content)
            with open(process+'/'+process+'_proc_card.dat','w') as outfile:
                outfile.write(proc_card_0)
                outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-'+params[ipar][1] + '_' + params[jpar][1]+ '_massless\n')
                outfile.write(proc_card_1)
                outfile.write("generate p p > l+ l+ vl vl j j QCD=0 SMHLOOP=0 NP=1 NP"+params[ipar][1]+"^2==1 NP"+params[jpar][1]+"^2==1 @ 1\n")
                outfile.write("add process p p > l- l- vl~ vl~ j j QCD=0 SMHLOOP=0 NP=1 NP"+params[ipar][1]+"^2==1 NP"+params[jpar][1]+"^2==1 @ 2\n")
                outfile.write("output "+process)
            os.system("curl -s http://stash.osgconnect.net/+jiexiao/run_card.dat -o "+process+'/'+process+'_run_card.dat')
'''
