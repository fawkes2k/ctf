const inp = document.querySelector("input");
const sub = document.querySelector('button');
function xor(_0x28ba71, _0x350584) {
  let _0x29e51b = '';
  for (let _0x148676 = 0x0; _0x148676 < _0x28ba71.length; _0x148676++) {
    _0x29e51b += String.fromCharCode(_0x28ba71.charCodeAt(_0x148676) ^ _0x350584.charCodeAt(_0x148676 % _0x350584.length));
  }
  return _0x29e51b;
}
function toHex(_0x359d42) {
  let _0xa1a877 = '';
  for (let _0x27ba7d = 0x0; _0x27ba7d < _0x359d42.length; _0x27ba7d++) {
    let _0x45e7fd = _0x359d42.charCodeAt(_0x27ba7d).toString(0x10);
    if (_0x45e7fd.length == 0x1) {
      _0x45e7fd = '0' + _0x45e7fd;
    }
    _0xa1a877 += _0x45e7fd;
    console.log(_0x45e7fd);
  }
  return _0xa1a877;
}
function reverseString(_0x30e0ba) {
  return _0x30e0ba.split('').reverse().join('');
}
sub.onclick = function () {
  const _0x32e2d3 = inp.value;
  let _0x359865 = toHex(xor(_0x32e2d3, "ABCD"));
  if (_0x359865.substr(0x0, 0x4) == "1611" && _0x359865.substr(0x4, 0x4).split('').reverse().join('') == "e1a0" && _0x359865.substr(0x8, 0x4) == '3a72' && _0x359865.substr(0xc, 0x4).split('').reverse().join('') == "2212" && _0x359865.substr(0x10, 0x4) == '3431' && _0x359865.substr(0x14, 0x4).split('').reverse().join('') == "5202" && _0x359865.substr(0x18, 0x4) == "3573" && _0x359865.substr(0x1c, 0x4).split('').reverse().join('') == "a2c2" && _0x359865.substr(0x20, 0x4) == "1e2c" && _0x359865.substr(0x24, 0x4).split('').reverse().join('') == "0337" && _0x359865.substr(0x28, 0x4) == '1e2c' && _0x359865.substr(0x2c, 0x4).split('').reverse().join('') == "7707" && _0x359865.substr(0x30, 0x4) == "2527" && _0x359865.substr(0x34, 0x4).split('').reverse().join('') == "9372") {
    document.body.innerText = "Correct!";
  } else {
    document.body.innerText = "Incorrect.";
  }
};