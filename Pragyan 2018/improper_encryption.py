import binascii


# M4 = "29190f1b18390707093a290b2d0b113f37332533333a0c3d1a29160a2f100a1d0034323b1b2e1225252500182531391d13260c21211019242d0a0a123b362d232d3a3a0a083c0e363c183a032b332d252c5637252d047b522a1e462a2a2909081705033d"

# M4 = binascii.unhexlify(M4)

# known = "sAldnJfpUGlciN"


# for p in range(14):

# 	password = "A" * p + known

# 	num = 28 - len(password) 

# 	password += "A" * num

# 	#password = binascii.hexlify(password)
	
# 	answer  = ""
	
# 	for x in range(28):
# 		answer += chr(M4[x] ^ ord(password[x]))

# 	print(answer[p:p+13])

# maybe = ["wL@|qNdNp@{Ox","~mt{jHXURP@rH","_Ys`ltCwBk}Bb","k^hfPoagyVMhw","lEnZKMq\Dfg}A","wCRAi]JatLrKR","qIcyfwQ^YDXg","MdksB[G{KoWmr","VF{{Hkmn}}|bxW","tV@uOAxXnIw]~","dm}EeTNK[\Rtk","_PMopb]~Ny{ag","b`gzFqhkkPnmS","RJrLUD}NBEbYe"]
# M4 = "2d142303073d05392c3d3e273c2a1a211f082b280d2d0e332025380301352a122a151c3a342e362d2723171904011c0c0c292b3d0122063e2e1e2a08102a2d3d0b2e102123141c280f0c373d2b380d3d0301301f2d281935233239330f3a102b123b0d2a"

# M4 = binascii.unhexlify(M4)


# for x in range(len(maybe)):
# 	known = maybe[x]
# 	for p in range(14):

# 		password = "A" * p + known
# 		num = 28 - len(password) 

# 		password += "A" * num
		
# 		answer  = ""
		
# 		for x in range(28):
# 			answer += chr(M4[x] ^ ord(password[x]))

# 		print(",\"" + answer[p:p+13] + "\"")


