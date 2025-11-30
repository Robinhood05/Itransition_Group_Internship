let a = process.argv.slice(2);
//base case
if (a.length === 0) {
    console.log("");
    process.exit(0);
}





//shortest string >= Ans string
let s = a[0];
for (let i = 1; i < a.length; i++) {
    if (a[i].length < s.length) {
        s = a[i];
    }
}


for (let len = s.length; len > 0; len--) {
    for (let i = 0; i + len <= s.length; i++) {

        let sub = s.substring(i, i + len);

        let ok = true;
        for (let j = 0; j < a.length; j++) {
            if (!a[j].includes(sub)) {
                ok = false;
                break;
            }
        }

        if (ok) {
            console.log(sub);
            process.exit(0);
        }
    }
}

console.log("");
