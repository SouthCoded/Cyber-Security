


alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


axis_value =  "\"So,_did_you_hold_back_during_thattest?\"\"Maybe_a_little,\"_Sophronia_admitted._Soapgrinned.\"That's_my_girl.\"_Sophronia_glared_at_him._He_was_gettingfamiliar.\"You_are,_miss.\"_He_continued_togrin.\"I'm_my_own_girl,_thank_you_verymuch.\"―Gail_Carriger"

table_value = "6(#KM5_3KYG^~]O\"9q#O4KLsbE{_yri|6(5SDjll`%J:WEs6q-WETYtwSqD#%](D\"*O0W3YIL]&Yls(#\"^8RV}[8v}4g]uI94M>o.SIJUMu?gD$)`@NVpL:~R&xYs6(~V:c[K(=H8VSs<w5b:NTuN@{{]{tgBUk0c0WAQj7V*hSBUqgS0C\}}a<\"fwwT*Dy3W?$O5eEH.n?%L\"~U:RY;LGzR\"~T/D)~d6hHYU;QMu ??Y\"W=?0p_E{Xw'"



flag = ""

# table_value = ")J\"<E9o.cOMU%T!$NB/!0U`tLrqERuaG4(g.EUyM2?z>"

# axis_value = "5T3@mPuNk_Wh@t_5T3@mP_l0lR3p34t"


bit = 0
	
for d in table_value:
	
	pos_table = alphabet.find(d)
	pos_axis = alphabet.find(axis_value[bit:bit+1])

	bit += 1
	bit = bit % len(axis_value)


	y = (pos_table - pos_axis) % 94

	flag += alphabet[y:y+1]


print(flag)













