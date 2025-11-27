You have to write a JavaScript code that prints the longest common substring of passed arguments (with trailing newline — just use console.log for output).

The code will be running under Node.js and arguments will be passed via command line (it means you should not read standard input stream).

If the longest common superstring is empty (no arguments are passed or arguments have no common substrings) it’s necessary to print single newline. If there are several solution print any single one of them.

Limits are the following (do not use them in your solutions, these are only test restrictions): single string length is less or equal to 256, number of strings is less or equal to 64, strings contain only English letter and digits, time limit per test is 5 seconds.

The output should not contain any excess characters (error or debug messages, additional newlines, etc.).

Examples:

> node lcs.js

> node lcs.js ABCDEFZ WBCDXYZ
> BCD
> node lcs.js 132 12332 12312
> 1
> node lcs.js ABCDEFGH ABCDEFG ABCEDF ABCED
> ABC
> node lcs.js ABCDEFGH ABCDEFG ABCDEF ABCDE
> ABCDE
> node lcs.js ABCDEFGH ABCDEFG ABCDEF ABCDE EDCBA
> A
> node lcs.js ABCDEFGH ABCDEFG ABCDEF ABCDE EDCBCA
> BC
> node lcs.js ABCDEFGH ABCDEFG AxBCDEF ABCDxE EDCBCAABCD
> BCD
> node lcs.js ABCDEFGH 1234

> node lcs.js ABCDEFGH
> ABCDEFGH
