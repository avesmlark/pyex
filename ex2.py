taxes = {
"AL": 4.0,
"AK": 0.0,
"AZ": 5.6,
"CA": 7.25,
"CO": 2.9,
"CT": 6.35,
"DE": 0.0,
"DC": 5.75,
"FL": 6.0,
"GA": 4.0,
"HI": 4.0,
"ID": 6.0,
"IL": 6.25,
"IN": 7.0,
"IA": 6.0,
"KS": 6.5,
"KY": 6.0,
"LA": 5.0,
"ME": 5.5,
"MD": 6.0,
"MA": 6.25,
"MI": 6.0,
"MN": 6.875,
"MS": 7.0,
"MO": 4.225,
"MT": 0.0,
"NE": 5.5,
"NV": 6.85,
"NH": 0.0,
"NJ": 6.625,
"NM": 5.125,
"NY": 4.0,
"NC": 4.75,
"ND": 5.0,
"OH": 5.75,
"OK": 4.5,
"OR": 0.0,
"PA": 6.0,
"PR": 11.5,
"RI": 7.0,
"SC": 6.0,
"TN": 7.0,
"TX": 6.25,
"UT": 4.7,
"VT": 6.0,
"VA": 4.3,
"WA": 6.5,
"WV": 6.0,
"WI": 5.0,
"WY": 4.0,

}

print("Good day.  Please allow me to compute the state sales tax.")
while 1 == 1:
	print("Please input state in the format: TX")
	state = input()
	tax_rate = taxes[state]
	print("Thank you.")
	total = float(input("Please input total in the format: 52.71        "))
	salt = tax_rate * 0.01 * total
	print("The sales tax is")
	print(salt)