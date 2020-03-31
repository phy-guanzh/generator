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
#        ('53', 'cll'),
        ('54', 'cll1'),
        ('55', 'cqq1'),
        ('56', 'cqq11'),
        ('57', 'cqq3'),
        ('58', 'cqq31'),
    ]

#    os.system("source source_condor.sh")

    with open('gridpack_submitcondor.sh','w') as outfile:
        for ipar,param in enumerate(params):
      # 1D cards
      # int
                process='VBS_SSWW_'+ params[ipar][1]+'_LL'
                outfile.write('nohup ./submit_condor_gridpack_generation.sh ' +process+ ' cards/Allcw1/'+process +' >' +process+'.log 2>&1 & \n' )

                process='VBS_SSWW_'+ params[ipar][1]+'_TL'
                outfile.write('nohup ./submit_condor_gridpack_generation.sh ' +process+ ' cards/Allcw1/'+process +' >' +process+'.log 2>&1 & \n' )

                process='VBS_SSWW_'+ params[ipar][1]+'_TT'
                outfile.write('nohup ./submit_condor_gridpack_generation.sh ' +process+ ' cards/Allcw1/'+process +' >' +process+'.log 2>&1 & \n' )
~                                             
