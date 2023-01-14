var CryptoJS = require("crypto-js");

var $_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
var _chars_len = $_chars.length;

function _rds(len) {
    var retStr = '';
    for (i = 0; i < len; i++) {
        retStr += $_chars.charAt(Math.floor(Math.random() * _chars_len));
    }
    return retStr;
}

function _gas(data, key0, iv0) {
    key0 = key0.replace(/(^\s+)|(\s+$)/g, "");/* 去除空格 */
    var key = CryptoJS.enc.Utf8.parse(key0);/* 转换为utf8 */
    var iv = CryptoJS.enc.Utf8.parse(iv0);
    var encrypted = CryptoJS.AES.encrypt(data, key, {
        iv: iv,//偏移量
        mode: CryptoJS.mode.CBC,//加密模式
        padding: CryptoJS.pad.Pkcs7//填充方式
    });
    return encrypted.toString();/* 返回的是base64格式的密文 */
}

function encryptAES(data, _p1) {
    if (!_p1) {
        return data;
    }
    var encrypted = _gas(_rds(64) + data, _p1, _rds(16));//密码，key，偏移量
    return encrypted;
}

function etd2(_p0, _p1) {
    var p2 = encryptAES(_p0, _p1);//密码，key
    return p2;
    }

console.log(etd2('123456', 'zbkTSuwUxCdMSxNp'));// 123456为密码，zbkTSuwUxCdMSxNp为源码中的key