maybe1 = ["ZXcvsaw\}EhD","coC{LK]bM~\sR","TOGAtwHsNgGeb","tK}yHbYpW|QUY","pqEE]sZiLjang","JIyPLpCrZZZPp","rulAOiXdjadGS","N`}BVrNTQ_sdP","[q~[Md~ooHPgu","Jrg@[TEQxkSBU","Ik|Vko{F[hvbv","PpjfPQleXMVAK","KfZ]nFOf}mu|X","]VacyeLC]NHo]","SyWxmu]l~m~Ut","jNw|WMayongNb","]nsFoqthlw|XR","}jI~Sdekuljhi","yPqBFufrnzZSW","ChMWWvixJam@","{TXFTodHq_zc","GAIEMtrOsOHY`","RPJ\VbBtMXkZE","CSSG@RyJZ{he","@JHQpiG]yxM_F","YQ^aKWP~z]m|{","BGnZu@s}_}NAh","TwUdbcpX^sRm","rMPckIFNnVCe^","KzpgQqz[UZ~H","|Zt]iMoJ|LAhx","\^NeUX~IeWWXC","XdvY@I}P~Agc}","b\JLQJdKhq\]j","Z`_]RS]XJbJI","fuN^KHimctuiJ","sdMGP^YV]cVjo","bgT\FnbhJ@UOO","a~OJvU\iCpol","xeYzMkK\jfPLQ","csiAs|h_OFsqB","uCRd_kzoeNbG","FJKeWRd^UksOK","}kamjXKDhjT]","H]o[UVMZGqqBm","hYUciC\Y^jgrV","lcm_|R_@E|WIh","V[QJmQF[SLlw","ngD[nH]McwR`\\","RrUXwSK}XIEC_","GcVAlE{Ff^f@z","V`OZzu@xq}eeZ","UyTLJN~oR~@Ey","LbB|qpiLQ[`fD","WtrGOgJOt{C[W","ADIyXDIjTX~HR","AQMYLpteh[YZ}","xfm]vHHpyX@Ak","OFigNt]azA[W[","oBS_raLbcZMg`","kxkcgpO{xL}\^","Q@WvvsV`n|FbI","i|BgujMv^Gxuj","UiSdlq[FeyoVi","@xP}wgk}[nLUL","Q{IfaWPCLMOpl","RbRpQlnToNjPO","KyD@jRywlkJsr","Pot{TEZtIKiNa","F_OECfYQihT]d","ZWqBn`OXXqLln","c`QFTXsMIrUwx","T@U|ldf\JkNaH","tDoDPqw_SpXQs","p~WxE`tFHfhjM","JFkmTcm]^VSTZ","rz~|WzvKnmmCy","NooNa`{USz`z","[~lfUwP@kDYc_","J}u}CGk~|gZF","Idnks|Ui_df\\","Px[HBBJ\A_Ea","KiH`vUaIya|xr","]Ys^avblYBAkw","\]@zaJTguyf@}","ej`~[rhrdz[k","RJdDcN}cgcdM[","rN^|_[l`~xr}`","vtf@JJoyenBF^","LLZU[Ivbs^yxI","tpODXPmtCeGoj","He^GAK{Dx[PLi","]t]^Z]KFLsOL","LwDELmpAQopjl","On_S|VNVrlUJO","VuIcGhYuqIuir","McyXyzvTiVTa","[SBfn\yStJkGd","`pHpEfBBgRiJN","YGht^~WvQpQX","nglNGbkFuHkGh","NcVv{wzElS}wS","JYnJnfy\wEMLm","paR_e`Gauvrz","H]GN||{QQNHeY","tHVMegmajp_FZ","aYUT~q]ZTg|E","pZLOhAfdCD`_","sCWYXzXs`GZ@|","jXAicDOPcbzcA","qNqR]SlSFBY^R","g~JlJpovfadMW","{RXxOVhWQ@BED","Bex|unTB@C[^R","uE|FMRASCZ@Hb","UAF~qGPPZAVxY","Q{~BdVSIAWfCg","kCBWuUJRWg]}p","SWFvLQDg\cjS","ojFEoWGt\btIP","z{E\tAwObuWJu","kx\GbqLquVToU","haGQRJrfVUqOv","qzQaiteEUpQlK","jlaZWcFFpPrQX","|\Zd@@EcPsOB]","YBcvH|}aBtIzB","`uCrrDAtSwPaT","WUGHJxTePnKwd","wQ}pvmEfIu]G_","skELc|FRcm|a","ISyYr_dDSVBv","qolHqfDrthhUU","Mz}Kh}RBOVvV","Xk~RskbyqA\\us","IhgIe[YGfb_PS","Jq|_U`gPEazpp","Sjjon^psFDZSM","H|ZTPISpcdyn^","^LajGjPUCGD}[","Iy^FbiKrwalSW","pN~BXQwgfbuHA","Gnzx`mbve{n^q","gj@@\\xsu|`xnJ","cPx|IiplgvHUt","YhDiXjiwqFskc","aTQx[sraA}M|@","]A@{BhdQzCZ_C","HPCbY~TjDTy\f","YSZyONoTSwzyF","ZJAouQCpt_Ye","CQW_DKF`sQzX","XGgdz\ecVq\GK","Nw\ZmfFvRaTN","rDnlw_XGbDEF[","KsNhMgdRsG\]M","|SJRu[qCp^GK}","\WpjIN`@iEQ{F","XmHV\_cYrSa@x","bUtCM\zBdcZ~o","ZiaRNEaTTXdiL","f|pQW^wdofsJO","smsHLHG_QqPIj","bnjSZx|aFRSlJ","awqEjCBveQvLi","xlguQ}UUftVoT","czWNojvVCTuRG","uJlpxIuscwHAB","OtDyALmRGmPJo","vCd}{tQGVnIQy","Ac`GCHDVUwRGI","agZ]UULlDwr","e]bCjLVLWztLL","_e^V{OOWAJOr[","gYKGxVTAqqqex","[LZDaMBqJOfF{","N]Y]z[rJtXEE^","_^@FlkItc{F`~","\G[P\Pwc@xc@]","E\M`gn`@C]Cc`","^J}[YyCCf}`^s","HzFeNZ@fF^]Mv","^QORyxwnx\~Y","FiqKhADb{EeO","qIuqP}Qs|b^s","QMOIlh@peyHCD","UwwuyyCi~oxxz","oOK`hzZrh_CFm","Ws^qkcAdXd}QN","kfOrrxWTcZjrM","~wLkingo]MIqh","otUp^\QJnJTH","lmNfOebFimotk","uvXVt[uejHOWV","n`hmJLVfOhljE","xPSS]oUCoKQy@","^UOgiwcIyzRDU","nC[dHIcGJipbs","xWXEvImtYKVDi","lTy{vG^g{mp^G","ouG{xtME]KjpO","NKGuKgoc{QDxK","pKIFXEIEaL|]","pEzUzco_OwHjK","~viw\EuqGs^|K","MeKQz_[yCeH|B","^Gmw`qS}UsHut","|aKmNyWkCsACE","ZGQCF}A}Czwrb","|]KBkW}JLFUQ","Wt{`rq_R[jiye","gbocSO_\hyK_C","qvlBmOQo{[myY","euM|mAb|Y}Kcw","fTs|crq^[QM","GjsrPaSxYAE{","yj}ACCu^CowAm","ydNRaeSDmgsW{","wW]pGCIjeceA{","DDVaYgbausAr","WfYp{wofwcsHD","u@jUkpacz~u","SfeD]{}fajLOR","u|KLYmkfh\}ha","v@|{tMDpKQTIO","FVhxUsD~xBvoi","PBkYksJMk`PIs","DAJgk}y^IFvS]","G`tgeNj|o`l}U","f^tiV]HZIzBuQ","X^zZEn|STJqG","XPIIgYHf}\\NgQ","VcZkARHuXXqQ","epxMge|@qNNqX","vR^k}KtDgXNxn","TtxqSCpRqXGN_","rRb_[GfDqQqx","THLW_QpDxg@XK","BGg}HVf`pldcZ","rQs~ihfnCFE|","dEp_Whh]P]`cf","pFQaWf[Nr{FyH","sgoaYUHlT]\W@","RYoojFjJrGr_D","lYa\ydLlhiz[R","lWRO[BjvFa~MD","bdAm}dpXNeh[D","QwcK[~^PJs~[M","BUEmAPVT\e~R{","`scwoXRBJewdJ","FUyYg\DTJlAUm","`OWQcJRTCZpr^","E\aAStv[M\\Nvl","uJuBrJvU~OlPJ","c^vcLJxfmmJvP","w]W]LDKuOKll~","t|i]BwXWimvBv","UBiSqdzqOwXJr","kBg`bF\WUYPNd","kLTs@`zM{QTXr","eGQfF`csUBNr","Vlew@\\NkwCTN{","ENCQZrFoaUTGM","gheKtzBywU]q|","ANe|~Tow\k@[","gTQmxhBo~jZgh","^Z]ZqdMf}v[@","nLIYPZMhNeyfY","xXJxnZC[]G_@C","l[kFnTpHayZm","ozUF`gcjYGcte","NDUHStAL]M|a","pD[{@VgjesExw","pJhhbpApK{Ana","~y{JDV[^CWxa","MjYlbLuVGiAxh","^HJxb}RQAq^","|nYPVjyDGHGo","ZHC~^noRGv~vH","|RmvZxyRN@OQ{","XPlb~NVYP~qll","hFxa_pVWcmSJJ","~R{@apXdpOulP","jQZ~a~kwRiSv~","ipd~oMxUtOIXv","HNdp\^ZsRUgPr","vNjCO||UH{oTd","v@YPmZZOfskBr","xsJrK|@anw}Tr","K`hTmfnijakT{","XBNrwHfm|wk]M","zdhhY@b{jwbk|","\BrFQDtmj~TZ[","zX\\NURbmcHe}h","d}dhZb@|BU~f_","Tkpk{\@rqF\@y","BsJE\\NAbdzfc","V|RtER}R@B\|M","U]ltKanpfdFRE","tclzxrLV@~hZA","JcbIkPjpZP`^W","JmQZIvLjtXdHA","D^BxoPVD|\r^A","wM`^IJxLxJd^H","doFxSdpHn\dW~","FI`b}lt^x\maO","`ozLuhbHxU[Ph","FuTDq~tHqcjw[","_t`PRjitGUiU","OI`cqljgGTwOs","Y]cBOldTTvQii","M^B|ObWGvPwsG","N||AQDePvm]O","oA|rrBfCvlCUK","QArAa`@elBKQ]","QOARCFfBJOGK","_|Rpe`|QJNYQK","lopVCzRYNXOQB","MVpYTZ]XNOXt","]kpjw\^KNNFnE","{MjDXH]NGp_b","]WDL{N^]GqAxQ","]OOnWx_gs^VS","mY[mvFQT`|pu","{MXLHFqbGBZVo","oNyrHHBqed|LA","loGrF{QSCBfbI","MQG|uhsueXHjM","sQIOfJUSv@n[","s_z\DlsIQ~DxM","}li~bJigYzRnM","NKXDPGo]lDnD","]]m~^~OkKzDgr","{KdpvK}]zMQC","Y]QJxr]k]s{`d","GB|dKkTEJGW","Mtr^}mILRf{F","}bf]\SIBauYY`","kve|bSGqrWz","uDBb]tbPqYeT","|TzBlng@vWCK\\","]jzL_}EfPMmCX","cjtL_c@JceGN","cdGlnyEZdkaQX","mWTNH__tlowGX","^DvhnEq|hyaGQ","MfPNtkyx~oaNg","o@vTZc}nhohxV","IflzRgkxhf^Iq","o|BrVq}xaPonB","vIBth[ZyGCRjJ","F_VwIeZwtPpLl","PKUVweTDgrVjv","DHthwkgWETppX","GiJhyXtucrj^P","fWJfJKVSEhDVT","XWDUYipu_FLRB","XYwF{OVoqNHDT","Vjdd]iLAyJ^RT","eyFB{sbI}\HR]","v[`da]jMkJH[k","T}F~OUn[}JAmZ","r[\PGQxM}Cw\}","TArXCGnMtuF{N","Kyha^HolbjGf~","{o|bvobQye@X","m{CAvaQB[CfB","yx^}AxRB`}e|l","zY`}OKA`F[Rd","[g`s|XcF`AQZ`","egn@ozE`zoY^v","ei]SM\czTg]H`","kZNqkzyT\cK^`","XIlWM`W\Xu]^i","KkJqWN_XNc]W_","iMlkyF[NXcTan","OkvEqBMXXjbPI","iqXMuT[XQ\Swz","{S}WM}zIKKRH","KEiTlCzGxlitn","]QjuRCttkNORt","IRKKRMGgIhiHZ","JsuK\~TEoNsfR","kMuEomvcIT]nV","UM{v|OPESzUj@","UCHe^iv_}rQ|V","[p[GxOlquvGjV","hcya^UByq`Qj_","{A_GD{J}gvQci","Ygy]jsNkqvXUX","AcsbwX}qnd","Y[M{faN}xI_CL"]


maybe2 = ["ZXcvsaw\}EhD","jNw|WMayongNb","|Zt]iMoJ|LAhx","hYUciC\Y^jgrV","kxkcgpO{xL}\^","JFkmTcm]^VSTZ","tFe^GAK{Dx[PL","tHVMegmajp_FZ","z{EoCAwObtIPZ","IhgIe[YGfb_PS","ZJAouQCpt_Ye","xlguQ}UUftVoT","^J}[YyCCf}`^s","xPSS]oUCoKQy@","^UOgiwcIyzRDU","gbocSO_\hyK_C","PBkYksJMk`PIs","pFQaWf[Nr{FyH","t|i]BwXWimvBv","NDUHStAL]M|a","vx@YPmZZOfskB","JmQZIvLjtXdHA","_|RCR`|QJOGKd","NKXDPGo]lDnD'","MfPNtkyx~oaNg","T}F~OUn[}JAmZ","OkvEqBMXXjbPI","Y[M{faN}xI_CL]"]

for x in range(len(maybe2)):
	
	known = maybe2[x]

	for p in range(9):

		key = known[p:p+5]
		for t in maybe1:
			if key in t:
				print("Key : " + key + " , maybe2 " + known + " , maybe1 " + t)