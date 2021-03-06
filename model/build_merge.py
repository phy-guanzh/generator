import os

if __name__ == "__main__":
    params = [('21', 'cW'),
        ('24', 'cHbox'),
        ('25', 'cHDD'),
        ('28', 'cHW'),
        ('30', 'cHB'),
        #('32', 'cHWB'),
        ('45', 'cHl1'),
        ('46', 'cHl3'),
        ('47', 'cHe'),
        ('48', 'cHq1'),
        ('49', 'cHq3'),
        #('50', 'cHu'),
        #('51', 'cHd'),
        #('53', 'cll'),
        ('54', 'cll1'),
        ('55', 'cqq1'),
        ('56', 'cqq11'),
        ('57', 'cqq3'),
        ('58', 'cqq31'),
    ]

    # loop over parameters to be restricted
    for ipar,param in enumerate(params):
        # 1D cards
        # int
        # ./merge.pl /home/pku/xiaoj/polar/lhe/cHW_bsm_*.lhe cHW_bsm.lhe.gz cHW_bsm.txt
        process=params[ipar][1]+'_int'
        try:
            os.system('./merge.pl /home/pku/xiaoj/polar/eft_lhe/'+ process+'_*.lhe '+process+'.lhe.gz '+process+'.txt')
        except:
            print('>>>>>>>>>>>>>>>>>>>> Please check: '+process)
        else:
            pass
        # bsm
        process=params[ipar][1]+'_bsm'
        try:
            os.system('./merge.pl /home/pku/xiaoj/polar/eft_lhe/'+ process+'_*.lhe '+process+'.lhe.gz '+process+'.txt')
        except:
            print('>>>>>>>>>>>>>>>>>>>> Please check: '+process)
        else:
            pass
        
        # 2D cards
        for jpar in range(ipar+1,len(params)):
            process=params[ipar][1] + '_' + params[jpar][1]
            try:
                os.system('./merge.pl /home/pku/xiaoj/polar/eft_lhe/'+ process+'_*.lhe '+process+'.lhe.gz '+process+'.txt')
            except:
                print('>>>>>>>>>>>>>>>>>>>> Please check: '+process)
            else:
                pass
