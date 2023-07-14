
from pymol.cgo import *
from pymol import cmd
import numpy as np
from chempy.brick import Brick

        

RegularData_0_data = np.array([[[0,1],
  [1,2]],

 [[1,2],
  [2,3]]])
RegularData_0 = Brick.from_numpy(RegularData_0_data, [1.,1.,1.], origin=[0,0,0])
cmd.load_brick(RegularData_0, "RegularData_0")


RegularData_2_data = np.array([[[0,1],
  [0,1]],

 [[0,1],
  [0,1]]])
RegularData_2 = Brick.from_numpy(RegularData_2_data, [1.,1.,1.], origin=[0,0,0])
cmd.load_brick(RegularData_2, "RegularData_2")

cmd.ramp_new("ColorRamp_1", "RegularData_2", range = [0.0,0.010101010101010102,0.020202020202020204,0.030303030303030304,0.04040404040404041,0.05050505050505051,0.06060606060606061,0.07070707070707072,0.08080808080808081,0.09090909090909091,0.10101010101010102,0.11111111111111112,0.12121212121212122,0.13131313131313133,0.14141414141414144,0.15151515151515152,0.16161616161616163,0.17171717171717174,0.18181818181818182,0.19191919191919193,0.20202020202020204,0.21212121212121213,0.22222222222222224,0.23232323232323235,0.24242424242424243,0.25252525252525254,0.26262626262626265,0.27272727272727276,0.2828282828282829,0.29292929292929293,0.30303030303030304,0.31313131313131315,0.32323232323232326,0.33333333333333337,0.3434343434343435,0.3535353535353536,0.36363636363636365,0.37373737373737376,0.38383838383838387,0.393939393939394,0.4040404040404041,0.4141414141414142,0.42424242424242425,0.43434343434343436,0.4444444444444445,0.4545454545454546,0.4646464646464647,0.4747474747474748,0.48484848484848486,0.494949494949495,0.5050505050505051,0.5151515151515152,0.5252525252525253,0.5353535353535354,0.5454545454545455,0.5555555555555556,0.5656565656565657,0.5757575757575758,0.5858585858585859,0.595959595959596,0.6060606060606061,0.6161616161616162,0.6262626262626263,0.6363636363636365,0.6464646464646465,0.6565656565656566,0.6666666666666667,0.6767676767676768,0.686868686868687,0.696969696969697,0.7070707070707072,0.7171717171717172,0.7272727272727273,0.7373737373737375,0.7474747474747475,0.7575757575757577,0.7676767676767677,0.7777777777777778,0.787878787878788,0.797979797979798,0.8080808080808082,0.8181818181818182,0.8282828282828284,0.8383838383838385,0.8484848484848485,0.8585858585858587,0.8686868686868687,0.8787878787878789,0.888888888888889,0.8989898989898991,0.9090909090909092,0.9191919191919192,0.9292929292929294,0.9393939393939394,0.9494949494949496,0.9595959595959597,0.9696969696969697,0.9797979797979799,0.98989898989899,1.0], color = [[0.19215686274509805, 0.21176470588235294, 0.5843137254901961], [0.19830834294502114, 0.23114186851211072, 0.5938485198000769], [0.20753556324490582, 0.2602076124567474, 0.6081507112648982], [0.21368704344482892, 0.2795847750865052, 0.617685505574779], [0.22291426374471357, 0.3086505190311419, 0.6319876970396002], [0.2290657439446367, 0.3280276816608997, 0.641522491349481], [0.23829296424452134, 0.35709342560553636, 0.6558246828143023], [0.247520184544406, 0.38615916955017304, 0.6701268742791234], [0.2536716647443291, 0.4055363321799308, 0.6796616685890043], [0.26289888504421377, 0.4346020761245675, 0.6939638600538255], [0.2690503652441369, 0.45397923875432533, 0.7034986543637063], [0.28865820838139183, 0.48035371011149564, 0.7170319108035371], [0.31034217608612075, 0.5061899269511727, 0.7304113802383699], [0.32479815455594, 0.5234140715109573, 0.7393310265282584], [0.34648212226066905, 0.5492502883506345, 0.7527104959630911], [0.3609381007304883, 0.5664744329104192, 0.7616301422529796], [0.38262206843521723, 0.5923106497500962, 0.7750096116878125], [0.39707804690503656, 0.6095347943098809, 0.783929257977701], [0.4187620146097656, 0.635371011149558, 0.7973087274125337], [0.4404459823144945, 0.661207227989235, 0.8106881968473664], [0.45490196078431383, 0.6784313725490198, 0.8196078431372549], [0.4802768166089966, 0.6987312572087659, 0.8306805074971165], [0.4971933871587852, 0.7122645136485968, 0.8380622837370243], [0.5225682429834679, 0.7325643983083431, 0.8491349480968858], [0.5479430988081508, 0.7528642829680893, 0.8602076124567475], [0.5648596693579393, 0.7663975394079201, 0.8675893886966551], [0.5902345251826222, 0.7866974240676664, 0.8786620530565168], [0.6071510957324107, 0.8002306805074972, 0.8860438292964244], [0.6325259515570935, 0.8205305651672434, 0.8971164936562861], [0.6494425221068819, 0.8340638216070742, 0.9044982698961938], [0.6746635909265668, 0.8529796232218377, 0.914878892733564], [0.6991157247212612, 0.8649750096116878, 0.9217993079584775], [0.7154171472510573, 0.8729719338715878, 0.9264129181084199], [0.7398692810457518, 0.884967320261438, 0.9333333333333333], [0.756170703575548, 0.8929642445213379, 0.9379469434832757], [0.7806228373702423, 0.904959630911188, 0.9448673587081892], [0.8050749711649368, 0.9169550173010381, 0.9517877739331027], [0.8213763936947329, 0.9249519415609382, 0.956401384083045], [0.8458285274894273, 0.9369473279507882, 0.9633217993079585], [0.8621299500192235, 0.9449442522106882, 0.9679354094579009], [0.8831987697039602, 0.9547866205305652, 0.9637831603229524], [0.8975009611687813, 0.960322952710496, 0.9374855824682813], [0.9070357554786621, 0.9640138408304498, 0.9199538638985004], [0.9213379469434834, 0.9695501730103806, 0.8936562860438291], [0.9308727412533642, 0.9732410611303345, 0.8761245674740483], [0.9451749327181853, 0.9787773933102653, 0.8498269896193771], [0.9547097270280662, 0.9824682814302191, 0.8322952710495962], [0.9690119184928874, 0.9880046136101499, 0.805997693194925], [0.9833141099577086, 0.9935409457900808, 0.7797001153402537], [0.9928489042675894, 0.9972318339100346, 0.7621683967704729], [0.9997693194925029, 0.9928489042675894, 0.7381776239907728], [0.9994617454825068, 0.9833141099577085, 0.7237216455209535], [0.9990003844675125, 0.9690119184928874, 0.7020376778162245], [0.9985390234525182, 0.9547097270280661, 0.6803537101114956], [0.9982314494425221, 0.9451749327181853, 0.6658977316416763], [0.9977700884275279, 0.930872741253364, 0.6442137639369473], [0.9974625144175318, 0.9213379469434833, 0.629757785467128], [0.9970011534025375, 0.9070357554786621, 0.6080738177623991], [0.9966935793925413, 0.8975009611687812, 0.5936178392925797], [0.9962322183775472, 0.88319876970396, 0.5719338715878508], [0.9957708573625529, 0.8630526720492119, 0.5502499038831219], [0.9954632833525567, 0.847673971549404, 0.5357939254133026], [0.9950019223375625, 0.8246059207996924, 0.5141099577085736], [0.9946943483275663, 0.8092272202998847, 0.4996539792387543], [0.9942329873125721, 0.7861591695501731, 0.47797001153402535], [0.9937716262975779, 0.7630911188004613, 0.4562860438292964], [0.9934640522875817, 0.7477124183006536, 0.4418300653594771], [0.9930026912725874, 0.724644367550942, 0.4201460976547482], [0.9926951172625913, 0.7092656670511341, 0.4056901191849288], [0.9922337562475971, 0.6861976163014225, 0.3840061514801999], [0.9886966551326413, 0.657362552864283, 0.36885813148788926], [0.9859284890426759, 0.6373702422145329, 0.3596309111880046], [0.9817762399077278, 0.6073817762399077, 0.34579008073817763], [0.9790080738177624, 0.5873894655901576, 0.336562860438293], [0.9748558246828143, 0.5574009996155325, 0.322722029988466], [0.972087658592849, 0.5374086889657824, 0.31349480968858134], [0.9679354094579009, 0.5074202229911575, 0.2996539792387545], [0.9637831603229527, 0.47743175701653207, 0.28581314878892733], [0.9610149942329873, 0.457439446366782, 0.2765859284890427], [0.9568627450980393, 0.42745098039215684, 0.2627450980392157], [0.9479430988081508, 0.4086889657823914, 0.25413302575932334], [0.9345636293733179, 0.38054594386774315, 0.24121491733948483], [0.9211841599384853, 0.3524029219530952, 0.22829680891964643], [0.9122645136485967, 0.33364090734332946, 0.21968473663975396], [0.8988850442137639, 0.3054978854286813, 0.20676662821991543], [0.8899653979238754, 0.28673587081891583, 0.19815455594002307], [0.8765859284890427, 0.2585928489042676, 0.18523644752018453], [0.8676662821991542, 0.2398308342945021, 0.1766243752402922], [0.8542868127643214, 0.2116878123798539, 0.1637062668204537], [0.8392925797770089, 0.1845444059976932, 0.1528642829680892], [0.8239138792772011, 0.16978085351787775, 0.15255670895809306], [0.8008458285274894, 0.14763552479815456, 0.1520953479430988], [0.7854671280276817, 0.13287197231833908, 0.15178777393310267], [0.7623990772779701, 0.11072664359861592, 0.15132641291810842], [0.7393310265282584, 0.08858131487889273, 0.1508650519031142], [0.7239523260284506, 0.07381776239907728, 0.15055747789311805], [0.700884275278739, 0.05167243367935409, 0.1500961168781238], [0.6855055747789311, 0.03690888119953864, 0.14978854286812765], [0.6624375240292195, 0.014763552479815478, 0.1493271818531334], [0.6470588235294118, 0.0, 0.14901960784313725]])

cmd.isomesh("IsoMesh_0", "RegularData_0", 1.7320508075688774, )
cmd.color("ColorRamp_1", "IsoMesh_0")
cmd.set("transparency", 0, "IsoMesh_0")
        