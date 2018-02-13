 load('base64.js');
 function process(a, b) {
    var len = Math.max(a.length, b.length);
    var out = [];
    for (var i = 0, ca, cb; i < len; i++) {
      ca = a.charCodeAt(i % a.length);
      cb = b.charCodeAt(i % b.length);
      out.push(ca ^ cb);
    }
    return String.fromCharCode.apply(null, out);
  }

  var inputEl = 'xaufoujk}yngrcne EacrBxz`Cz*wT~:h/ny4L23.{'
  var flag = 'Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA==';
  var key = "nosource"
  print(btoa(process(inputEl, key)))

// console.log(Buffer.from('Hello World!').toString('base64'));
// console.log(Buffer.from(b64Encoded, 'base64').toString());