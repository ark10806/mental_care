global strs
strs = []
line = 201
def crop(str):
    str = str[line * 10 : -line * 13]

    return str

def append():
    global strs
    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                         `..`                            :ss/`      .-.                                                 
                                                                                                   ``  `+hddds-                          :omNs`    .yNdo.                                               
                                                                                                -odddhsdNdyshNm+`                         .sMh.     .:MM+                                               
                                                                                            `.-omNdsydNMMdhhydMm/`                        -yy:       oMm/                                               
                                                                                        .-+ydmmNMh+//+hMMhhdmmNNmdy+-`                     `` ```    -/-                                                
                                                                                     ./ydNmdysyMmo////ohh////++osydmNds/`                    .ydh+`                                                     
                                                                                  `-smNmys++//oMmo/////+//////////++shmNdo-                  `-oNN+                                                     
                                                                                `:yNNho+//////oMmo////////////////////+sdNms.                  +Nm/                                                     
                                                                               `omNho/////////+NNy//////////////////////+sdNm/`                :o:                                                      
                                                                              -hNms+///////////syo////////////////////////+yNNo`                                                                        
                                            ````                             -dMd+//////////////////////////////////////////oNNs`                                                                       
                                          .+hddy/`                          .hMd+////////////////////////////////////////////sNN+                                                                       
                                          /dd+omN/                         `sMmo/////////////////////////////////////////////+yMN-                                                                      
                                           `   -:`                         -NMNmyo++//////////////////////////////////////////+dMy                                                                      
                                                                           sMmmNMNmhs//////////////////////////////////////////hMN                                                                      
                                      `-:-`     .:/:.`                     mMh++ydNNd+/////////////////////////////////////////sNM-                                                                     
                                    `omMNNm+`  /mMdNNy.                    NMhsdh++++/////oyhhdhys+////////////////////////////omM/                                                                     
                                    `/s:`/mh`  -+:`-yh.                   `NMhdMNs/////+smNmdhhhdNNd+//////////////////////////omM:                                                                     
                                                                        .smMMh+so/////+hNmo+/////+hNmo/////////////////////////yNM.                                                                     
                                                                        +NMMMd+///////sNNo////////+dMd+///////////////////////+hMm                                                                      
                                                                        /NMhNNs//////+hMh+/////////oMNs///////////////////////omM+                                                                      
                                                                       `sMd`sMh+/////+dMy+//////////dMh+/////////////////////+dMh.                                                                      
                                                                        oNN--dNy/////+hMh+//////////sMmo////////////////////+dMd-                                                                       
                                                                        .sNmyhNMy+///+yMd+//////////+mMy///////////////////odMd:                                                                        
                                                                         `-ohhdNNh+///omNs//////////+yMm+////////////////+smMy.       ``                                                                
                                                                            ```-hNmy+/+hMm+//////////+dMh+/////////////+ydNd/`  `-+ydmmmmho:` ```........```                                            
                                                              `...`             `/hNmyoomMh+//////////omNy+/////////+shmNh+.   .smNdhyssyhNNhyhdmmmmmmmmmddhyo+:...-:/:-.`                              
                                      ``--/+ossyyyyysso+::--ohddmddhs/`           `:ymNmmMNy+//////////smNy+///++oshmNms:`    -hMdo+/////+odMNhssssooossssyyddmNmdmmmmmmmh+.                            
                                 `.:+shmmmmmdddhhhhhdddmNNmNNdysssshmNd:             ./dMMNNy+//////////omNdyhhmmmmdmMd.      +Mmo/////////+mms//////////////+smMdyo+++oydNd:                           
                              `-+ydNmdhyoo++++/+////++++ohNNo+//////+hMd:             `yMdsmNh+//////////ohNMdhyso++omMs     `sMd+//////////+o+//////////////odMh+///////+hMd-                          
                           `.+dNMMMNmhso+///////////////+dMy/////////+MMo             `yMy:+hNms+/////////+os+///////yNN.   `+mMNo///////////////////////////+yy+/////////oMM/                          
                         `:smMNmdhyyhdmNh+//////////////+yh+/////////+MMs`            `yMh ./smNho///////////////////+mMy.`:hNmhho////////////////////////////////////////oMMo`                         
                        .yNMMms++////+ohNdo//////////////////////////sNNmo.            oMN` -/+hmh+//////////////////+dMMmdmNh+//////////////////////////////////////////+dMMNy`                        
                      `+mNNMmo/////////+hmy///////////////////////////+sdNd:           /mM- `://++////////////////////hMNmMms////////////////////////////////////////////yNdsdMh.                       
                     .yNmsyMd+//////////+++/////////////////////////////+yNNo`         .hMy` -///////////////////////+dMNNms/////////////////////////////////////////////+o+/+dMh.                      
                    .hMdo/sNNo////////////////////////////////////////////sNNy/:.`      /NN/`-//////////////////////+sNMMNs///////////////////////////////////////////////////+mMs`                     
                   `dMdo//+hNm+////////////////////////////////////////////sNMMNmdo.     oMm/://///////////////////oyNMMMh+////////////////////////////////////////////////////sNN/                     
                   sMmo////+sy+////////////////////////////////////////////+sNNssdNm/    oMMNy+//////////+////////oNMMMMNo/////////////////////////////////////////////////////+dMy`                    
                  :NNy//////////////////////////////////////////////////////+hMd/+yNN:  +NNydNms++////+o+//////////mMNMMd//////////////////////////////////////////////////////+yMN.                    
                  yMm+///////////////////////////////////////////////////////smMo/+dMd`-dMy/+sdNmdyyoohNd+////////yMmymMs///////////////////////////////////////////////////////sNM:                    
                 -dMy/////////////////////////////////////////////////+++oo//+dMh//yNm-+NM+///+oshmMNNNNMmo//////+mNyomMo/////////////////////////////////////////////////////+shNMdyo:`                
               `-oNMyso+/////////////////////////////////////////+osyhmmNMNo//hMm+/oNN/sMN///////+dMd-.-sMNy+////oNNoomMs///////////////////////////////////////////////////+ymNmhhhdmNm+               
             .omNMNmmNNmh+/////////////////////////////////////+hmNMMMNmdys+//yNm+/oNN/oMM+//////sNM/    /mNdo///sNN++mMy//////////////////////////////////////////////////+hNmo+////+smMo              
            /mMds+///+ohNNs+////////////////////++ooo+/////////+yhhyo+////////yNm+/sNm:-dMdo///+yNNo      .sNMho/oNNo/dMm+////////////////////////////////////////////////+yMmo////////yNm-             
           :NMy+////////sNNs//////////////+osyhdmNNMMy+/////////////ohds+/////hMm+/hMm` -yMNmddNNd/`        -yNNdhNNs/oNNo////////////////////////////////////////////////oNNs/////////oNN+             
          `hMh+//////////yMd+///////////+yNNMNNNmdhyo+/////////////+dMMmo////+dMh/omMs   `-+sss+-`            .+hmMMd++dMd+///////////////////////////////////////////////hMh+/////////oNN+             
          .NMy///////////omNs+///////////oyyyo++++/////////////////+ohys+////sNMo+yNN.                           `+MNs/+mNh+/////////////////////////////////////////////oMms//////////sNN/             
          .NMy///////////+yMd+////////////////+ydmh+////////////////////////+dNh/omMo                              hMd+/omNh+///////////////////////////////////////////+mNy+//////////hMm`             
          .mMy////////////omMs////////////////odNMmo///////+shhhyhhhhs+////+hMmo+dMh.                              -mMh+/odNdo/////////////////////////////////////////+dMd+//////////omM+              
          `yMh+///////////+yNm+////////////////oss+////+syhmMMMMNhsshmmy+/+hNmo+hMd-                                /mNh//+hNmy+//////////////////////////////////////odNd+//////////+hMd`              
           /NNo////////////omMy+/////////////////////+hmmhyyhNNd/`  `-mNyohNmo+hMd:              `--                `/mMy+/+odNmyo///////////////////////////////////odNd+//////////+yNm:               
           .yMd+////////////oNNy////////////////////+dMs.`  `..`      yMmmNh++hMd:              `oNm.                 :dMdo//+ohmNhso+/////////////////////////////+yNNy+//////////+yNm/                
            :mMy/////////////sNNs+//////////////////sNM.      -o/.``.+NMNds+odMd.               `sMm/-`                .hMms+//+oydmmdhso+/////////////////////+oshmNdo+//////////+hNm/`                
             /NNy+////////////sNNy+/////////////////odMo.```./dNNmmmNMNds++yNNs.                 .odmd:                 `+mNdo+///++shdmmmmhyysooooo+ooooosyyhmmNNmho+//////////+sdNh-                  
              +NNy+////////////sdNdo/////////////////ohNmhyymmmhymNNmho++sdNd/`            ```     `..`                   -smNho+/////++osyhdmmmmmmmmmmmmmmmdhysoo+////////////ohNNs`                   
               /mNh+////////////+hNmhsoo+++///////////+oshdddmmmmmhs+++sdNmo.             `sdo`      .:.                   `-smNdshho//////+++++ooooooooo++++////////////////oymNh:`                    
                :hNms+////////////odmmmmmmdhhyyyyyyyhhhmmmmmdhys++////yNmo.               .NMo.`    .mMs`                     -odNMNs/////////////////////////////////////+ohmNy:`                      
                 .omNho+///////////+++oosyyhhhdddddhhhhysso++:-://////dMy`                `omNmy    .mMy/-                      `+MNs//////////////////////////////////+oydNms:`                        
                   .ymNho+///////////////////++/:-////-``-::.`  .:////mMs`                  .:/-     :yddy`                      -MNs////////////////////////////////ohmNmy/.                           
                     :smNds++/////////////////:.` `.-`    ``     `:///MMo                              `.`                       :MNs////////////////////////////////dMNo-                              
                       .+dNmdso+/////////////:`                   .//+MMo                                                        .MNs////////++ooo++/////////////////mMMd/                              
                          -ohmNmy+///////////`                    `:/oMN/                                                         mMh+/////+ydmNNNmds+//////////////+mdhNN+`                            
                            `.dMd+///////////                     `:/yMd-                                                         +Mms////+hNdsoooymNh///////////////+++sNN/                            
                              +Mmo///////////                     -/+mMy`                                                         `yMms+//oNNo/////sNM+/////////////////+dMh`                           
                              .dMh+//////////`                   .//sNm:                                                           `omNho+omNy+///+yNN+////////+shs+/////yMd.                           
                               +NNo//////////:`                `-//omMs                                                              -mMNdhhNNdhhhmNms///+/+oshmNdo//////yMd.                           
                               `yMm+///////////-`          ``-:///smMy                                                              .sNmyhmNNMMMMMMmhyhdddmNNNMMo///////+mMy                            
                                .hMdo////////////::-...--:/ohdy++yNNs`                                                             .yMmo///+ossyhddNMNyyso+:-:dMh+/////+dMd.                            
                                 .yMms+////////////////+dNNNdyosdMd/`                                                              +MNo//////////+yNN/        -hNNhyssdNNh.                             
                                   +mNds+//////////////+hMmoshmNm+`                                                               `sMd+/////////+hMm/           :shdmdhs:`                              
                                    .+mMmyo/////////////odMNMms:`                                                                  /NNs///////+ymMh-               ```                                  
                                      `/hNNds+///////////yNM-                                                                      `+mNhsoosydNNd/`                                                     
                                        `-odNd+//////////omM/                                                                        -ohmmNmdho:`                                                       
                                           .hMd+/////////omM+                                                                          ``...``                                                          
                                            /Mmo/////////smM:                                                                                                                                           
                                            :Mmo////////+hMN`                                                                                                                                           
                                            .MNy///////+yNN/                                                                                                                                            
                                             yNmyo++++shNm+`                                                                                                                                            
                                             `/hmmmmmmNds-                                                                                                                                              
                                               `.-///:-`                                                                                                                                                
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                          .-`        `                                                                  
                                                                             `-::.`                                      .yNd:      :hh/`                                                               
                                                                           `omNmNmh:   `````                              .hMd`     .oNNo                                                               
                                                                           yMmsosdMmo/sdmmdy/.`                            oms       -mNo                                                               
                                                                         `-MMNddmNNNNNNdssymNmhyo:.`                       `.`       `::`                                                               
                                                                     `./ydmNddyssoo+mMd+///odMNdmNmds/.                       `/+:`                                                                     
                                                                   `/ymNdhso+//////+mms/////sNN++oshmNms:`                    .sNNs                                                                     
                                                                 `/dNmyo+///////////oo+/////omMo////+ohmNh/`                   `yMd`                                                                    
                                                                -hNmy+//////////////////////omMo///////+yNNy-                  `/s:                                                                     
                                                              `+mNh+////////////////////////+hh+/////////odNm/                                                                                          
                                                             `oNNs////////////////////////////////////////+yNN+                                                                                         
                                                            `+NNs//////////////////////////////////////////+yNN/                                                                                        
                                                            :NNy+///////////////////////////////////////////+hMd-                                                                                       
                                                            hMd+//+ss++//////////////////////////////////////+NMo                                                                                       
                                                           `MNy//+yNNNmhyo+///////////////////////////////////hMh.                                                                                      
                                                           /Mmo///+oydNNMMd///////////////////////////////////sMN:                                                                                      
                                                           +Mm+/////+++osso/////////+oyyyyys+/////////////////oMM:                                                                                      
                                       .shdh+`             oMm+////+hNd+//////////+ymNNdddmNNdo///////////////oMM/                                                                                      
                                       odhshm+             oMmo////+hNdo/////////omNdo+///++yNNs//////////////sMN:                                                                                      
                                        `  ``             +mMMms+///+o+/////////+mMh+///////+yNm+/////////////hMh.                       `-/osso+-                         .---`                        
                                                        `oNMMMMNNmhs+///////////yMdo/////////+mNy////////////oMN+                      :yNNNdhhdNNd+/+osyyhhhhhhyso+/-..+hNNNNNNmy/`                    
                                             ./oo/.     /NNoo+/-:+hNms//////////mMh+//////////mMd///////////+dMh.                     +NNho++//++yNMNmmdhhyyyyyyhdmmmNmmNmyo++oshmNd.                   
                                  `ohmdy/    mNddNd-   `oMh.      `+NN+/////////MMy///////////hMd+/////////odMd.                     -mNy+////////smNs++/////////++++yMNy+///////+dMd`                  
                                  `hyosdy`   ..``--     /NNys:     -dMo/////////MNy///////////sMd+///////+smNh.                      /NNo/////////+sds///////////////ohs+/////////oNN/                  
                                   ``  ``               `/dMMm+.``-yNm+/////////NMh///////////sMm+//////ohNmo`                       /NNy///////////+/////////////////+///////////sNN:                  
                                                          `-+hmmmmNNh+//////////hMh+//////////oMmo///+sdNms-                       .omNNmo///////////////////////////////////////omMm`                  
                                                             `-:/yNNhs+/////////sMmo//////////+NNyosdmNdo.                        :dNdsoo+//////////////////////////////////////+ymNNs.                 
                                                                 `:sdNmdys+++++/+dMy+//////////hMNNmNMy.                         /NNh+///////////////////////////////////////////++omNh-                
                                                                    `-oymNNmmdhhhdMNo//////////oNMh+yNm:                        /NNy+///////////////////////////////////////////////+dMh.               
                                                                       `sMMsysyhhdmNm+/////////+yNmo+dMh`                      :dMh+/////////////////////////////////////////////////omMy               
                                                                       `sMM--`.-//+dNd+/////////+hNh/smM/                     `yMm+///////////////////////////////////////////////////sNM/              
                                                    ``.-::///////:-..:shmNNddho:.:/+hNdo/////////+o+/+hMd`                    :NMs////////////////////////////////////////////////////+dMd`             
                                               `./oyhdmmmmmmmmmmmmmmmNmhsoooshmNo.-/+hNd+/////////////yNMh+.                 `oMm+/////////////////////////////////////////////////////sNm:             
                                           `-+ydNNmdyssoo+++++++++sdMd+///////omNo`://++//////////////sNMmNd:             `.:omMh+/////////////////////////////////////////////////////oNN+             
                                        `:odmNdyso+///////////////oNMs/////////yMh.-//////////////////yNN+dMh`           .odNmNMy+/////////////////////////////////////////////////////+mNy:/:.`        
                                      ./dNmhs++///////////////////ommo/////////hNNo//////////////////odMyodMy`          -dNdo+dMy+////////////////////////////////////////////////////+sNMNmmmNds-      
                                    .+dNdy+////////////////////////++//////////oyhNNho//////////////odMNhmNh-           yMdo/+hMh+///////////////////////////////////////////////////+hNmyo+++sdNm/     
                                   :dNms+//++oshhhso+/////////////////////////////ohNmy+//////////+smNNmdy/`            NMh//+yMm+//////////////////////////////////////////////////+yNmo//////+hMm`    
                                 `oMNy+//+ydNNmddmmNmyo/////////////////////////////omNho//////+oymNd+`                `MMy///omMy//////////////////////////////////////////////////sNNs////////sNM-    
                                .yMms///smNds++///+ohNNs/////////////////////////////+hNmo++oshmNNh/`                   mMh+//+yNN+////////////////////////////////////////////////+NNy+////////sNM-    
                               .yMm+///oNNy+////////+sdh//////////////////////////////+hNNNNmNNMm:                      oMmo///+dMd+//////////////////////////////////////////////+dMd+/////////yMN`    
                              `sMmo////yMd+////////////////////////////////////////////+dMmo+++mMy.                     .dMh+///+dNd+////////////////////////////////////////////+hNd+/////////+dMy     
                              /MNs/////yMm+/////////////////////////////////////////////omNy///oNN/                      /NNy////+dMmo+/////////////////////////////////////////odMm+//////////yMN-     
                              mMh+/////+NNh+/////////////////////////////////////////+ydhyMmo//oNM+                       /NMy+///+smNdo//////////////////////////////////////+yNNh+//////////sNN/      
                             :MNs///////odNh+/////////////////////////////////////+ohNMNdoMNy+smMh.                        /NNh+////oyNNds+/////////////////////////////////+sdNds+/////////+yNNo`      
                             oMmo////////+o+////////////////////////////////////+ymNMNho+/dMNNNdo.                          :mNdo/////+ymNmhs++//////////////////////////+oymNms+//////////+hNm/`       
                             yMd+//////////////////////////////////////////////oNMNdy+////yMMs-`                             .sNNh+/////+oydmNdhyoo++/////////////+++osyhmNNds+//////////+ymNh.         
                             hMd+//////////////////////////////////////////////+syo+oys+//yMMm.                               `:hNmy+//////+osydmNNmmmdhyyyyyyyhhdmmNNmdhyso+//////////+smNd/`          
                            `yMmo++/////////////////////////////////+++////////////smMNd+/hMMM+                  .-`            `:hNmho+///////+++oosyhhhhddddhhhhyso+++////////////+oymNd+`            
                          .+yNMMNNmdy+///////////////////////////+oydmh+///////////odNmy+/NMMMy                 :dN:              `:ymNdyo+/////////////+++++++//////////////////+oydNmy/`              
                         +mNmysooosdNmy+/////////////////////++oymNNNmy+////////////++++/oMNmMy                 /mMo-               `.+hmmdyo////////////////////////////////++oydNmh+.`                
                        oMNs+//////+odNh+//////////////////oydNNMNdyo+//////////+//++++/+dMddMs                 `/hdo                  `-+dMm+//////////////////////////////+ymNmy+-                    
                       :mNy//////////omMy/////////////////+dMNmhs+++/////////+shdddmmmmhhNmyNM:                   ```                     yMm+//////////////////////////////+sNNo`                      
                       oNN+///////////sNNs/////////////////+oo+//odmdo/////++hNMMMNo::+mMMshMd.            :hy       `+y:                 oNm+////////++oosoo+///////////////oNN/                       
                       oNm+///////////+yMdo//////////////////////hMMNy///+sdmmNMMm+`  `sMNoNN+            `sMm.      -dMs`                :mNy///////+hmmmmmmdy+/////////////sNN:                       
                       +NNo////////////+mNh+/////////////////////oyys+//odNh+--//.`   .yMdmMy`             :dNd/     `oNms.                yMm+/////+dNds++osmNh/////////////yNm.                       
                       .mNh/////////////omNy+//////////////////////////+hMh`     `:++odNmmMh.               `-:`       -+/`                .dNdo////oNNo/////yNN+///////////+dMd                        
                        oMmo/////////////smNh+/////////////////////////+hMo     `+NNmhyymMh.                                                -hNms+//+mNh++/+odMd///////+os+/+mMs                        
                        `hMdo/////////////odNdo/////////////////////////sNN+-.-/yNms++smNh.                                                  /NMNmhsosmNmddmmNho+++osyhmmm+/omM:                        
                         .dMdo/////////////+hNmy+///////////////////////+ymMNmmmdy+/+yNNs.                                                  `oMdsydmmmmNNNNNmdhhdmmmNdhyo+/+yMN`                        
                          -hNmo//////////////sdNmyo++++//////////++++oshdmNmhyo++/+ohNm+`                                                   `yMh+/++ooyyyhNMNhdMNhsoo+/////odMs                         
                           .sNmy+/////////////+sdNNmmddhhyyyyyyhdddmNNmdhs+://///+ymNy.                                                      +NNo///////+yNN+`hMd+////////+yMN-                         
                            `/mNdo//////////////+osssyhhhddddddhhysso////:` `-///sNN+`                                                       .yNNyo++++sdNm/`:mMo/////////omNo`                         
                              .sNNho+//////////////////////+///:///:. `..`    ./+hMh.                                                         `/hmNmmmNmdo.  /mMo////////omMy.                          
                                -yNNho+//////////////////////:.``..`           -+hMy`                                                            .:///:.`    .hMd+/////+smNy.                           
                                  -yNNds+////////////////////`                 `+dMs`                                                                         -hNmhysyhmNN+`                            
                                    .+dNNhs+////////////////`                  `+dMo`                                                                           :shdddhs/`                              
                                      `-smNmhs+/////////////                   -+NM+                                                                                `                                   
                                         `-yNMd+///////////:                  ./oNMo`                                                                                                                   
                                           -mNy/////////////                `.//+smMh`                                                                                                                  
                                            hMd+////////////-`            `.://///odMh`                                                                                                                 
                                            /MNs/////////////:.`      ``.-/////////oNNo                                                                                                                 
                                             hMdo///////////////::--:://oyy+///////+mMy                                                                                                                 
                                             .hMdo/////////////////++oydNmd+///////oNNo                                                                                                                 
                                              .yNmo/////////////ohdmmmmhs+////////+hMd.                                                                                                                 
                                               .hMd////////////+mMMNyo+//////////odNm:                                                                                                                  
                                                yMm+///////////sNNdNmyo+++++++osdNmy.                                                                                                                   
                                               .hMh///////////+dMh./ymNNmddddmNmho-`                                                                                                                    
                                               /NMo//////////+yNN-  `.-/++oo+/:.`                                                                                                                       
                                               oMM+/////////+sNN+                                                                                                                                       
                                               +NMo////////+yNNo`                                                                                                                                       
                                               `oNNho++++oymNd/`                                                                                                                                        
                                                `:ydmmmmmmmh/.                                                                                                                                          
                                                   .-://::.`                                                                                                                                            
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                             `---`                                                                                      
                                                                                                .:oss+-   `/ymmdmdo                                                                                     
                                                                                               +mmdyyNm:  .sho--sNM.                                                                                    
                                                                                               ./--:sMm:   ``:shmms                                                                                     
                                                                                                 -hmds:`     /so/-                                                                                      
                                                          .-/+/-`                                `--`   ```                                                                                             
                                                        -smNmmmNm+..--::::::---..`                   `:shddy/`                                                                                          
                                                       .hMdsooymMMmmmmmmmmNNNNmmmds+-`               `+yo/sNN/                                                                                          
                                                       :MNhdmmmmhyssoo+++yNNhsooshNMNdy+-`             `/odNm-                                                                                          
                                                      -sMNmdyo++////////omMs//////smMddNmh/.           .yhs+.                                                                                           
                                                   `-smNds+/////////////smd+///////dMm+oydNmo.          ``                                                                                              
                                                  .sNNho/////////////////+/////////hMm+///sdNm+`                                                                                                        
                                                 :mNdo+///////////////////////////+dMy/////+smMy.                                                                                                       
                                               `+NNy+/////////////////////////////+ss+///////odMd-                                                                  `-/+++/-`                           
                                               +NMs///////////////////////////////////////////+dMh.                                    .:+osss+-`   ```...-...````-odNmmmmmNmy:                         
                                              :mMh+////////////////////////////////////////////omMs`                                 -smNNddddNNdsyhdmmmmmmmmmmmdhmMdo+++++ohNN+                        
                                             `hMMdhs+///////////////////////////////////////////sNN-                                /mNho/////+smMNhyysooo+ooosyhMMy+////////sNN:                       
                                             -MMmNMms/////+so++/////////////////////////////////+dMy                               -dMh/////////+NNy////////////+hy+/////////+mNo                       
                                             oMmo+++/////+dMMNNdhhso+///////////////////////////+hMm                               :mMs//////////oyo/////////////////////////sNN+                       
                                             yMNdo////////+syhmmNMMNs////////////+osyddhys+//////hMM                              `+NMh/////////////////////////////////////omMMh:`                     
                                             hMMNs///////////++++oso+///////////odNNddhddNNho////hMM                             `hNNNNs////////////////////////////////////+sshNNs`                    
                                             yMdo///////////yNms+//////////////sMNy+/////+hNmo//+hMm                            /mNho+o+///////////////////////////////////////+odNm-                   
                                             +Mmo+oo++//////ymNy+/////////////omNy////////+hMh+/+dMs                           /mMy+/////////////////////////////////////////////+hNm:                  
                                            .yMNmNNNNds+////++++/////////////+dMd+/////////sMNo/yNN-                          /mMy////////////////////////////////////////////////+hMd:                 
                                           -dNy::hMMMMNmdyo+/////////////////omMs//////////oNMoomNo`                         .dMh+/////////////////////////////////////////////////+mMy.                
                                           sMm.  `/o+/:/omNh+////////////////yNN+//////////oNMsmMy.                          oMmo///////////////////////////////////////////////////oNN/                
                                           +Nm:`         -dMs///////////////+hMh///////////sMMNNy.                          `NMh+///////////////////////////////////////////////////+hMNy-              
                                           `sNmyss+`     .hMy///////////////omMs///////////yMMN+`                        `-/oMNy+///////////////////////////////////////////////////+yMMNNo`            
                                             -+yhdNdo/-:+hNd+///////////////sNNo//////////+hMm:                        .sdmmmmNNmh+//////////////////////////////////////////////////sMMyNN+`           
                                                 `/hNMNNNds+///////////////+yMd+//////////oNM+                       `+mNhs++++shNms+////////////////////////////////////////////////sNMoyMd-           
                                                   `oNMMNdys++/////////////+dMy+//////////sMm-                       :mMy+//////+sNNs////////////////////////////////////////////////sMNooMN/           
                                                    `/dMNmmNmmdhyssooooooooyNNs//////////+mMs`                      `yMd+/////////hMd+//////////////////////////////////////////////+yMd+oMM/           
                                                      .smNdyoyhhdmmmmmmmmmmNMmo//////////sMMo                       -dMy//////////oNNs//////////////////////////////////////////////+dMy+oMN:           
                                                        :dMy.-///:++++ooo++hNh+//+syddhsomMMs`                      -dMs//////////+hMh+/////////////////////////////////////////////sNmo/yMm-           
                               ```          ``          .hMo  ..``.::.-:///+o+//smNdhhdNNMNMh.                      .hMh///////////sNNo////////////////////////////////////////////oNNy+/mMy`           
                             .oyhyo.     `/syy+-`       `sMh       ````-+oossssyNNhoo++yNMdMm-                      `oNN+//////////+hNd+//////////////////////////////////////////omNy+/sMm/            
                            .dMhoymm/   `sNdoymNy.       +NM`  ``.:+yhdmmmmmmmmmmmmmmNmmNMNMN:                       -dMy///////////odMh+///////////////////////////////////////+smNy+/omNs`            
                            `dNs-`-/.   `oNd:`.os.       -dMo-/sdmNdhyssoooo++++++++ossyhdmNNh+:`                     +NNs///////////omNh+/////////////////////////////////////odNms//odMh`             
                             .hNmh-      `omNy-          `sNNmmdyo++//+ydmmmmho//////////++oydNNds-`                  `sMmo///////////omNdo/////////////////////////////////+ohNmy+/+odMd.              
                               .//`        .//`        .+dNNhs+//////omNds+ohNmo//////////////+shNNh/`                 `yMmo///////////+hNmy+///////////////////////////++oymNmy+//+sNNy`               
                                      ``             `+mNmy+////////+mNy+///+hmo/////////////////+ymNh/`                `sNms///////////+sdNmyo++///////////////////++oyhmNmhs+///ohMm+`                
                                    -sdmds:`       `:dMms+//////////yNm+/////++////////////////////+ymNh-                `oNNh+///////////+smNNNmdhysooooooooooosyhdmNNmdyo+////+hNNy-                  
                                   .NMy/omm:      `sNNy+///////////+dMd//////////////////////////////ohNN/                 -hMms+///////////+oyyyhddmmmNNNNNNNmmmddyys++//oyo+ohNNh:                    
                                   .NMy- `.      `hMms/////////////+dMd///////////////////////////////+yNN+                 `+mNds//////////////////+++++++++++++/////////NMmmNNs-`                     
                                    -smNh`      .dMdo///////////////hMm+////////////////////////////////sNN+                  `+dMmyo+////////////////////////////////////mMNh/`                        
                                      `-.      `yMm+////////////////odh+/////////////////////////////////yMm:                   `/hNNdy++/////////////////////////////////mMy`                          
                                               +NNo//////////////////+///////////////////////////////////+dMh`                    `.+hNNmhs+//////////////////////////////dMy`                          
                                              -dMy////////////////////////////////////////////////////////sNM/                        ./yMMd///////////////////+//////////mMs`                          
                                              +MNo////////////////////////////////////////////////+oo+////+dMh                        :sdMMy///////////////+ydmmdhs+/////+MM+                           
                                             `yMh+/////////////////////////////////////////////+ohmNNy/////hMN                      .hNmhhNN+/////////////sNNdysydNmo////yMd-                           
                                             .dMy+//////////////////////////////////////////+shmNMNds+/////yNM`                    `sMmo/+hNd+///////////+mNy+///+hMm//+sNN+                            
                                             .mMy+/////////////////////////////////////////+hNNNdso+///////sNM.                    .yMh///+so////////////+mNy+///+hMm+ohNMh`                            
                                             .dMy+/////////++///////////////////////////////oys+++oo+/////+yNM-                    `oNNo//////////////////sNNdysydNNhdmmdNN+`                           
                                             `hMh+/////+syddddhys+//////////////////////////////+hNNd+///odNMMh-                    .yNmyo++///////////++++sdNMMMMMNmdyo+yMm/                           
                                             `oMm+///+ymmdhyyyhdNmy+////////////////////////////+hNNh++shNMMMMMmo`                   `:ydmmmmdhhhhhhddmmmmmmNMMmdhso++////dMy`                          
                                              :mMy//+dNds+/////+odNh+////////////////////////////+oo+ymmyosdmhodNo`                     .-/+osssyysssoo+//:::yMmo////////+mMs`                          
                                              `sMm++hNd+/////////omMy+//////////////////////////////yNd:`  `.``oMm.                             ```          .yNmyo++//+ohMd:                           
                                               -dMhsNNo//////////+yMm+/////////////////////////////+NN+      :dmMh`                                           `/hmmdhhhmNms-                            
                                                :mNmMd+///////////oNNo/////////////////////////////+mNo`    `yMNh-                                              `-/osyso/-                              
                                                 :mMMh+///////////+dMy//////////////////////////////omNy/--/yNd/`                                                                                       
                                                  :mMh+///////////+hMd//////////////////////////////+sNMNdmmho.                                                                                         
                                                  `oMm+////////////sNM+///////////////////////////+ohNNs---.`                                                                                           
                                                   :NMs////////////+dMy////////////////////////++sdNmy-                                                                                                 
                                                   `yMm+////////////sNNo////////////////////+oshmNdo-                                                                                                   
                                                    :mMy////////////+dMd+///////////++++ooydmNNMm/`                                                                                                     
                                                     +NNy+///////////+NNdyysssssyyyhhdmmNNddysoMN/                                                                                                      
                                                      +MNs+///////////sNNmmmmmmmdddhhysso+/-:/-hMy`                                                                                                     
                                                       +NNy+///////////+o+////////////////.  ` /Mm-                                                                                                     
                                                       `/mNd+/////////////////////////.`..     .NM/                                                                                                     
                                                         -dMms+//////////////////////`         `yMo`                                                                                                    
                                                          yMMNho////////////////////-          `sMy`                                                                                                    
                                                         .hMdhds////////////////////.          `sMy`                                                                                                    
                                                       -smMMh///////////////////////`          `yMNyo/-`                                                                                                
                                                      /NNhmMd///////////////////////`          -NMdhmmNmho-`                                                                                            
                                                     .mNy+sNNo//////////////////////.          oMd++++osdNNh:                                                                                           
                                                     .mNy++mNh+//////////////////////`       `+Nms///////+yNN+                                                                                          
                                                      +NNhssNNy+//////////////////////-.```.:sNms/////////+hMd                                                                                          
                                                       -sdmmNNNho/+///////////////////////+smNdo//////////odMy                                                                                          
                                                         `.-:odMNdho///////////////////+oymNMNhssoo+++++oymNd-                                                                                          
                                                          -odmNNmdyo///////////odyoosydmNmysyhddmmmmmmmmmmho.                                                                                           
                                                        `omNhsoo++////////////+dMNmmmhyo:.    ``..--://:-.`                                                                                             
                                                        :NMy/////////////////+yNN+-..`                                                                                                                  
                                                        +MN+////////////////+hNN/                                                                                                                       
                                                        /NMs//////////////+ymNh:                                                                                                                        
                                                        `sNNy++/+////++oshmNd+.                                                                                                                         
                                                         `/hmmmdhyyhhdmmmds:`                                                                                                                           
                                                           `-/osyyyyyo+:-`                                                                                                                              
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                           .:/-`                                                                                                        
                                                                                  ``      `+dmNh:                                                                                                       
                                                                                `sdmh/`    `..hMh`                                                                                                      
                                                                                `:/oNN+       sh/                                                                                                       
                                                                                   -mm+       ``                                                                                                        
                                                                                    -.  `:/:.                                                          .:++o+/:.`                                       
                                                                                        /dmmd+`                                                      .smNmddmmmmy:`                                     
                                        ``----.`     ````````````                        `.sMm.                              `.-/++/:-````..--------/dMds+++++oyNNo`             :yy/`      ```         
                                      .+ydmmmmdy/:/+oyyhdddddddhyso+:-``                  `/h+`                            `:ymNNmdmNmhshddmmmmNNmmmNNNmhhyo++//sMN:             -smMs`    .ydy:`       
                                     :dNdysooymMNmmmdhhyyyssyyyyhmMMNNmhs/.                 `                             `oNNho++++oymMNhssoooooooooosyhdmmmdhssMM/              .hMh.    `:oMm/       
                                    .yMd++sdmNmhyo++//////////+sdNmhyyydmNNy/.                                            /NMo////////+dNy+////////////////+sydmNMM+`             :hy-       oMm/       
                                    .hMhhmNdyo+//////////////+yNNs+/////+odMMdo-                                          oMM//////////+so////////////////////++sdNNy:`               ``     +s:        
                                    `sMMmho+/////////////////+hms/////////+MMNNNo.                                       -hMMo///////////////////////////////////+oymNy-             :dds.              
                                   `oNNh+/////////////////////++//////////+MNysdMd:`                                    +mNmNd+/////////////////////////////////////+hNNo.           ./hMd`             
                                  .hMms+/////////////////////////////////+hMmo/+yNN+`                                 `sMNy+ss+//////////////////////////////////////+smMh`           -hNd`             
                                 -dMd+////////////////////////////////////sy+///+sNN+                                `yMmo/////////////////////////////////////////////+dMd.          .oo`              
                                .hMd+////////////////////////////////////////////+yNN:                              `oNNo///////////////////////////////////////////////+mMy`                           
                               `sMm+//////////////////////////////////////////////+dMd`                             :mMs/////////////////////////////////////////////////oMN+                           
                               :NMdso++////////////////////////////////////////////oNN/                            `yMd+//////////////////////////////////////////////////hMd-                          
                              `sMMMMNNmdy+/////////////////////////////////////////+mMy                            .NMy+//////////////////////////////////////////////////oMN/                          
                              .dMhoyhdmNd+////////sysoo+++//////////////////////++oodMh.                         `-sMMmdhyo+//////////////////////////////////////////////+mMo`                         
                              .NMy///++++////////+mMMNNNmddhys+///////////////oymNNmNMNdo.                      -yNNdyyyhmNms/////////////////////////////////////////////+dMs`                         
                              .NMy/oddy+//////////+osyhddmNNNdo/////////////+ymNhso++osdNm/                    -dMd++////+smNy////////////////////////////////////////////+dMs`                         
                              .mMy/sNNNo////////////++o+++++++//////////////sNmo///////+yNN/                  `yMd+////////sNNs///////////////////////////////////////////+mM+                          
                              `yMh++ooo+////////////smNdo//////////////////+dMy+////////+mMy`                 .NMy//////////hMd+//////////////////////////////////////////sMM/                          
                               /MNo/++++oyyo+///////odNdo//////////////////oNNs//////////yMd.                 :MNo//////////oMNs//////////////////////////////////////////dMN:                          
                               :mMdhdmmmNMMNmysso+///+++///////////////////yMd+//////////yMd.                 :MNs///////////dMh+////////////////////////////////////////sMMN:                          
                               -mMMNo:-/dNMNmhdmmdo+//////////////////////+NNy///////////hMh`                 .NMy///////////sNmo///////////////////////////////////////sNMMm:                          
                               -dMMy    `:/:.``./mNy//////////////////////oMmo//////////+mMs                  `yMd+//////////+hNd+////////////////////////////////////+ymNmMh.                          
                               `yMMm:`           +Md+////////////////////+dNh+//////////yNN:                   :mMs///////////odNd+//////////////////////////////////ohNmyNNo                           
                                /NMNmdyydh+.`  `-hNh+///////////////////+yNmo//////////omMs                    `oNNo///////////odNdo//////////////////////////////+oyNNhsdMh.                           
                                `sMNyyhmMMMmhsshmmy+///////////////////+yNmo//////////+hMm.                     .yNmo///////////+hNms+//////////////////////////osdmNhoodMd-                            
                                 .hMdo++sdNNMNmdyo+///////////////+++oymNmo//////////+yNN:  ./oss+-`             .yMmo///////////+ymNho+//////////////////+++oydmmdyo+smNd.                             
                                  `yMms+//+sydmmmmdhyyssssossssyyhdmmNmmy+//////////+hNm/ `omNmddNNy`             `yNms+///////////ohmNdhyssoooooooooossyhdmmmmhs+++odNmo`                              
                                   `omNh+////++osyhhddmNmmmmmNmddhhyso++///////////+hMm/  yMms+/+omMy`             `+mNdo////////////oymNmmmmmmmmmmmmmmmdhhyso+//+ydNms-                                
                                     :yNmyss+///:..://:-/+++///++////////////////+smNh-  :MNyossyymMNhysso+/:-.``    -sNNho+///////////+o+++++ooooooo+++++///////sMMo.                                  
                                      `:hNMMs//-`  `..  `--.``.:////////////////ohNms.-/smMNNNmddddddddmMMMNNMNmhs+:.` :hNNho+///////////////////////////////////sMM.                                   
                                        `/mMy/:`               `://///////////+yNNdyymNNdhsoo++++////+yNNhsooydNMNNNmh+-`:ymNdy++////////////////////////////////sMM-                                   
                                         `yMd/:                 `////////////+hMMNNNdyo+////////////+hNdo/////+yNNsoydmNdo-.+hmNmyo+/////////////////////////////sNM:                                   
                                          oMN+:                  ://////////+sNMNds++///////////////oNms+//////+hMh///+sdNNy:`-+hMNh/////////////////////////////omM:                                   
                                          :mMs:.                 ://///////ohNNho///////////////////+so+///////+hMd/////+oymNy-.sNNs///////////////////////+/////sNM-                                   
                                          `hMd/:`               .////////+yNNho////////////////////////////////+hMh////////+hNNmMNMd///////////////////+oydddhs+/yMN.                                   
                                           +NNo//-`            .////////odMdo//////////////////////////////////omMs//////////smMmyMmo/////////////////odNmhyhmNmshMy`                                   
                                           `hMd+////-..`````.-////////+smNh+//////////////////////////////////+yMh+///////////+dMddms/////////////////dMh+///+yNMMm:                                    
                                            -NNy+//////////+yhds+/////oNNy+////////////////////////////////////+s+/////////////+dMd+/+os+/////////////dMh+////yNMm/                                     
                                             +MNs///+o+//+ymNdy+/////+NNy+//////////////////////////////////////////////////////omNy/+hNNdyo+++///////omNmhyydNNy-                                      
                                             `oNNs/+hNmhsyNNo+//////+dMd+////////////////////////////////////////////////////////sMmo//+shmNNNmddddddddmNMNNNMN/                                        
                                              `oNNy++oydmMMh////////sNNo////////////////////////////////////////////////////////+hMMy+////oNMh+hMNdhhyyysso+smMh`                                       
                                                /dMdo+/+sNMo///////+dMh///////////////////////////////////////////////////////ohNMMMd+////sNN/ .dMd+/////////omMo                                       
                                                 .sNNhs/sMMo///////omMo//////////////////////////////////////////////////////+hNNdyMmsosshNNo`  -mNho////////+dMh                                       
                                                  `-smNdhNMs///////sNM+///////////////////////////////////////++//////////////+oo+yMMNmNmhs:     -hNmy++///++yNM+                                       
                                                     ./hmNMd+//////sNM+/////////////////////////////////+osyhhddhys++///////////+dNMMs:.``        `+hmNdhhhdmNd+                                        
                                                       `./hMmysooosdMM+///////////////////////////////+sdNmdhyyyhdmmho//////////omMMMNd:            `-/osyys+:.                                         
                                                          `/ydmmmmmdNMo//////////////////////////////+hNms++/////+ohNms+/////////+yMMMMh                                                                
                                                             `.---.-hMh/////////////////////////////+yNmo//////////+sNNs//////////yMmNMh`                                                               
                                                                    oNNo////////////////////////////+mMy+///////////+hMm/////////+NNo/mNo                                                               
                                                                    .dMd+///////////////////////////sMmo/////////////sNM+////////yMd. yMh`                                                              
                                                                     :NNy+//////////////////////////yMd+/////////////omMo///////omN+ -mMs                                                               
                                                                      +NNy+/////////////////////////mMh//////////////omMo//////odMd/smNs`                                                               
                                                                      `+mNy+///////////////////////+MNy//////////////yNM+/////odNNmmhs:                                                                 
                                                                        /dNdo+/////////////////////oMmo/////////////+hMm////+smNs..``                                                                   
                                                                         .oNNho+///////////////////yMd+/////////////+dMy//+sdNd/`                                                                       
                                                                           -yNNds++///////////////+mNy//////////////sNNo+ydNmo.                                                                         
                                                                             -odNmhs++////////////sNmo/////////////+hMmdNNh+.                                                                           
                                                                               `:odNNdhyso++/////+mMh//////////////sNMMMo-`                                                                             
                                                                                  /NMhdmNNmmdhhyyhNN+/////////////+mMmNM+                                                                               
                                                                                 `sMm///+osyyhdmNMNs//////////////yMd:yMd`                                                                              
                                                                                 -dMy//////////+dMh+/////////////yNm: :NN:                                                                              
                                                                                 /MNo//////////yNd+/////////////sNM/  .mNo                                                                              
                                                                                `sMd+//////////+++////////////+yNNo    mMy                                                                              
                                                                                `hMh+/////////////////////////+yhs.    yMh`                                                                             
                                                                               `:mMy//////////////////////////////.    yMh`                                                                             
                                                                             .+dNMMy+/////////////////////////////`   `mMh                                                                              
                                                                            .hMmsdMy+/////////////////////////////`   -mMN+`                                                                            
                                                                            +MNo+yMd+/////////////////////////////.  `sNNNNo`                                                                           
                                                                            /NNs/smNs/////////////////////////////: `+NNoyNN-                                                                           
                                                                            `oNNhydMNo//////////////////////////////yNmo/odMo                                                                           
                                                                             `-ohdmmMms+/////////////////////////+ymNho//+hMh                                                                           
                                                                                `...+mNdyso+////////////+////++shmNdo+///+hMh                                                                           
                                                                                     .+hNMm+//////////+ymyyyhdNMNho//////omMo                                                                           
                                                                                      .sNNy+//////////sNMmddyo+NMy+/////+hMd.                                                                           
                                                                                     /dNms+//////////odMy.``  `/mNdyssyhmNh-                                                                            
                                                                                    /NNy+///////////odMh.       .+ydmmdhs:`                                                                             
                                                                                   `dMd+//////////+smNy-          ``````                                                                                
                                                                                   `dMd+////////+sdNm+`                                                                                                 
                                                                                    :mNhs+++++oydNms.                                                                                                   
                                                                                     -sdmmmdmmmmy+.                                                                                                     
                                                                                       `-/++/:-`                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                               :so/.                                                     `.://:.`                                                       
                                                                               /hdNd-                                   ````            -ymmmmmmh/`                                                     
                                                                     `//-`      `-hm/                                ./shddhy+-........:mNho++oymNs`                      -/.                           
                                                                     :dmNd:       `.                               `omNmhyyydNNmmmmmmmmmMNdhyso+oMN/                      yNm/       ``                 
                                                                      `-yNy                                        sNms+////+smMdsoooosssyhhmmmmdMMs`                     -mMs`     +dh:                
                                                                        .:.  `:++-`                             `-oMNy////////sdy+/////////+++oshmNNh/.                   -hy-      .hMd.               
                                                                             `sdmNy.                          `/yNNMmo///////////////////////////+oydNmo-                  `        .dNs`               
                                                                              ``:Nm:                         -hNmyoNNy//////////////////////////////+odNmo.                  -/.     -:`                
                                                                                 ..                        .sNNy+//yNh+///////////////////////////////+odNd:                `sNN+                       
                                                                                                          -hMmo////+so+/////////////////////////////////+hNN+`               .dMy`                      
                                                                                                         -dMd+///////////////////////////////////////////+sNN+`              :dh-                       
                                `            ````````                                                   `dMd+//////////////////////////////////////////////yMm:                                         
                           `-+syhys/.`.-+osyhddmmmdddhys+/-````                                         oMmo///////////////////////////////////////////////+dMy`                                        
                         `omNNdhyhNMMNNNmmdhyyyyyyyyyyhdNMMMNNmdyo:`                                   .mMh/////////////////////////////////////////////////sMM-                                        
                         yMms++shmNmdys++//////////////smNmysssydmNd/                                  +NNo/////////////////////////////////////////////////omMo                                        
                        -MNsohNNmyo+//////////////////sNNy+//////+yNN+                                 sNm++syyyso+/////////////////////////////////////////+dMy                                        
                        -MNmNNyo//////////////////////hmy/////////+hMMo.                               yMNmNmmmmmNNho///////////////////////////////////////+hMh                                        
                        .MMNy+////////////////////////++//////////+hMNMm/`                             sMMds++/++oyMNs+/////////////////////////////////////+dMy                                        
                       /mNdo//////////////////////////////////////smNssmNs`                           `hMd+////////sNNs/////////////////////////////////////omMo                                        
                     `+mNy+///////////////////////////////////////oys++omMh`                          :mMs/////////+hMd+////////////////////////////////////yMN-                                        
                     /NNy///////////////////////////////////////////////omMy`                         +NM+//////////omNy///////////////////////////////////omMs`                                        
                    -mMy+////////////////////////////////////////////////sNN+                         /NMo//////////+yNN+/////////////////////////////////+dMh.                                         
                    hMd+/////////////////////////////////////////////////+hMh.                        -dMy///////////+mMy////////////////////////////////+dMd-                                          
                   -MNs///////////////////////////////////////////////////oMN/                         sNmo///////////sNNs/////////////////////////////+smNy.                                           
                   +Mmo//ohhhysssoo+///////////////////////////////////+ossMMy:.                       .dMh+///////////sNms+/////////////////////////+ohNmo`                                            
                   yMd+//ymNNNNNNNNd+/////////+syyysssoo+++///////////sdmmmmmmmms-                      :NNy+///////////yNNy+/////////////////////++sdNms-                                              
                   hMd+///++oossyyhs+/////////smNNNNMMNNNNmo////////+hNmyo++++ohNm/`                     /mNy+//////////+smNdo////////////////++oshmNdo-                                                
                  .mMd+///////+++/////////////++ooossyyyyhy+////////yNNo///////+hMm-                      /dNd+///////////ohNmyo////////+++osydmNmmNM+                                                  
                 `sMMmo//////omNms////////////////+oo+/////////////+dMy/////////+mMo`                      -hNms+//////////+odmmdhhhhhdmmmmNmdhys++hMd                                                  
                 -dMMNy//////omNms+//////////////+mNNd+////////////omMo/////////+hMy`                       .yMNdyso+/////////oyddhhhhhhysso++/////sNM-                                                 
                 /mMdMd+//////+++////+++++////////hmmh+////////////yNN+/////////+hMy`                     `:ymNmmmmNds+/////////++/////////////////+dMy                                                 
                 /NMsmMy+///////+osyyhmmmdsoo++////++/////////////+hMh//////////+dMo`                    `oNNyo++oodMNhyyyyyyssooo++////////////////yNm.                                                
                 :mMssmNy/////+ymmdhdNMMMMNmmmdy+/////////////////omMs//////////oNN/                     -NMhshdmmmmNNmddddmmNmmmmmdhhhyo+//////////oNN/                                                
                 `hMd+smNh+///hMh:```-sdh+-..:yNmo///////////////+hMd+//////////dMh.                  `.:hMMNmdhyso++++++++++++oyNNmmddmmmho+/////+++mNo                                                
                  /NNs/odNms+/NMs      `      `yMh///////////////sNms//////////sMm/                 `:sdNmhyo+////////////////+yNNy+///+ohNNds++shdmdNMs                                                
                  `yMmo/+smNdsyMm+.``-oy:`    .yMh//////////////sNNy+/////////omNs`               .+dNmhs+////////////////////sNNs///////+hNMNmNMdhyhmMd-                                               
                   `hMmo+/+sdNNmNNMmmNmmNho//smNd+///////////+ohNms//////////omMy`              .+mNds+//////////////////////+shs+////////oNNshNNho//+dMy`                                              
                    .yNms///+oydNNNmhso+shddddyo+///////++oshdNNmo//////////omMh`              /dMms+/////////////////////////////////////sNNo/ohNmy++dMy`                                              
                     `+mNdo////++sydNNNmddhhyssssssyyhhdmNNNddds+//////////sNNs`             `sNNy+//////////////////////////////////////+dMd////smNdmMd:                                               
                       .sNNho///////++osyhddmmmmmmmdddhyyoo+/////////////+hMm+`             .yMmo////////////////////////////////////////sNNo/////+dMMo`                                                
                         -yNNdo+//////:..:///-.:/+//-://///////////////+ymMh-              .yMm+/////////////////////////////////////////+so///////+dMd.                                                
                           .omMd+////.   `..    `-.   `-/////////////+ymNd/               `sMmo/////////////////////////////////////////////////////+mMy`                                               
                             -MNs///.                  `-//////////+ymMd/`                :NNs+//////////////////////////////////////////////////////oMN/                                               
                             `MNy///`                   `:////////omMh:`                  dMh+///////////////////////////////////////////////////////+mMy`                                              
                              NMh///`                   `-///////+hMd.                   -MNs/////////////////////////////////////////////////////////yMm-                                              
                              dMh+//`                   `-///////oNM+                    +Mmo/////////////////////////////////////////////////////////oMN:                                              
                              oMmo//:`                  .////////sMm-                    sMm+///////////////////////////////////////////+oyhhhhyo+////oMM/                                              
                              -NMy+//:.`              `.////////+mMy`                    sMd+/////////////////////////////////////////ohmmmhyyhmNds+//oMM/                                              
                             `yNNy+////:-.``      ``.-://///////yMm:                     sMm+///////////////////////////////////////+yNmyo++///+smNy+/oMN:                                              
                            `yMdo+//////////:::::://///////////sNN+                      /Mmo//////////////////////////////////////+hNmo/////////sNNs/yMm-                                              
                            /NNs////////++////////////////////+dMy`                      `NMy+/////////////////////////////////////sNNo//////////+hMh+mMy`                                              
                            +NNo///////ommmhyyyyssoo+/////////omMo                        sMmo////////////////////////////////////+dMy+//////////+yMdsMN/                                               
                            .mNh+//////+osyhhNMNmdNms/////////+hNm-                       .dMh+///////////////////////////////////sNmo///////////+yMmNMy`                                               
                             :mNho++/////++ohMm+..sMmo/////////+hMh-                       /mNy///////////////////////////////////dMh+///////////+hMNMd.                                                
                              -smNmhhyyyhdmNms-   `sNmy+////////+MMo                       `+mNy+////////////////////////////////+MNs////////////+mMMd.                                                 
                                ./oshhhhys+:.      `+mNds+/////+sMN/                        `/mNho///////////////////////////////yMm+////////////sMMy.                                                  
                                    ```              .odNmdysyydNm+`                          .yNmyo////////////////////////////omNy/////////////dMh.                                                   
                                                       `:oyhddhy+.                             `/hNmyo+////////////////////////+hMd+////////////oMN/                                                    
                                                           ````                                  `:ymNdyo++////////////////////sNNo////////////+mMy`                                                    
                                                                                                    .+dMMmdyso+++////////////+smNy////////////+hMd.                                                     
                                                                                                      sMNyhmNmmmhhyyssoooooosymNy+///////////+yNN:                                                      
                                                                                                     .yMh//++osyhhdmmmmmmmmmNMms+///////////+yNN/                                                       
                                                                                                     -dMy///////////+++++++ohho////////////+dMm:                                                        
                                                                                                     -mMs///////////////////+////////////+smMd-                                                         
                                                                                                     :NMs//////////////////////////////+odNMMs                                                          
                                                                                                     :NMo/////////////////////////////+dNNhNNo                                                          
                                                                                                     :mMs/+ooo++//////////////////////+hy+sNN/                                                          
                                                                                                     -dMddNNmmNmho////////////////////////hMMm/                                                         
                                                                                                     `sMMmso++ohNNs//////////////////////+dNdMm:                                                        
                                                                                                      +NMo/////+hMd///////////////////////+++dMs`                                                       
                                                                                                      :mMy/////+dMh///////////////////++////+hMy`                                                       
                                                                                                       /mNdysshmNdo////////////////+ohmdo///oNM+                                                        
                                                                                                        .+ydNMMNho+//////////++ooydmNmho+//+dMh.                                                        
                                                                                                          ``-+NMNmmdhyyyyyyhhdmNNmhyo+////+dMd-                                                         
                                                                                                             .NNhoshhhdddddmMNhNNs+/////+smMh.                                                          
                                                                                                            `hMd+////+++++odMy.omNhysosydNmo`                                                           
                                                                                                            :NNs/////////+hNm. `-ohmmmmdy+.                                                             
                                                                                                            -mNy+//////+odNd-     `....`                                                                
                                                                                                             oNNho+++oshNNs.                                                                            
                                                                                                              /hmmmmmmmdo-`                                                                             
                                                                                                               `.:/+/:.`                                                                                
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                          `.``                                                                          
                                                                                                             `..`       -sdddh+.               .:++/-    `-+syys:                                       
                                                                                                          .+hdmmmho-`  :NNhssmNd-            .ymmhhmNo   +mmysyNN+                                      
                                                                                                         +mNdyssydNmyysmMmso+odMh`           `//--/dMh   `:.-:oNN+                                      
                                                                                                     `-/sNNy+////+yMNdhdmmmmmmmMM/`            `sdmds-     -dmdy:`                                      
                                                                                                  .:sdNNMMd+//////+yy+///++ooshdNNho:`          -:-`        ..`                                         
                                                                                                -sdNmhsoNNy////////////////////+oshNNh+`            ./oss+.                                             
                                                 `-::.`                                       -ymNhs+//+mNy///////////////////////++ydNd+`         `sdhydNm.                                            
                                               `/dNNNms                                     `omNho+/////hMd+/////////////////////////+smNh:         `.-:sNN:                                            
                                               /mM+.sMN`                                   -yNmo+///////+ys+///////////////////////////+hNm/         :dmmy/                                             
                                               +my -dNs                                   -dMd+/////////////////////////////////////////+yNN/         ..`                                               
                                          ```  `.` .o+`                                  `dMd+///////////////////////////////////////////+yNm:                                                          
                                        :yddh+`      ```                                 sMNy+////////////////////////////////////////////+dMh`                                                         
                                       :MmooNN/    :ydddo.                              -mMMNhs+///////////////////////////////////////////oMN/                                                         
                                       hMy`+Nm:   -NNs:mMs`                             +NNdNMNmy///////////////////////////////////////////mMs`                                                        
                                       .:.`sd+    -h+`:NN+                              yMNsosdds+++++//////////////////////////////////////hMh.                                                        
                                                      oh+`                              hMMNs/+shdmmmmdyo///////////////////////////////////yMd.                                                        
                                                                                       .hMNs+smNmhsosshNNh+/////////////////////////////////yMh.                                                        
                                                                                     `+NMMm+yNNs+//////+hMmo////////////////////////////////dMy`                                                        
                                          ```                                        `sMMMNsdMy/////////+hMd+//////////////////////////////+MN+                                                         
                     `.-://:.``.-/+shdmNNNNNNNNmmhyo+:.``....`                       `yMdNNdNMo//////////+dMh+////////////////////////////+dMh.                                                         
                   .ohmNmmmmNddmNmmdhyyssssossssyyhmmNNmmNNNmdho-                    .mM++MNNMs///////////sNNo///////////////////////////+yNm:                                                          
                  /mNdso++++sdMNy+++//////////////++yNNdsooosydNNy.                  `sMh/mMMMh///////////+hNm+/////////////////////////+hNN:                                                           
                 /mMs+////////yNmo/////////////////sNNy///////+odMd-                  .omNmMMMNo///////////odMh+///////////////////////smNh-                                                            
                 oMN//////////+hNs+///////////////+yNy+/////////oMN+                    .:osmMMd+///////////omNy+///////////////////+sdNmo.                                                             
                 oMM+//////////+++/////////////////+++//////////oMMy.                       -yNMdo///////////omNh+///////////////+oydNmo.                                                               
                -hMMh+/////////////////////////////////////////+dMNNd:                       `:mMdo///////////odNds+/////////+oshdNMNo.                                                                 
               -dNdhy+/////////////////////////////////////////+yyohNN:                        .yNms+//////////+ymNho+++osyydmmmdhydMy`                                                                 
              .mNh+////////////////////////////////////////////////+yNm/                        `+mNho///////////oymNmmmmmmdhyo++//omMs                                                                 
             `hMd+//////////////////////////////////////////////////+hMd-                         -yNmyo///////////oyhyoo+++//+++///sNM:                                                                
             oNNo////////////////////////////////////////////////////+NMs`                         `:hNNho+//////////+///+osydmmmmhsodMd.````````                                                       
            -dMh//////////////////////////////////////////////////////yMm:                           -dMNmho+///////////ohmmdhysyhmNmdNNdhhhhhhhyso+/:.``                                               
            /NMo///////////////////////////////////////////////////+oydMMdo:`                        `sMmyhs+//////////omNho+oshdmNNmmdhhyyyyyyyhhdmmmmdyo//ooo/-.                                      
          `-yMM+//////////////////////////////////+//////////////+smNmhyhdmNd/`                       +NMo/////////////dMmyhmNmdyso++//////////////+++syNMNmdddmNmy:`                                   
         -hmNMN//////oyhhhhhhhhhyo+//////////+shhhhhhhhhhhs+/////hNms+////+yNN+`                      .hMh+///////////+mMNNdyo++//////////////////////+dNms+++++ohNNo                                   
        /mNhdMN/////+ymNNNNNNNNNNy+//////////+dNNNmNNNNNNNh+////oNms///////+yNN:                       +NNs/////////+ydNmyo+//////////////////////////hNd+///////+sNM:                                  
       -dMy/yNM+/////++oo++++o+o++////////////+++++++++++++/////yMd+////////+dMy                      ./mMNs+/////+smNds+/////////////////////////////syo/////////+dMy                                  
       +NM+/omMo//////////+syo////////////////////osso+////////+mNh/////////+hMm                    .odNmdNNy+///+hNms+///////////////////////////////////////////omMm/                                 
       oMM//+dMd/////////+mMMMo//////////////////oNMMNo////////+mNs//////////hMm                   :mNds+/odNmyosmNh+////////////////////////////////////////////+hNNNNo`                               
       oMM///sNNs////////+ymmd+//////////////////+hmmh+////////sNm+/////////+hMm                  /mNy+////+ohmNNMh+/////////////////////////////////////////////smmosNNo`                              
       +NM+///yNmo/////////+++////+++oyyso++++/////++/////////+dMd//////////+dMy                 `hMd/////////oNNh+//////////////////////////////////////////////+++//sNN+                              
       -dMy////hMmo////////////oydmmmNMMMMNmmmhs+/////////////sNMo//////////oNM/                 `yMm+//////+smMd+////////////////////////////////////////////////////+yNN.                             
        sNm+///+yNms//////////hNms/:/yNMMd+::+hNms///////////odMh//////////+yMd.                  .dMmhsoshdNMMNs//////////////////////////////////////////////////////+mMy                             
        .dMd+///+smMdo///////sMd.     .:.      +NN+/////////+dMh+//////////sNN/                     /ydmmmdyyNMd+///////////////////////////////////////////////////////hMm.                            
         -NNh+////+yNNds+////yMh.     -o+`     /NM+////////omNh+//////////+NNs`                        ``` -dMNy////////////////////////////////////////////////////+osshNN/                            
          :dNd+/////+ymNmyo+++dNdo:-:omNNy/--:smNy///////+yNNy+//////////omNy.                            `sMMNs/////////////////////////////////////////////////+sdmNmmmNNNy-                          
           .yNNs+/////+oymNNdysydmmmmdhoydmmmmmyo+/++osydNNdo//////////+smMs`                             -dMMNs////////////////////////////////////////////////+hNmy++//+ohNm:                         
            `/mNds+//////+oshdmNmmmdhyysssyyyyyyyhdmmNmdhso+//////////+hNN+                               :NMMNs////////////////////////////////////////////////yNmo///////+hMm`                        
              `omNms+////////++ooyhhdddmmmNNmmddhhyso+++////////////+yNNy-                                /MMMMh///////////////////////////////////////////////+NNy+////////omM/                        
                .+dNmho+///////////:-/++++/:/++++/:-://///////////ohmNh/`                                 :NMdMm+//////////////////////////////////////////////sMmo/////////+mMo                        
                  `:ymNdyo///////:.` `-/:.` `.-:-`  `.:////////+sdNmy/`                   `-/oys-         :mMyNNy/////////////////////////////////////////////+mNh//////////+mMo                        
                     ./yNms/////-`     `              `://////+hNmo-`                    `hNmhso-         .hMhyNmo////////////////////////////////////////////sNNo//////////omM/                        
                       `oMmo///:`                      .//////smM/                       :Mmo--::`        `oMNohNd+//////////////////////////////////////////+dMh///////////yNM.                        
                        `dMh+//-                       `//////yMM::::-`                  `smmddmh:         -dMy+hNmo/////////////////////////////////////////yNN+//////////+dMd                         
                         /Mmo//-                       `//////yMMmmmmmdo.                  .-:-.`           oNNo+yNms+//////////////////////////////////////omNy///////////sNN/                         
                         .mMy+/:`                      .//////sNMyo+osdNd-         ./oso.         ```       `hMd++smNds+///////////////////////////////////odNh+//////////+dMy`                         
                         `yMh+//-`                    .///////odNo////+dMs`       /mNhyo.       -ohdh-       .mMh+/+ymNdyo+///////////////////////////////omNh+///////////hMd-                          
                         :dMh+///:.`                `-/////////+o/////+hMy`      `yMd---//     :mNy+:`        -dMh+//+shNmdyo+//////////////////////////+smNh+//////////+yNm/                           
                       `+NNh+///////-..`````````..-://////////////////sNN+        :hmmmmdy`    :Nmo:/so.       -hNmo+//+osdmNmdyso+++++/////////+++++osymNms+//////////+yNm+                            
                      .yNms+////////////::::::///////////////////////omNy.         `.---.      `+hmmmho`        .sNmy+/////+oyhdmmmmmdhhyyyyyyhhhddmmmNmdy+///////////+hNm/                             
                     .hMmo////////////////////////////////////////++yNNs.                        ``.``           `/mNdo+oo/////++oosyyhhddddddhhhyysoo+++////////////odNd:                              
                    `yMdo///////////////++ossssyyyyyyyso+++////++oymNd/                                            .smNdMmo////////////////////////////////////////+yNNs.                               
                    /MNs//////////////+sdmmmNmddddddddmNmmhhhhhdmNmy/`                                              `-yNMmo//////////////////////////////////////+ymNh:`                                
                    sMd+/////////////odNd+-````````````-/osyyyyo+-`                                                    sMmo///////////////////////////////////+ohmNd/`                                  
                    sMd+///////////+yNNs`                                                                              yMd+////////////////////////////////+oydNNy:`                                    
                    :NNy+/////////+dNm/`                                                                               hMd+////////////////////////////////+dMNo.`                                      
                    `+NNho++//++ohNNs.                                                                                 mMd/////////++++////////////////////+hMmoyhhhs:`                                 
                      -sNNmmddmmNNy-                                                                                   dMd+/////+ydmmmmhs+/////////////////+mMMmdhyhmMd:                                
                        `:+osso/-`                                                                                     oMm+////smNdyosymNd+////////////////sMNs+////+hMd-                               
                                                                                                                       .NNh+//+dMy/////+dMy+///////////////oys+//////sMN:                               
                                                                                                                        /NNy+/+dMy/////+dMh+////////////////////////+dMh.                               
                                                                                                                      `:hNNNdo+sNNyooosdNdo///////////////////////+smMh-                                
                                                                                                                     -yNmysymNdyshmmmmmds+////////////////////+oshmNd+`                                 
                                                                                                                    .hMd+///+sdmmmhhyso++++/////////++++++oyhdmNmho:`                                   
                                                                                                                    :NMo///////+oyhmmmNNmmdddddhhdddddmmNNmdhs+:``                                      
                                                                                                                    -dMh+/////////++ymMmo+oossssssssoo+/:-.``                                           
                                                                                                                     /dNdyoo+++ooshmNms.                                                                
                                                                                                                      .+hmmNNNNNmmhs/.                                                                  
                                                                                                                        `.-:::::-.`                                                                     
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                         `..`                            :ss/`      .-.                                                 
                                                                                                   ``  `+hddds-                          :omNs`    .yNdo.                                               
                                                                                                -odddhsdNdyshNm+`                         .sMh.     .:MM+                                               
                                                                                            `.-omNdsydNMMdhhydMm/`                        -yy:       oMm/                                               
                                                                                        .-+ydmmNMh+//+hMMhhdmmNNmdy+-`                     `` ```    -/-                                                
                                                                                     ./ydNmdysyMmo////ohh////++osydmNds/`                    .ydh+`                                                     
                                                                                  `-smNmys++//oMmo/////+//////////++shmNdo-                  `-oNN+                                                     
                                                                                `:yNNho+//////oMmo////////////////////+sdNms.                  +Nm/                                                     
                                                                               `omNho/////////+NNy//////////////////////+sdNm/`                :o:                                                      
                                                                              -hNms+///////////syo////////////////////////+yNNo`                                                                        
                                            ````                             -dMd+//////////////////////////////////////////oNNs`                                                                       
                                          .+hddy/`                          .hMd+////////////////////////////////////////////sNN+                                                                       
                                          /dd+omN/                         `sMmo/////////////////////////////////////////////+yMN-                                                                      
                                           `   -:`                         -NMNmyo++//////////////////////////////////////////+dMy                                                                      
                                                                           sMmmNMNmhs//////////////////////////////////////////hMN                                                                      
                                      `-:-`     .:/:.`                     mMh++ydNNd+/////////////////////////////////////////sNM-                                                                     
                                    `omMNNm+`  /mMdNNy.                    NMhsdh++++/////oyhhdhys+////////////////////////////omM/                                                                     
                                    `/s:`/mh`  -+:`-yh.                   `NMhdMNs/////+smNmdhhhdNNd+//////////////////////////omM:                                                                     
                                                                        .smMMh+so/////+hNmo+/////+hNmo/////////////////////////yNM.                                                                     
                                                                        +NMMMd+///////sNNo////////+dMd+///////////////////////+hMm                                                                      
                                                                        /NMhNNs//////+hMh+/////////oMNs///////////////////////omM+                                                                      
                                                                       `sMd`sMh+/////+dMy+//////////dMh+/////////////////////+dMh.                                                                      
                                                                        oNN--dNy/////+hMh+//////////sMmo////////////////////+dMd-                                                                       
                                                                        .sNmyhNMy+///+yMd+//////////+mMy///////////////////odMd:                                                                        
                                                                         `-ohhdNNh+///omNs//////////+yMm+////////////////+smMy.       ``                                                                
                                                                            ```-hNmy+/+hMm+//////////+dMh+/////////////+ydNd/`  `-+ydmmmmho:` ```........```                                            
                                                              `...`             `/hNmyoomMh+//////////omNy+/////////+shmNh+.   .smNdhyssyhNNhyhdmmmmmmmmmddhyo+:...-:/:-.`                              
                                      ``--/+ossyyyyysso+::--ohddmddhs/`           `:ymNmmMNy+//////////smNy+///++oshmNms:`    -hMdo+/////+odMNhssssooossssyyddmNmdmmmmmmmh+.                            
                                 `.:+shmmmmmdddhhhhhdddmNNmNNdysssshmNd:             ./dMMNNy+//////////omNdyhhmmmmdmMd.      +Mmo/////////+mms//////////////+smMdyo+++oydNd:                           
                              `-+ydNmdhyoo++++/+////++++ohNNo+//////+hMd:             `yMdsmNh+//////////ohNMdhyso++omMs     `sMd+//////////+o+//////////////odMh+///////+hMd-                          
                           `.+dNMMMNmhso+///////////////+dMy/////////+MMo             `yMy:+hNms+/////////+os+///////yNN.   `+mMNo///////////////////////////+yy+/////////oMM/                          
                         `:smMNmdhyyhdmNh+//////////////+yh+/////////+MMs`            `yMh ./smNho///////////////////+mMy.`:hNmhho////////////////////////////////////////oMMo`                         
                        .yNMMms++////+ohNdo//////////////////////////sNNmo.            oMN` -/+hmh+//////////////////+dMMmdmNh+//////////////////////////////////////////+dMMNy`                        
                      `+mNNMmo/////////+hmy///////////////////////////+sdNd:           /mM- `://++////////////////////hMNmMms////////////////////////////////////////////yNdsdMh.                       
                     .yNmsyMd+//////////+++/////////////////////////////+yNNo`         .hMy` -///////////////////////+dMNNms/////////////////////////////////////////////+o+/+dMh.                      
                    .hMdo/sNNo////////////////////////////////////////////sNNy/:.`      /NN/`-//////////////////////+sNMMNs///////////////////////////////////////////////////+mMs`                     
                   `dMdo//+hNm+////////////////////////////////////////////sNMMNmdo.     oMm/://///////////////////oyNMMMh+////////////////////////////////////////////////////sNN/                     
                   sMmo////+sy+////////////////////////////////////////////+sNNssdNm/    oMMNy+//////////+////////oNMMMMNo/////////////////////////////////////////////////////+dMy`                    
                  :NNy//////////////////////////////////////////////////////+hMd/+yNN:  +NNydNms++////+o+//////////mMNMMd//////////////////////////////////////////////////////+yMN.                    
                  yMm+///////////////////////////////////////////////////////smMo/+dMd`-dMy/+sdNmdyyoohNd+////////yMmymMs///////////////////////////////////////////////////////sNM:                    
                 -dMy/////////////////////////////////////////////////+++oo//+dMh//yNm-+NM+///+oshmMNNNNMmo//////+mNyomMo/////////////////////////////////////////////////////+shNMdyo:`                
               `-oNMyso+/////////////////////////////////////////+osyhmmNMNo//hMm+/oNN/sMN///////+dMd-.-sMNy+////oNNoomMs///////////////////////////////////////////////////+ymNmhhhdmNm+               
             .omNMNmmNNmh+/////////////////////////////////////+hmNMMMNmdys+//yNm+/oNN/oMM+//////sNM/    /mNdo///sNN++mMy//////////////////////////////////////////////////+hNmo+////+smMo              
            /mMds+///+ohNNs+////////////////////++ooo+/////////+yhhyo+////////yNm+/sNm:-dMdo///+yNNo      .sNMho/oNNo/dMm+////////////////////////////////////////////////+yMmo////////yNm-             
           :NMy+////////sNNs//////////////+osyhdmNNMMy+/////////////ohds+/////hMm+/hMm` -yMNmddNNd/`        -yNNdhNNs/oNNo////////////////////////////////////////////////oNNs/////////oNN+             
          `hMh+//////////yMd+///////////+yNNMNNNmdhyo+/////////////+dMMmo////+dMh/omMs   `-+sss+-`            .+hmMMd++dMd+///////////////////////////////////////////////hMh+/////////oNN+             
          .NMy///////////omNs+///////////oyyyo++++/////////////////+ohys+////sNMo+yNN.                           `+MNs/+mNh+/////////////////////////////////////////////oMms//////////sNN/             
          .NMy///////////+yMd+////////////////+ydmh+////////////////////////+dNh/omMo                              hMd+/omNh+///////////////////////////////////////////+mNy+//////////hMm`             
          .mMy////////////omMs////////////////odNMmo///////+shhhyhhhhs+////+hMmo+dMh.                              -mMh+/odNdo/////////////////////////////////////////+dMd+//////////omM+              
          `yMh+///////////+yNm+////////////////oss+////+syhmMMMMNhsshmmy+/+hNmo+hMd-                                /mNh//+hNmy+//////////////////////////////////////odNd+//////////+hMd`              
           /NNo////////////omMy+/////////////////////+hmmhyyhNNd/`  `-mNyohNmo+hMd:              `--                `/mMy+/+odNmyo///////////////////////////////////odNd+//////////+yNm:               
           .yMd+////////////oNNy////////////////////+dMs.`  `..`      yMmmNh++hMd:              `oNm.                 :dMdo//+ohmNhso+/////////////////////////////+yNNy+//////////+yNm/                
            :mMy/////////////sNNs+//////////////////sNM.      -o/.``.+NMNds+odMd.               `sMm/-`                .hMms+//+oydmmdhso+/////////////////////+oshmNdo+//////////+hNm/`                
             /NNy+////////////sNNy+/////////////////odMo.```./dNNmmmNMNds++yNNs.                 .odmd:                 `+mNdo+///++shdmmmmhyysooooo+ooooosyyhmmNNmho+//////////+sdNh-                  
              +NNy+////////////sdNdo/////////////////ohNmhyymmmhymNNmho++sdNd/`            ```     `..`                   -smNho+/////++osyhdmmmmmmmmmmmmmmmdhysoo+////////////ohNNs`                   
               /mNh+////////////+hNmhsoo+++///////////+oshdddmmmmmhs+++sdNmo.             `sdo`      .:.                   `-smNdshho//////+++++ooooooooo++++////////////////oymNh:`                    
                :hNms+////////////odmmmmmmdhhyyyyyyyhhhmmmmmdhys++////yNmo.               .NMo.`    .mMs`                     -odNMNs/////////////////////////////////////+ohmNy:`                      
                 .omNho+///////////+++oosyyhhhdddddhhhhysso++:-://////dMy`                `omNmy    .mMy/-                      `+MNs//////////////////////////////////+oydNms:`                        
                   .ymNho+///////////////////++/:-////-``-::.`  .:////mMs`                  .:/-     :yddy`                      -MNs////////////////////////////////ohmNmy/.                           
                     :smNds++/////////////////:.` `.-`    ``     `:///MMo                              `.`                       :MNs////////////////////////////////dMNo-                              
                       .+dNmdso+/////////////:`                   .//+MMo                                                        .MNs////////++ooo++/////////////////mMMd/                              
                          -ohmNmy+///////////`                    `:/oMN/                                                         mMh+/////+ydmNNNmds+//////////////+mdhNN+`                            
                            `.dMd+///////////                     `:/yMd-                                                         +Mms////+hNdsoooymNh///////////////+++sNN/                            
                              +Mmo///////////                     -/+mMy`                                                         `yMms+//oNNo/////sNM+/////////////////+dMh`                           
                              .dMh+//////////`                   .//sNm:                                                           `omNho+omNy+///+yNN+////////+shs+/////yMd.                           
                               +NNo//////////:`                `-//omMs                                                              -mMNdhhNNdhhhmNms///+/+oshmNdo//////yMd.                           
                               `yMm+///////////-`          ``-:///smMy                                                              .sNmyhmNNMMMMMMmhyhdddmNNNMMo///////+mMy                            
                                .hMdo////////////::-...--:/ohdy++yNNs`                                                             .yMmo///+ossyhddNMNyyso+:-:dMh+/////+dMd.                            
                                 .yMms+////////////////+dNNNdyosdMd/`                                                              +MNo//////////+yNN/        -hNNhyssdNNh.                             
                                   +mNds+//////////////+hMmoshmNm+`                                                               `sMd+/////////+hMm/           :shdmdhs:`                              
                                    .+mMmyo/////////////odMNMms:`                                                                  /NNs///////+ymMh-               ```                                  
                                      `/hNNds+///////////yNM-                                                                      `+mNhsoosydNNd/`                                                     
                                        `-odNd+//////////omM/                                                                        -ohmmNmdho:`                                                       
                                           .hMd+/////////omM+                                                                          ``...``                                                          
                                            /Mmo/////////smM:                                                                                                                                           
                                            :Mmo////////+hMN`                                                                                                                                           
                                            .MNy///////+yNN/                                                                                                                                            
                                             yNmyo++++shNm+`                                                                                                                                            
                                             `/hmmmmmmNds-                                                                                                                                              
                                               `.-///:-`                                                                                                                                                
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                          .-`        `                                                                  
                                                                             `-::.`                                      .yNd:      :hh/`                                                               
                                                                           `omNmNmh:   `````                              .hMd`     .oNNo                                                               
                                                                           yMmsosdMmo/sdmmdy/.`                            oms       -mNo                                                               
                                                                         `-MMNddmNNNNNNdssymNmhyo:.`                       `.`       `::`                                                               
                                                                     `./ydmNddyssoo+mMd+///odMNdmNmds/.                       `/+:`                                                                     
                                                                   `/ymNdhso+//////+mms/////sNN++oshmNms:`                    .sNNs                                                                     
                                                                 `/dNmyo+///////////oo+/////omMo////+ohmNh/`                   `yMd`                                                                    
                                                                -hNmy+//////////////////////omMo///////+yNNy-                  `/s:                                                                     
                                                              `+mNh+////////////////////////+hh+/////////odNm/                                                                                          
                                                             `oNNs////////////////////////////////////////+yNN+                                                                                         
                                                            `+NNs//////////////////////////////////////////+yNN/                                                                                        
                                                            :NNy+///////////////////////////////////////////+hMd-                                                                                       
                                                            hMd+//+ss++//////////////////////////////////////+NMo                                                                                       
                                                           `MNy//+yNNNmhyo+///////////////////////////////////hMh.                                                                                      
                                                           /Mmo///+oydNNMMd///////////////////////////////////sMN:                                                                                      
                                                           +Mm+/////+++osso/////////+oyyyyys+/////////////////oMM:                                                                                      
                                       .shdh+`             oMm+////+hNd+//////////+ymNNdddmNNdo///////////////oMM/                                                                                      
                                       odhshm+             oMmo////+hNdo/////////omNdo+///++yNNs//////////////sMN:                                                                                      
                                        `  ``             +mMMms+///+o+/////////+mMh+///////+yNm+/////////////hMh.                       `-/osso+-                         .---`                        
                                                        `oNMMMMNNmhs+///////////yMdo/////////+mNy////////////oMN+                      :yNNNdhhdNNd+/+osyyhhhhhhyso+/-..+hNNNNNNmy/`                    
                                             ./oo/.     /NNoo+/-:+hNms//////////mMh+//////////mMd///////////+dMh.                     +NNho++//++yNMNmmdhhyyyyyyhdmmmNmmNmyo++oshmNd.                   
                                  `ohmdy/    mNddNd-   `oMh.      `+NN+/////////MMy///////////hMd+/////////odMd.                     -mNy+////////smNs++/////////++++yMNy+///////+dMd`                  
                                  `hyosdy`   ..``--     /NNys:     -dMo/////////MNy///////////sMd+///////+smNh.                      /NNo/////////+sds///////////////ohs+/////////oNN/                  
                                   ``  ``               `/dMMm+.``-yNm+/////////NMh///////////sMm+//////ohNmo`                       /NNy///////////+/////////////////+///////////sNN:                  
                                                          `-+hmmmmNNh+//////////hMh+//////////oMmo///+sdNms-                       .omNNmo///////////////////////////////////////omMm`                  
                                                             `-:/yNNhs+/////////sMmo//////////+NNyosdmNdo.                        :dNdsoo+//////////////////////////////////////+ymNNs.                 
                                                                 `:sdNmdys+++++/+dMy+//////////hMNNmNMy.                         /NNh+///////////////////////////////////////////++omNh-                
                                                                    `-oymNNmmdhhhdMNo//////////oNMh+yNm:                        /NNy+///////////////////////////////////////////////+dMh.               
                                                                       `sMMsysyhhdmNm+/////////+yNmo+dMh`                      :dMh+/////////////////////////////////////////////////omMy               
                                                                       `sMM--`.-//+dNd+/////////+hNh/smM/                     `yMm+///////////////////////////////////////////////////sNM/              
                                                    ``.-::///////:-..:shmNNddho:.:/+hNdo/////////+o+/+hMd`                    :NMs////////////////////////////////////////////////////+dMd`             
                                               `./oyhdmmmmmmmmmmmmmmmNmhsoooshmNo.-/+hNd+/////////////yNMh+.                 `oMm+/////////////////////////////////////////////////////sNm:             
                                           `-+ydNNmdyssoo+++++++++sdMd+///////omNo`://++//////////////sNMmNd:             `.:omMh+/////////////////////////////////////////////////////oNN+             
                                        `:odmNdyso+///////////////oNMs/////////yMh.-//////////////////yNN+dMh`           .odNmNMy+/////////////////////////////////////////////////////+mNy:/:.`        
                                      ./dNmhs++///////////////////ommo/////////hNNo//////////////////odMyodMy`          -dNdo+dMy+////////////////////////////////////////////////////+sNMNmmmNds-      
                                    .+dNdy+////////////////////////++//////////oyhNNho//////////////odMNhmNh-           yMdo/+hMh+///////////////////////////////////////////////////+hNmyo+++sdNm/     
                                   :dNms+//++oshhhso+/////////////////////////////ohNmy+//////////+smNNmdy/`            NMh//+yMm+//////////////////////////////////////////////////+yNmo//////+hMm`    
                                 `oMNy+//+ydNNmddmmNmyo/////////////////////////////omNho//////+oymNd+`                `MMy///omMy//////////////////////////////////////////////////sNNs////////sNM-    
                                .yMms///smNds++///+ohNNs/////////////////////////////+hNmo++oshmNNh/`                   mMh+//+yNN+////////////////////////////////////////////////+NNy+////////sNM-    
                               .yMm+///oNNy+////////+sdh//////////////////////////////+hNNNNmNNMm:                      oMmo///+dMd+//////////////////////////////////////////////+dMd+/////////yMN`    
                              `sMmo////yMd+////////////////////////////////////////////+dMmo+++mMy.                     .dMh+///+dNd+////////////////////////////////////////////+hNd+/////////+dMy     
                              /MNs/////yMm+/////////////////////////////////////////////omNy///oNN/                      /NNy////+dMmo+/////////////////////////////////////////odMm+//////////yMN-     
                              mMh+/////+NNh+/////////////////////////////////////////+ydhyMmo//oNM+                       /NMy+///+smNdo//////////////////////////////////////+yNNh+//////////sNN/      
                             :MNs///////odNh+/////////////////////////////////////+ohNMNdoMNy+smMh.                        /NNh+////oyNNds+/////////////////////////////////+sdNds+/////////+yNNo`      
                             oMmo////////+o+////////////////////////////////////+ymNMNho+/dMNNNdo.                          :mNdo/////+ymNmhs++//////////////////////////+oymNms+//////////+hNm/`       
                             yMd+//////////////////////////////////////////////oNMNdy+////yMMs-`                             .sNNh+/////+oydmNdhyoo++/////////////+++osyhmNNds+//////////+ymNh.         
                             hMd+//////////////////////////////////////////////+syo+oys+//yMMm.                               `:hNmy+//////+osydmNNmmmdhyyyyyyyhhdmmNNmdhyso+//////////+smNd/`          
                            `yMmo++/////////////////////////////////+++////////////smMNd+/hMMM+                  .-`            `:hNmho+///////+++oosyhhhhddddhhhhyso+++////////////+oymNd+`            
                          .+yNMMNNmdy+///////////////////////////+oydmh+///////////odNmy+/NMMMy                 :dN:              `:ymNdyo+/////////////+++++++//////////////////+oydNmy/`              
                         +mNmysooosdNmy+/////////////////////++oymNNNmy+////////////++++/oMNmMy                 /mMo-               `.+hmmdyo////////////////////////////////++oydNmh+.`                
                        oMNs+//////+odNh+//////////////////oydNNMNdyo+//////////+//++++/+dMddMs                 `/hdo                  `-+dMm+//////////////////////////////+ymNmy+-                    
                       :mNy//////////omMy/////////////////+dMNmhs+++/////////+shdddmmmmhhNmyNM:                   ```                     yMm+//////////////////////////////+sNNo`                      
                       oNN+///////////sNNs/////////////////+oo+//odmdo/////++hNMMMNo::+mMMshMd.            :hy       `+y:                 oNm+////////++oosoo+///////////////oNN/                       
                       oNm+///////////+yMdo//////////////////////hMMNy///+sdmmNMMm+`  `sMNoNN+            `sMm.      -dMs`                :mNy///////+hmmmmmmdy+/////////////sNN:                       
                       +NNo////////////+mNh+/////////////////////oyys+//odNh+--//.`   .yMdmMy`             :dNd/     `oNms.                yMm+/////+dNds++osmNh/////////////yNm.                       
                       .mNh/////////////omNy+//////////////////////////+hMh`     `:++odNmmMh.               `-:`       -+/`                .dNdo////oNNo/////yNN+///////////+dMd                        
                        oMmo/////////////smNh+/////////////////////////+hMo     `+NNmhyymMh.                                                -hNms+//+mNh++/+odMd///////+os+/+mMs                        
                        `hMdo/////////////odNdo/////////////////////////sNN+-.-/yNms++smNh.                                                  /NMNmhsosmNmddmmNho+++osyhmmm+/omM:                        
                         .dMdo/////////////+hNmy+///////////////////////+ymMNmmmdy+/+yNNs.                                                  `oMdsydmmmmNNNNNmdhhdmmmNdhyo+/+yMN`                        
                          -hNmo//////////////sdNmyo++++//////////++++oshdmNmhyo++/+ohNm+`                                                   `yMh+/++ooyyyhNMNhdMNhsoo+/////odMs                         
                           .sNmy+/////////////+sdNNmmddhhyyyyyyhdddmNNmdhs+://///+ymNy.                                                      +NNo///////+yNN+`hMd+////////+yMN-                         
                            `/mNdo//////////////+osssyhhhddddddhhysso////:` `-///sNN+`                                                       .yNNyo++++sdNm/`:mMo/////////omNo`                         
                              .sNNho+//////////////////////+///:///:. `..`    ./+hMh.                                                         `/hmNmmmNmdo.  /mMo////////omMy.                          
                                -yNNho+//////////////////////:.``..`           -+hMy`                                                            .:///:.`    .hMd+/////+smNy.                           
                                  -yNNds+////////////////////`                 `+dMs`                                                                         -hNmhysyhmNN+`                            
                                    .+dNNhs+////////////////`                  `+dMo`                                                                           :shdddhs/`                              
                                      `-smNmhs+/////////////                   -+NM+                                                                                `                                   
                                         `-yNMd+///////////:                  ./oNMo`                                                                                                                   
                                           -mNy/////////////                `.//+smMh`                                                                                                                  
                                            hMd+////////////-`            `.://///odMh`                                                                                                                 
                                            /MNs/////////////:.`      ``.-/////////oNNo                                                                                                                 
                                             hMdo///////////////::--:://oyy+///////+mMy                                                                                                                 
                                             .hMdo/////////////////++oydNmd+///////oNNo                                                                                                                 
                                              .yNmo/////////////ohdmmmmhs+////////+hMd.                                                                                                                 
                                               .hMd////////////+mMMNyo+//////////odNm:                                                                                                                  
                                                yMm+///////////sNNdNmyo+++++++osdNmy.                                                                                                                   
                                               .hMh///////////+dMh./ymNNmddddmNmho-`                                                                                                                    
                                               /NMo//////////+yNN-  `.-/++oo+/:.`                                                                                                                       
                                               oMM+/////////+sNN+                                                                                                                                       
                                               +NMo////////+yNNo`                                                                                                                                       
                                               `oNNho++++oymNd/`                                                                                                                                        
                                                `:ydmmmmmmmh/.                                                                                                                                          
                                                   .-://::.`                                                                                                                                            
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    #9
    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                             `---`                                                                                      
                                                                                                .:oss+-   `/ymmdmdo                                                                                     
                                                                                               +mmdyyNm:  .sho--sNM.                                                                                    
                                                                                               ./--:sMm:   ``:shmms                                                                                     
                                                                                                 -hmds:`     /so/-                                                                                      
                                                          .-/+/-`                                `--`   ```                                                                                             
                                                        -smNmmmNm+..--::::::---..`                   `:shddy/`                                                                                          
                                                       .hMdsooymMMmmmmmmmmNNNNmmmds+-`               `+yo/sNN/                                                                                          
                                                       :MNhdmmmmhyssoo+++yNNhsooshNMNdy+-`             `/odNm-                                                                                          
                                                      -sMNmdyo++////////omMs//////smMddNmh/.           .yhs+.                                                                                           
                                                   `-smNds+/////////////smd+///////dMm+oydNmo.          ``                                                                                              
                                                  .sNNho/////////////////+/////////hMm+///sdNm+`                                                                                                        
                                                 :mNdo+///////////////////////////+dMy/////+smMy.                                                                                                       
                                               `+NNy+/////////////////////////////+ss+///////odMd-                                                                  `-/+++/-`                           
                                               +NMs///////////////////////////////////////////+dMh.                                    .:+osss+-`   ```...-...````-odNmmmmmNmy:                         
                                              :mMh+////////////////////////////////////////////omMs`                                 -smNNddddNNdsyhdmmmmmmmmmmmdhmMdo+++++ohNN+                        
                                             `hMMdhs+///////////////////////////////////////////sNN-                                /mNho/////+smMNhyysooo+ooosyhMMy+////////sNN:                       
                                             -MMmNMms/////+so++/////////////////////////////////+dMy                               -dMh/////////+NNy////////////+hy+/////////+mNo                       
                                             oMmo+++/////+dMMNNdhhso+///////////////////////////+hMm                               :mMs//////////oyo/////////////////////////sNN+                       
                                             yMNdo////////+syhmmNMMNs////////////+osyddhys+//////hMM                              `+NMh/////////////////////////////////////omMMh:`                     
                                             hMMNs///////////++++oso+///////////odNNddhddNNho////hMM                             `hNNNNs////////////////////////////////////+sshNNs`                    
                                             yMdo///////////yNms+//////////////sMNy+/////+hNmo//+hMm                            /mNho+o+///////////////////////////////////////+odNm-                   
                                             +Mmo+oo++//////ymNy+/////////////omNy////////+hMh+/+dMs                           /mMy+/////////////////////////////////////////////+hNm:                  
                                            .yMNmNNNNds+////++++/////////////+dMd+/////////sMNo/yNN-                          /mMy////////////////////////////////////////////////+hMd:                 
                                           -dNy::hMMMMNmdyo+/////////////////omMs//////////oNMoomNo`                         .dMh+/////////////////////////////////////////////////+mMy.                
                                           sMm.  `/o+/:/omNh+////////////////yNN+//////////oNMsmMy.                          oMmo///////////////////////////////////////////////////oNN/                
                                           +Nm:`         -dMs///////////////+hMh///////////sMMNNy.                          `NMh+///////////////////////////////////////////////////+hMNy-              
                                           `sNmyss+`     .hMy///////////////omMs///////////yMMN+`                        `-/oMNy+///////////////////////////////////////////////////+yMMNNo`            
                                             -+yhdNdo/-:+hNd+///////////////sNNo//////////+hMm:                        .sdmmmmNNmh+//////////////////////////////////////////////////sMMyNN+`           
                                                 `/hNMNNNds+///////////////+yMd+//////////oNM+                       `+mNhs++++shNms+////////////////////////////////////////////////sNMoyMd-           
                                                   `oNMMNdys++/////////////+dMy+//////////sMm-                       :mMy+//////+sNNs////////////////////////////////////////////////sMNooMN/           
                                                    `/dMNmmNmmdhyssooooooooyNNs//////////+mMs`                      `yMd+/////////hMd+//////////////////////////////////////////////+yMd+oMM/           
                                                      .smNdyoyhhdmmmmmmmmmmNMmo//////////sMMo                       -dMy//////////oNNs//////////////////////////////////////////////+dMy+oMN:           
                                                        :dMy.-///:++++ooo++hNh+//+syddhsomMMs`                      -dMs//////////+hMh+/////////////////////////////////////////////sNmo/yMm-           
                               ```          ``          .hMo  ..``.::.-:///+o+//smNdhhdNNMNMh.                      .hMh///////////sNNo////////////////////////////////////////////oNNy+/mMy`           
                             .oyhyo.     `/syy+-`       `sMh       ````-+oossssyNNhoo++yNMdMm-                      `oNN+//////////+hNd+//////////////////////////////////////////omNy+/sMm/            
                            .dMhoymm/   `sNdoymNy.       +NM`  ``.:+yhdmmmmmmmmmmmmmmNmmNMNMN:                       -dMy///////////odMh+///////////////////////////////////////+smNy+/omNs`            
                            `dNs-`-/.   `oNd:`.os.       -dMo-/sdmNdhyssoooo++++++++ossyhdmNNh+:`                     +NNs///////////omNh+/////////////////////////////////////odNms//odMh`             
                             .hNmh-      `omNy-          `sNNmmdyo++//+ydmmmmho//////////++oydNNds-`                  `sMmo///////////omNdo/////////////////////////////////+ohNmy+/+odMd.              
                               .//`        .//`        .+dNNhs+//////omNds+ohNmo//////////////+shNNh/`                 `yMmo///////////+hNmy+///////////////////////////++oymNmy+//+sNNy`               
                                      ``             `+mNmy+////////+mNy+///+hmo/////////////////+ymNh/`                `sNms///////////+sdNmyo++///////////////////++oyhmNmhs+///ohMm+`                
                                    -sdmds:`       `:dMms+//////////yNm+/////++////////////////////+ymNh-                `oNNh+///////////+smNNNmdhysooooooooooosyhdmNNmdyo+////+hNNy-                  
                                   .NMy/omm:      `sNNy+///////////+dMd//////////////////////////////ohNN/                 -hMms+///////////+oyyyhddmmmNNNNNNNmmmddyys++//oyo+ohNNh:                    
                                   .NMy- `.      `hMms/////////////+dMd///////////////////////////////+yNN+                 `+mNds//////////////////+++++++++++++/////////NMmmNNs-`                     
                                    -smNh`      .dMdo///////////////hMm+////////////////////////////////sNN+                  `+dMmyo+////////////////////////////////////mMNh/`                        
                                      `-.      `yMm+////////////////odh+/////////////////////////////////yMm:                   `/hNNdy++/////////////////////////////////mMy`                          
                                               +NNo//////////////////+///////////////////////////////////+dMh`                    `.+hNNmhs+//////////////////////////////dMy`                          
                                              -dMy////////////////////////////////////////////////////////sNM/                        ./yMMd///////////////////+//////////mMs`                          
                                              +MNo////////////////////////////////////////////////+oo+////+dMh                        :sdMMy///////////////+ydmmdhs+/////+MM+                           
                                             `yMh+/////////////////////////////////////////////+ohmNNy/////hMN                      .hNmhhNN+/////////////sNNdysydNmo////yMd-                           
                                             .dMy+//////////////////////////////////////////+shmNMNds+/////yNM`                    `sMmo/+hNd+///////////+mNy+///+hMm//+sNN+                            
                                             .mMy+/////////////////////////////////////////+hNNNdso+///////sNM.                    .yMh///+so////////////+mNy+///+hMm+ohNMh`                            
                                             .dMy+/////////++///////////////////////////////oys+++oo+/////+yNM-                    `oNNo//////////////////sNNdysydNNhdmmdNN+`                           
                                             `hMh+/////+syddddhys+//////////////////////////////+hNNd+///odNMMh-                    .yNmyo++///////////++++sdNMMMMMNmdyo+yMm/                           
                                             `oMm+///+ymmdhyyyhdNmy+////////////////////////////+hNNh++shNMMMMMmo`                   `:ydmmmmdhhhhhhddmmmmmmNMMmdhso++////dMy`                          
                                              :mMy//+dNds+/////+odNh+////////////////////////////+oo+ymmyosdmhodNo`                     .-/+osssyysssoo+//:::yMmo////////+mMs`                          
                                              `sMm++hNd+/////////omMy+//////////////////////////////yNd:`  `.``oMm.                             ```          .yNmyo++//+ohMd:                           
                                               -dMhsNNo//////////+yMm+/////////////////////////////+NN+      :dmMh`                                           `/hmmdhhhmNms-                            
                                                :mNmMd+///////////oNNo/////////////////////////////+mNo`    `yMNh-                                              `-/osyso/-                              
                                                 :mMMh+///////////+dMy//////////////////////////////omNy/--/yNd/`                                                                                       
                                                  :mMh+///////////+hMd//////////////////////////////+sNMNdmmho.                                                                                         
                                                  `oMm+////////////sNM+///////////////////////////+ohNNs---.`                                                                                           
                                                   :NMs////////////+dMy////////////////////////++sdNmy-                                                                                                 
                                                   `yMm+////////////sNNo////////////////////+oshmNdo-                                                                                                   
                                                    :mMy////////////+dMd+///////////++++ooydmNNMm/`                                                                                                     
                                                     +NNy+///////////+NNdyysssssyyyhhdmmNNddysoMN/                                                                                                      
                                                      +MNs+///////////sNNmmmmmmmdddhhysso+/-:/-hMy`                                                                                                     
                                                       +NNy+///////////+o+////////////////.  ` /Mm-                                                                                                     
                                                       `/mNd+/////////////////////////.`..     .NM/                                                                                                     
                                                         -dMms+//////////////////////`         `yMo`                                                                                                    
                                                          yMMNho////////////////////-          `sMy`                                                                                                    
                                                         .hMdhds////////////////////.          `sMy`                                                                                                    
                                                       -smMMh///////////////////////`          `yMNyo/-`                                                                                                
                                                      /NNhmMd///////////////////////`          -NMdhmmNmho-`                                                                                            
                                                     .mNy+sNNo//////////////////////.          oMd++++osdNNh:                                                                                           
                                                     .mNy++mNh+//////////////////////`       `+Nms///////+yNN+                                                                                          
                                                      +NNhssNNy+//////////////////////-.```.:sNms/////////+hMd                                                                                          
                                                       -sdmmNNNho/+///////////////////////+smNdo//////////odMy                                                                                          
                                                         `.-:odMNdho///////////////////+oymNMNhssoo+++++oymNd-                                                                                          
                                                          -odmNNmdyo///////////odyoosydmNmysyhddmmmmmmmmmmho.                                                                                           
                                                        `omNhsoo++////////////+dMNmmmhyo:.    ``..--://:-.`                                                                                             
                                                        :NMy/////////////////+yNN+-..`                                                                                                                  
                                                        +MN+////////////////+hNN/                                                                                                                       
                                                        /NMs//////////////+ymNh:                                                                                                                        
                                                        `sNNy++/+////++oshmNd+.                                                                                                                         
                                                         `/hmmmdhyyhhdmmmds:`                                                                                                                           
                                                           `-/osyyyyyo+:-`                                                                                                                              
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    #10
    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                           .:/-`                                                                                                        
                                                                                  ``      `+dmNh:                                                                                                       
                                                                                `sdmh/`    `..hMh`                                                                                                      
                                                                                `:/oNN+       sh/                                                                                                       
                                                                                   -mm+       ``                                                                                                        
                                                                                    -.  `:/:.                                                          .:++o+/:.`                                       
                                                                                        /dmmd+`                                                      .smNmddmmmmy:`                                     
                                        ``----.`     ````````````                        `.sMm.                              `.-/++/:-````..--------/dMds+++++oyNNo`             :yy/`      ```         
                                      .+ydmmmmdy/:/+oyyhdddddddhyso+:-``                  `/h+`                            `:ymNNmdmNmhshddmmmmNNmmmNNNmhhyo++//sMN:             -smMs`    .ydy:`       
                                     :dNdysooymMNmmmdhhyyyssyyyyhmMMNNmhs/.                 `                             `oNNho++++oymMNhssoooooooooosyhdmmmdhssMM/              .hMh.    `:oMm/       
                                    .yMd++sdmNmhyo++//////////+sdNmhyyydmNNy/.                                            /NMo////////+dNy+////////////////+sydmNMM+`             :hy-       oMm/       
                                    .hMhhmNdyo+//////////////+yNNs+/////+odMMdo-                                          oMM//////////+so////////////////////++sdNNy:`               ``     +s:        
                                    `sMMmho+/////////////////+hms/////////+MMNNNo.                                       -hMMo///////////////////////////////////+oymNy-             :dds.              
                                   `oNNh+/////////////////////++//////////+MNysdMd:`                                    +mNmNd+/////////////////////////////////////+hNNo.           ./hMd`             
                                  .hMms+/////////////////////////////////+hMmo/+yNN+`                                 `sMNy+ss+//////////////////////////////////////+smMh`           -hNd`             
                                 -dMd+////////////////////////////////////sy+///+sNN+                                `yMmo/////////////////////////////////////////////+dMd.          .oo`              
                                .hMd+////////////////////////////////////////////+yNN:                              `oNNo///////////////////////////////////////////////+mMy`                           
                               `sMm+//////////////////////////////////////////////+dMd`                             :mMs/////////////////////////////////////////////////oMN+                           
                               :NMdso++////////////////////////////////////////////oNN/                            `yMd+//////////////////////////////////////////////////hMd-                          
                              `sMMMMNNmdy+/////////////////////////////////////////+mMy                            .NMy+//////////////////////////////////////////////////oMN/                          
                              .dMhoyhdmNd+////////sysoo+++//////////////////////++oodMh.                         `-sMMmdhyo+//////////////////////////////////////////////+mMo`                         
                              .NMy///++++////////+mMMNNNmddhys+///////////////oymNNmNMNdo.                      -yNNdyyyhmNms/////////////////////////////////////////////+dMs`                         
                              .NMy/oddy+//////////+osyhddmNNNdo/////////////+ymNhso++osdNm/                    -dMd++////+smNy////////////////////////////////////////////+dMs`                         
                              .mMy/sNNNo////////////++o+++++++//////////////sNmo///////+yNN/                  `yMd+////////sNNs///////////////////////////////////////////+mM+                          
                              `yMh++ooo+////////////smNdo//////////////////+dMy+////////+mMy`                 .NMy//////////hMd+//////////////////////////////////////////sMM/                          
                               /MNo/++++oyyo+///////odNdo//////////////////oNNs//////////yMd.                 :MNo//////////oMNs//////////////////////////////////////////dMN:                          
                               :mMdhdmmmNMMNmysso+///+++///////////////////yMd+//////////yMd.                 :MNs///////////dMh+////////////////////////////////////////sMMN:                          
                               -mMMNo:-/dNMNmhdmmdo+//////////////////////+NNy///////////hMh`                 .NMy///////////sNmo///////////////////////////////////////sNMMm:                          
                               -dMMy    `:/:.``./mNy//////////////////////oMmo//////////+mMs                  `yMd+//////////+hNd+////////////////////////////////////+ymNmMh.                          
                               `yMMm:`           +Md+////////////////////+dNh+//////////yNN:                   :mMs///////////odNd+//////////////////////////////////ohNmyNNo                           
                                /NMNmdyydh+.`  `-hNh+///////////////////+yNmo//////////omMs                    `oNNo///////////odNdo//////////////////////////////+oyNNhsdMh.                           
                                `sMNyyhmMMMmhsshmmy+///////////////////+yNmo//////////+hMm.                     .yNmo///////////+hNms+//////////////////////////osdmNhoodMd-                            
                                 .hMdo++sdNNMNmdyo+///////////////+++oymNmo//////////+yNN:  ./oss+-`             .yMmo///////////+ymNho+//////////////////+++oydmmdyo+smNd.                             
                                  `yMms+//+sydmmmmdhyyssssossssyyhdmmNmmy+//////////+hNm/ `omNmddNNy`             `yNms+///////////ohmNdhyssoooooooooossyhdmmmmhs+++odNmo`                              
                                   `omNh+////++osyhhddmNmmmmmNmddhhyso++///////////+hMm/  yMms+/+omMy`             `+mNdo////////////oymNmmmmmmmmmmmmmmmdhhyso+//+ydNms-                                
                                     :yNmyss+///:..://:-/+++///++////////////////+smNh-  :MNyossyymMNhysso+/:-.``    -sNNho+///////////+o+++++ooooooo+++++///////sMMo.                                  
                                      `:hNMMs//-`  `..  `--.``.:////////////////ohNms.-/smMNNNmddddddddmMMMNNMNmhs+:.` :hNNho+///////////////////////////////////sMM.                                   
                                        `/mMy/:`               `://///////////+yNNdyymNNdhsoo++++////+yNNhsooydNMNNNmh+-`:ymNdy++////////////////////////////////sMM-                                   
                                         `yMd/:                 `////////////+hMMNNNdyo+////////////+hNdo/////+yNNsoydmNdo-.+hmNmyo+/////////////////////////////sNM:                                   
                                          oMN+:                  ://////////+sNMNds++///////////////oNms+//////+hMh///+sdNNy:`-+hMNh/////////////////////////////omM:                                   
                                          :mMs:.                 ://///////ohNNho///////////////////+so+///////+hMd/////+oymNy-.sNNs///////////////////////+/////sNM-                                   
                                          `hMd/:`               .////////+yNNho////////////////////////////////+hMh////////+hNNmMNMd///////////////////+oydddhs+/yMN.                                   
                                           +NNo//-`            .////////odMdo//////////////////////////////////omMs//////////smMmyMmo/////////////////odNmhyhmNmshMy`                                   
                                           `hMd+////-..`````.-////////+smNh+//////////////////////////////////+yMh+///////////+dMddms/////////////////dMh+///+yNMMm:                                    
                                            -NNy+//////////+yhds+/////oNNy+////////////////////////////////////+s+/////////////+dMd+/+os+/////////////dMh+////yNMm/                                     
                                             +MNs///+o+//+ymNdy+/////+NNy+//////////////////////////////////////////////////////omNy/+hNNdyo+++///////omNmhyydNNy-                                      
                                             `oNNs/+hNmhsyNNo+//////+dMd+////////////////////////////////////////////////////////sMmo//+shmNNNmddddddddmNMNNNMN/                                        
                                              `oNNy++oydmMMh////////sNNo////////////////////////////////////////////////////////+hMMy+////oNMh+hMNdhhyyysso+smMh`                                       
                                                /dMdo+/+sNMo///////+dMh///////////////////////////////////////////////////////ohNMMMd+////sNN/ .dMd+/////////omMo                                       
                                                 .sNNhs/sMMo///////omMo//////////////////////////////////////////////////////+hNNdyMmsosshNNo`  -mNho////////+dMh                                       
                                                  `-smNdhNMs///////sNM+///////////////////////////////////////++//////////////+oo+yMMNmNmhs:     -hNmy++///++yNM+                                       
                                                     ./hmNMd+//////sNM+/////////////////////////////////+osyhhddhys++///////////+dNMMs:.``        `+hmNdhhhdmNd+                                        
                                                       `./hMmysooosdMM+///////////////////////////////+sdNmdhyyyhdmmho//////////omMMMNd:            `-/osyys+:.                                         
                                                          `/ydmmmmmdNMo//////////////////////////////+hNms++/////+ohNms+/////////+yMMMMh                                                                
                                                             `.---.-hMh/////////////////////////////+yNmo//////////+sNNs//////////yMmNMh`                                                               
                                                                    oNNo////////////////////////////+mMy+///////////+hMm/////////+NNo/mNo                                                               
                                                                    .dMd+///////////////////////////sMmo/////////////sNM+////////yMd. yMh`                                                              
                                                                     :NNy+//////////////////////////yMd+/////////////omMo///////omN+ -mMs                                                               
                                                                      +NNy+/////////////////////////mMh//////////////omMo//////odMd/smNs`                                                               
                                                                      `+mNy+///////////////////////+MNy//////////////yNM+/////odNNmmhs:                                                                 
                                                                        /dNdo+/////////////////////oMmo/////////////+hMm////+smNs..``                                                                   
                                                                         .oNNho+///////////////////yMd+/////////////+dMy//+sdNd/`                                                                       
                                                                           -yNNds++///////////////+mNy//////////////sNNo+ydNmo.                                                                         
                                                                             -odNmhs++////////////sNmo/////////////+hMmdNNh+.                                                                           
                                                                               `:odNNdhyso++/////+mMh//////////////sNMMMo-`                                                                             
                                                                                  /NMhdmNNmmdhhyyhNN+/////////////+mMmNM+                                                                               
                                                                                 `sMm///+osyyhdmNMNs//////////////yMd:yMd`                                                                              
                                                                                 -dMy//////////+dMh+/////////////yNm: :NN:                                                                              
                                                                                 /MNo//////////yNd+/////////////sNM/  .mNo                                                                              
                                                                                `sMd+//////////+++////////////+yNNo    mMy                                                                              
                                                                                `hMh+/////////////////////////+yhs.    yMh`                                                                             
                                                                               `:mMy//////////////////////////////.    yMh`                                                                             
                                                                             .+dNMMy+/////////////////////////////`   `mMh                                                                              
                                                                            .hMmsdMy+/////////////////////////////`   -mMN+`                                                                            
                                                                            +MNo+yMd+/////////////////////////////.  `sNNNNo`                                                                           
                                                                            /NNs/smNs/////////////////////////////: `+NNoyNN-                                                                           
                                                                            `oNNhydMNo//////////////////////////////yNmo/odMo                                                                           
                                                                             `-ohdmmMms+/////////////////////////+ymNho//+hMh                                                                           
                                                                                `...+mNdyso+////////////+////++shmNdo+///+hMh                                                                           
                                                                                     .+hNMm+//////////+ymyyyhdNMNho//////omMo                                                                           
                                                                                      .sNNy+//////////sNMmddyo+NMy+/////+hMd.                                                                           
                                                                                     /dNms+//////////odMy.``  `/mNdyssyhmNh-                                                                            
                                                                                    /NNy+///////////odMh.       .+ydmmdhs:`                                                                             
                                                                                   `dMd+//////////+smNy-          ``````                                                                                
                                                                                   `dMd+////////+sdNm+`                                                                                                 
                                                                                    :mNhs+++++oydNms.                                                                                                   
                                                                                     -sdmmmdmmmmy+.                                                                                                     
                                                                                       `-/++/:-`                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    #11
    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                               :so/.                                                     `.://:.`                                                       
                                                                               /hdNd-                                   ````            -ymmmmmmh/`                                                     
                                                                     `//-`      `-hm/                                ./shddhy+-........:mNho++oymNs`                      -/.                           
                                                                     :dmNd:       `.                               `omNmhyyydNNmmmmmmmmmMNdhyso+oMN/                      yNm/       ``                 
                                                                      `-yNy                                        sNms+////+smMdsoooosssyhhmmmmdMMs`                     -mMs`     +dh:                
                                                                        .:.  `:++-`                             `-oMNy////////sdy+/////////+++oshmNNh/.                   -hy-      .hMd.               
                                                                             `sdmNy.                          `/yNNMmo///////////////////////////+oydNmo-                  `        .dNs`               
                                                                              ``:Nm:                         -hNmyoNNy//////////////////////////////+odNmo.                  -/.     -:`                
                                                                                 ..                        .sNNy+//yNh+///////////////////////////////+odNd:                `sNN+                       
                                                                                                          -hMmo////+so+/////////////////////////////////+hNN+`               .dMy`                      
                                                                                                         -dMd+///////////////////////////////////////////+sNN+`              :dh-                       
                                `            ````````                                                   `dMd+//////////////////////////////////////////////yMm:                                         
                           `-+syhys/.`.-+osyhddmmmdddhys+/-````                                         oMmo///////////////////////////////////////////////+dMy`                                        
                         `omNNdhyhNMMNNNmmdhyyyyyyyyyyhdNMMMNNmdyo:`                                   .mMh/////////////////////////////////////////////////sMM-                                        
                         yMms++shmNmdys++//////////////smNmysssydmNd/                                  +NNo/////////////////////////////////////////////////omMo                                        
                        -MNsohNNmyo+//////////////////sNNy+//////+yNN+                                 sNm++syyyso+/////////////////////////////////////////+dMy                                        
                        -MNmNNyo//////////////////////hmy/////////+hMMo.                               yMNmNmmmmmNNho///////////////////////////////////////+hMh                                        
                        .MMNy+////////////////////////++//////////+hMNMm/`                             sMMds++/++oyMNs+/////////////////////////////////////+dMy                                        
                       /mNdo//////////////////////////////////////smNssmNs`                           `hMd+////////sNNs/////////////////////////////////////omMo                                        
                     `+mNy+///////////////////////////////////////oys++omMh`                          :mMs/////////+hMd+////////////////////////////////////yMN-                                        
                     /NNy///////////////////////////////////////////////omMy`                         +NM+//////////omNy///////////////////////////////////omMs`                                        
                    -mMy+////////////////////////////////////////////////sNN+                         /NMo//////////+yNN+/////////////////////////////////+dMh.                                         
                    hMd+/////////////////////////////////////////////////+hMh.                        -dMy///////////+mMy////////////////////////////////+dMd-                                          
                   -MNs///////////////////////////////////////////////////oMN/                         sNmo///////////sNNs/////////////////////////////+smNy.                                           
                   +Mmo//ohhhysssoo+///////////////////////////////////+ossMMy:.                       .dMh+///////////sNms+/////////////////////////+ohNmo`                                            
                   yMd+//ymNNNNNNNNd+/////////+syyysssoo+++///////////sdmmmmmmmms-                      :NNy+///////////yNNy+/////////////////////++sdNms-                                              
                   hMd+///++oossyyhs+/////////smNNNNMMNNNNmo////////+hNmyo++++ohNm/`                     /mNy+//////////+smNdo////////////////++oshmNdo-                                                
                  .mMd+///////+++/////////////++ooossyyyyhy+////////yNNo///////+hMm-                      /dNd+///////////ohNmyo////////+++osydmNmmNM+                                                  
                 `sMMmo//////omNms////////////////+oo+/////////////+dMy/////////+mMo`                      -hNms+//////////+odmmdhhhhhdmmmmNmdhys++hMd                                                  
                 -dMMNy//////omNms+//////////////+mNNd+////////////omMo/////////+hMy`                       .yMNdyso+/////////oyddhhhhhhysso++/////sNM-                                                 
                 /mMdMd+//////+++////+++++////////hmmh+////////////yNN+/////////+hMy`                     `:ymNmmmmNds+/////////++/////////////////+dMy                                                 
                 /NMsmMy+///////+osyyhmmmdsoo++////++/////////////+hMh//////////+dMo`                    `oNNyo++oodMNhyyyyyyssooo++////////////////yNm.                                                
                 :mMssmNy/////+ymmdhdNMMMMNmmmdy+/////////////////omMs//////////oNN/                     -NMhshdmmmmNNmddddmmNmmmmmdhhhyo+//////////oNN/                                                
                 `hMd+smNh+///hMh:```-sdh+-..:yNmo///////////////+hMd+//////////dMh.                  `.:hMMNmdhyso++++++++++++oyNNmmddmmmho+/////+++mNo                                                
                  /NNs/odNms+/NMs      `      `yMh///////////////sNms//////////sMm/                 `:sdNmhyo+////////////////+yNNy+///+ohNNds++shdmdNMs                                                
                  `yMmo/+smNdsyMm+.``-oy:`    .yMh//////////////sNNy+/////////omNs`               .+dNmhs+////////////////////sNNs///////+hNMNmNMdhyhmMd-                                               
                   `hMmo+/+sdNNmNNMmmNmmNho//smNd+///////////+ohNms//////////omMy`              .+mNds+//////////////////////+shs+////////oNNshNNho//+dMy`                                              
                    .yNms///+oydNNNmhso+shddddyo+///////++oshdNNmo//////////omMh`              /dMms+/////////////////////////////////////sNNo/ohNmy++dMy`                                              
                     `+mNdo////++sydNNNmddhhyssssssyyhhdmNNNddds+//////////sNNs`             `sNNy+//////////////////////////////////////+dMd////smNdmMd:                                               
                       .sNNho///////++osyhddmmmmmmmdddhyyoo+/////////////+hMm+`             .yMmo////////////////////////////////////////sNNo/////+dMMo`                                                
                         -yNNdo+//////:..:///-.:/+//-://///////////////+ymMh-              .yMm+/////////////////////////////////////////+so///////+dMd.                                                
                           .omMd+////.   `..    `-.   `-/////////////+ymNd/               `sMmo/////////////////////////////////////////////////////+mMy`                                               
                             -MNs///.                  `-//////////+ymMd/`                :NNs+//////////////////////////////////////////////////////oMN/                                               
                             `MNy///`                   `:////////omMh:`                  dMh+///////////////////////////////////////////////////////+mMy`                                              
                              NMh///`                   `-///////+hMd.                   -MNs/////////////////////////////////////////////////////////yMm-                                              
                              dMh+//`                   `-///////oNM+                    +Mmo/////////////////////////////////////////////////////////oMN:                                              
                              oMmo//:`                  .////////sMm-                    sMm+///////////////////////////////////////////+oyhhhhyo+////oMM/                                              
                              -NMy+//:.`              `.////////+mMy`                    sMd+/////////////////////////////////////////ohmmmhyyhmNds+//oMM/                                              
                             `yNNy+////:-.``      ``.-://///////yMm:                     sMm+///////////////////////////////////////+yNmyo++///+smNy+/oMN:                                              
                            `yMdo+//////////:::::://///////////sNN+                      /Mmo//////////////////////////////////////+hNmo/////////sNNs/yMm-                                              
                            /NNs////////++////////////////////+dMy`                      `NMy+/////////////////////////////////////sNNo//////////+hMh+mMy`                                              
                            +NNo///////ommmhyyyyssoo+/////////omMo                        sMmo////////////////////////////////////+dMy+//////////+yMdsMN/                                               
                            .mNh+//////+osyhhNMNmdNms/////////+hNm-                       .dMh+///////////////////////////////////sNmo///////////+yMmNMy`                                               
                             :mNho++/////++ohMm+..sMmo/////////+hMh-                       /mNy///////////////////////////////////dMh+///////////+hMNMd.                                                
                              -smNmhhyyyhdmNms-   `sNmy+////////+MMo                       `+mNy+////////////////////////////////+MNs////////////+mMMd.                                                 
                                ./oshhhhys+:.      `+mNds+/////+sMN/                        `/mNho///////////////////////////////yMm+////////////sMMy.                                                  
                                    ```              .odNmdysyydNm+`                          .yNmyo////////////////////////////omNy/////////////dMh.                                                   
                                                       `:oyhddhy+.                             `/hNmyo+////////////////////////+hMd+////////////oMN/                                                    
                                                           ````                                  `:ymNdyo++////////////////////sNNo////////////+mMy`                                                    
                                                                                                    .+dMMmdyso+++////////////+smNy////////////+hMd.                                                     
                                                                                                      sMNyhmNmmmhhyyssoooooosymNy+///////////+yNN:                                                      
                                                                                                     .yMh//++osyhhdmmmmmmmmmNMms+///////////+yNN/                                                       
                                                                                                     -dMy///////////+++++++ohho////////////+dMm:                                                        
                                                                                                     -mMs///////////////////+////////////+smMd-                                                         
                                                                                                     :NMs//////////////////////////////+odNMMs                                                          
                                                                                                     :NMo/////////////////////////////+dNNhNNo                                                          
                                                                                                     :mMs/+ooo++//////////////////////+hy+sNN/                                                          
                                                                                                     -dMddNNmmNmho////////////////////////hMMm/                                                         
                                                                                                     `sMMmso++ohNNs//////////////////////+dNdMm:                                                        
                                                                                                      +NMo/////+hMd///////////////////////+++dMs`                                                       
                                                                                                      :mMy/////+dMh///////////////////++////+hMy`                                                       
                                                                                                       /mNdysshmNdo////////////////+ohmdo///oNM+                                                        
                                                                                                        .+ydNMMNho+//////////++ooydmNmho+//+dMh.                                                        
                                                                                                          ``-+NMNmmdhyyyyyyhhdmNNmhyo+////+dMd-                                                         
                                                                                                             .NNhoshhhdddddmMNhNNs+/////+smMh.                                                          
                                                                                                            `hMd+////+++++odMy.omNhysosydNmo`                                                           
                                                                                                            :NNs/////////+hNm. `-ohmmmmdy+.                                                             
                                                                                                            -mNy+//////+odNd-     `....`                                                                
                                                                                                             oNNho+++oshNNs.                                                                            
                                                                                                              /hmmmmmmmdo-`                                                                             
                                                                                                               `.:/+/:.`                                                                                
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

    #12
    tmp = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                          `.``                                                                          
                                                                                                             `..`       -sdddh+.               .:++/-    `-+syys:                                       
                                                                                                          .+hdmmmho-`  :NNhssmNd-            .ymmhhmNo   +mmysyNN+                                      
                                                                                                         +mNdyssydNmyysmMmso+odMh`           `//--/dMh   `:.-:oNN+                                      
                                                                                                     `-/sNNy+////+yMNdhdmmmmmmmMM/`            `sdmds-     -dmdy:`                                      
                                                                                                  .:sdNNMMd+//////+yy+///++ooshdNNho:`          -:-`        ..`                                         
                                                                                                -sdNmhsoNNy////////////////////+oshNNh+`            ./oss+.                                             
                                                 `-::.`                                       -ymNhs+//+mNy///////////////////////++ydNd+`         `sdhydNm.                                            
                                               `/dNNNms                                     `omNho+/////hMd+/////////////////////////+smNh:         `.-:sNN:                                            
                                               /mM+.sMN`                                   -yNmo+///////+ys+///////////////////////////+hNm/         :dmmy/                                             
                                               +my -dNs                                   -dMd+/////////////////////////////////////////+yNN/         ..`                                               
                                          ```  `.` .o+`                                  `dMd+///////////////////////////////////////////+yNm:                                                          
                                        :yddh+`      ```                                 sMNy+////////////////////////////////////////////+dMh`                                                         
                                       :MmooNN/    :ydddo.                              -mMMNhs+///////////////////////////////////////////oMN/                                                         
                                       hMy`+Nm:   -NNs:mMs`                             +NNdNMNmy///////////////////////////////////////////mMs`                                                        
                                       .:.`sd+    -h+`:NN+                              yMNsosdds+++++//////////////////////////////////////hMh.                                                        
                                                      oh+`                              hMMNs/+shdmmmmdyo///////////////////////////////////yMd.                                                        
                                                                                       .hMNs+smNmhsosshNNh+/////////////////////////////////yMh.                                                        
                                                                                     `+NMMm+yNNs+//////+hMmo////////////////////////////////dMy`                                                        
                                          ```                                        `sMMMNsdMy/////////+hMd+//////////////////////////////+MN+                                                         
                     `.-://:.``.-/+shdmNNNNNNNNmmhyo+:.``....`                       `yMdNNdNMo//////////+dMh+////////////////////////////+dMh.                                                         
                   .ohmNmmmmNddmNmmdhyyssssossssyyhmmNNmmNNNmdho-                    .mM++MNNMs///////////sNNo///////////////////////////+yNm:                                                          
                  /mNdso++++sdMNy+++//////////////++yNNdsooosydNNy.                  `sMh/mMMMh///////////+hNm+/////////////////////////+hNN:                                                           
                 /mMs+////////yNmo/////////////////sNNy///////+odMd-                  .omNmMMMNo///////////odMh+///////////////////////smNh-                                                            
                 oMN//////////+hNs+///////////////+yNy+/////////oMN+                    .:osmMMd+///////////omNy+///////////////////+sdNmo.                                                             
                 oMM+//////////+++/////////////////+++//////////oMMy.                       -yNMdo///////////omNh+///////////////+oydNmo.                                                               
                -hMMh+/////////////////////////////////////////+dMNNd:                       `:mMdo///////////odNds+/////////+oshdNMNo.                                                                 
               -dNdhy+/////////////////////////////////////////+yyohNN:                        .yNms+//////////+ymNho+++osyydmmmdhydMy`                                                                 
              .mNh+////////////////////////////////////////////////+yNm/                        `+mNho///////////oymNmmmmmmdhyo++//omMs                                                                 
             `hMd+//////////////////////////////////////////////////+hMd-                         -yNmyo///////////oyhyoo+++//+++///sNM:                                                                
             oNNo////////////////////////////////////////////////////+NMs`                         `:hNNho+//////////+///+osydmmmmhsodMd.````````                                                       
            -dMh//////////////////////////////////////////////////////yMm:                           -dMNmho+///////////ohmmdhysyhmNmdNNdhhhhhhhyso+/:.``                                               
            /NMo///////////////////////////////////////////////////+oydMMdo:`                        `sMmyhs+//////////omNho+oshdmNNmmdhhyyyyyyyhhdmmmmdyo//ooo/-.                                      
          `-yMM+//////////////////////////////////+//////////////+smNmhyhdmNd/`                       +NMo/////////////dMmyhmNmdyso++//////////////+++syNMNmdddmNmy:`                                   
         -hmNMN//////oyhhhhhhhhhyo+//////////+shhhhhhhhhhhs+/////hNms+////+yNN+`                      .hMh+///////////+mMNNdyo++//////////////////////+dNms+++++ohNNo                                   
        /mNhdMN/////+ymNNNNNNNNNNy+//////////+dNNNmNNNNNNNh+////oNms///////+yNN:                       +NNs/////////+ydNmyo+//////////////////////////hNd+///////+sNM:                                  
       -dMy/yNM+/////++oo++++o+o++////////////+++++++++++++/////yMd+////////+dMy                      ./mMNs+/////+smNds+/////////////////////////////syo/////////+dMy                                  
       +NM+/omMo//////////+syo////////////////////osso+////////+mNh/////////+hMm                    .odNmdNNy+///+hNms+///////////////////////////////////////////omMm/                                 
       oMM//+dMd/////////+mMMMo//////////////////oNMMNo////////+mNs//////////hMm                   :mNds+/odNmyosmNh+////////////////////////////////////////////+hNNNNo`                               
       oMM///sNNs////////+ymmd+//////////////////+hmmh+////////sNm+/////////+hMm                  /mNy+////+ohmNNMh+/////////////////////////////////////////////smmosNNo`                              
       +NM+///yNmo/////////+++////+++oyyso++++/////++/////////+dMd//////////+dMy                 `hMd/////////oNNh+//////////////////////////////////////////////+++//sNN+                              
       -dMy////hMmo////////////oydmmmNMMMMNmmmhs+/////////////sNMo//////////oNM/                 `yMm+//////+smMd+////////////////////////////////////////////////////+yNN.                             
        sNm+///+yNms//////////hNms/:/yNMMd+::+hNms///////////odMh//////////+yMd.                  .dMmhsoshdNMMNs//////////////////////////////////////////////////////+mMy                             
        .dMd+///+smMdo///////sMd.     .:.      +NN+/////////+dMh+//////////sNN/                     /ydmmmdyyNMd+///////////////////////////////////////////////////////hMm.                            
         -NNh+////+yNNds+////yMh.     -o+`     /NM+////////omNh+//////////+NNs`                        ``` -dMNy////////////////////////////////////////////////////+osshNN/                            
          :dNd+/////+ymNmyo+++dNdo:-:omNNy/--:smNy///////+yNNy+//////////omNy.                            `sMMNs/////////////////////////////////////////////////+sdmNmmmNNNy-                          
           .yNNs+/////+oymNNdysydmmmmdhoydmmmmmyo+/++osydNNdo//////////+smMs`                             -dMMNs////////////////////////////////////////////////+hNmy++//+ohNm:                         
            `/mNds+//////+oshdmNmmmdhyysssyyyyyyyhdmmNmdhso+//////////+hNN+                               :NMMNs////////////////////////////////////////////////yNmo///////+hMm`                        
              `omNms+////////++ooyhhdddmmmNNmmddhhyso+++////////////+yNNy-                                /MMMMh///////////////////////////////////////////////+NNy+////////omM/                        
                .+dNmho+///////////:-/++++/:/++++/:-://///////////ohmNh/`                                 :NMdMm+//////////////////////////////////////////////sMmo/////////+mMo                        
                  `:ymNdyo///////:.` `-/:.` `.-:-`  `.:////////+sdNmy/`                   `-/oys-         :mMyNNy/////////////////////////////////////////////+mNh//////////+mMo                        
                     ./yNms/////-`     `              `://////+hNmo-`                    `hNmhso-         .hMhyNmo////////////////////////////////////////////sNNo//////////omM/                        
                       `oMmo///:`                      .//////smM/                       :Mmo--::`        `oMNohNd+//////////////////////////////////////////+dMh///////////yNM.                        
                        `dMh+//-                       `//////yMM::::-`                  `smmddmh:         -dMy+hNmo/////////////////////////////////////////yNN+//////////+dMd                         
                         /Mmo//-                       `//////yMMmmmmmdo.                  .-:-.`           oNNo+yNms+//////////////////////////////////////omNy///////////sNN/                         
                         .mMy+/:`                      .//////sNMyo+osdNd-         ./oso.         ```       `hMd++smNds+///////////////////////////////////odNh+//////////+dMy`                         
                         `yMh+//-`                    .///////odNo////+dMs`       /mNhyo.       -ohdh-       .mMh+/+ymNdyo+///////////////////////////////omNh+///////////hMd-                          
                         :dMh+///:.`                `-/////////+o/////+hMy`      `yMd---//     :mNy+:`        -dMh+//+shNmdyo+//////////////////////////+smNh+//////////+yNm/                           
                       `+NNh+///////-..`````````..-://////////////////sNN+        :hmmmmdy`    :Nmo:/so.       -hNmo+//+osdmNmdyso+++++/////////+++++osymNms+//////////+yNm+                            
                      .yNms+////////////::::::///////////////////////omNy.         `.---.      `+hmmmho`        .sNmy+/////+oyhdmmmmmdhhyyyyyyhhhddmmmNmdy+///////////+hNm/                             
                     .hMmo////////////////////////////////////////++yNNs.                        ``.``           `/mNdo+oo/////++oosyyhhddddddhhhyysoo+++////////////odNd:                              
                    `yMdo///////////////++ossssyyyyyyyso+++////++oymNd/                                            .smNdMmo////////////////////////////////////////+yNNs.                               
                    /MNs//////////////+sdmmmNmddddddddmNmmhhhhhdmNmy/`                                              `-yNMmo//////////////////////////////////////+ymNh:`                                
                    sMd+/////////////odNd+-````````````-/osyyyyo+-`                                                    sMmo///////////////////////////////////+ohmNd/`                                  
                    sMd+///////////+yNNs`                                                                              yMd+////////////////////////////////+oydNNy:`                                    
                    :NNy+/////////+dNm/`                                                                               hMd+////////////////////////////////+dMNo.`                                      
                    `+NNho++//++ohNNs.                                                                                 mMd/////////++++////////////////////+hMmoyhhhs:`                                 
                      -sNNmmddmmNNy-                                                                                   dMd+/////+ydmmmmhs+/////////////////+mMMmdhyhmMd:                                
                        `:+osso/-`                                                                                     oMm+////smNdyosymNd+////////////////sMNs+////+hMd-                               
                                                                                                                       .NNh+//+dMy/////+dMy+///////////////oys+//////sMN:                               
                                                                                                                        /NNy+/+dMy/////+dMh+////////////////////////+dMh.                               
                                                                                                                      `:hNNNdo+sNNyooosdNdo///////////////////////+smMh-                                
                                                                                                                     -yNmysymNdyshmmmmmds+////////////////////+oshmNd+`                                 
                                                                                                                    .hMd+///+sdmmmhhyso++++/////////++++++oyhdmNmho:`                                   
                                                                                                                    :NMo///////+oyhmmmNNmmdddddhhdddddmmNNmdhs+:``                                      
                                                                                                                    -dMh+/////////++ymMmo+oossssssssoo+/:-.``                                           
                                                                                                                     /dNdyoo+++ooshmNms.                                                                
                                                                                                                      .+hmmNNNNNmmhs/.                                                                  
                                                                                                                        `.-:::::-.`                                                                     
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        

    '''
    tmp = crop(tmp)
    strs.append(tmp)

import time
iter = 0

append()
endpoints = int(len(strs[0]) / line)
while True:
    for i in range(12): 
        print(strs[i])
        time.sleep(0.1)
# while True:
#     #0~200
#     print(strs[0][iter * line : (iter+1) * line], end='')
#     time.sleep(0.01)
#     if(iter > endpoints-13):
#         break
#     iter += 1
#     iter = (iter + 1) % endpoints

