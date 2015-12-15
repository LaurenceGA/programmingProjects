var removeTempC(bool) = true
var c(char)

repeat (--argc > 1) {
	++argv
	if ((*argv)++[0] == '-') {
		repeat ((c = (*argv)++[0]) != '\0') {
			switch (c) {
				case 'r':
					removeTempC = false
					break
				default:
					print("Incorrect optional argument %c.\n", c)
					break
			}
		}
	}
}
