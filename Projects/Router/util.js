function autoRefreshMainTable(tab_id) {
  var tableParent, tableChildren, tableLine;
  var i,
    tbodyNode,
    totalCnt = 0,
    delCnt = 0;
  var delArray = new Array();

  tableParent = getElById(tab_id);
  if (null == tableParent) return;
  tableChildren = tableParent.childNodes;
  if (null == tableChildren) return;

  for (i = 0; i < tableChildren.length; i++) {
    if ("TBODY" == tableChildren[i].tagName) {
      tbodyNode = tableChildren = tableChildren[i];
      break;
    }
  }

  tableChildren = tableChildren.childNodes;
  if (null == tableChildren) return;

  for (i = 0; i < tableChildren.length; i++) {
    tableLine = tableChildren[i];
    if (null == tableLine || "TR" != tableLine.tagName) continue;
    totalCnt++;
    if ("none" != tableLine.style.display) continue;

    delArray[delCnt++] = tableLine;
  }

  if (delCnt > 0) {
    for (i = 0; i < delArray.length; i++) tbodyNode.removeChild(delArray[i]);
    getElById("TRSpan").rowSpan = totalCnt - delCnt;
  }
}

/*start of modify by j00127542 for A36D07611 wps pin 20090815*/
function isSafeStringIn(compareStr, UnsafeStr) {
  for (var i = 0; i < compareStr.length; i++) {
    var c = compareStr.charAt(i);
    if (isValidAscii(c) != "") {
      return false;
    } else {
      if (UnsafeStr.indexOf(c) == -1) {
        return false;
      }
    }
  }
  return true;
}
/*end of modify by j00127542 for A36D07611 wps pin 20090815*/

/*adjust data type*/
function isValidAscii(val) {
  for (var i = 0; i < val.length; i++) {
    var ch = val.charAt(i);
    if (ch < " " || ch > "~") {
      return ch;
    }
  }
  return "";
}

function hasForbiddenChar(val) {
  var ForbiddenString = "\\'\"=<>/&";

  if (isValidAscii(val) != "") {
    return isValidAscii(val);
  }

  for (var i = 0; i < val.length; i++) {
    if (ForbiddenString.indexOf(val.charAt(i)) != -1) {
      return val.charAt(i);
    }
  }
  return "";
}

//用于WLAN校验密匙
function isHexaDigit(digit) {
  var hexVals = new Array(
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f"
  );
  var len = hexVals.length;
  var i = 0;
  var ret = false;

  for (i = 0; i < len; i++) if (digit == hexVals[i]) break;

  if (i < len) ret = true;

  return ret;
}

//用于WLAN校验密匙
function isValidKey(val, size) {
  var ret = false;
  var len = val.length;
  var dbSize = size * 2;

  if (len == size) {
    if (val.match(/[^\x00-\xff]/g)) {
      return ret;
    } else {
      for (i = 0; i < size; i++)
        if (val.charAt(i) == ",") {
          break;
        }
      if (i == size) ret = true;
    }
  } else if (len == dbSize) {
    for (i = 0; i < dbSize; i++) if (isHexaDigit(val.charAt(i)) == false) break;
    if (i == dbSize) ret = true;
  } else ret = false;

  return ret;
}

function isNameUnsafe(compareChar) {
  var unsafeString = "\"<>%\\^[]`+$,='#&: \t";

  if (
    unsafeString.indexOf(compareChar) == -1 &&
    compareChar.charCodeAt(0) > 32 &&
    compareChar.charCodeAt(0) < 123
  )
    return false; // found no unsafe chars, return false
  else return true;
}
// Check if a name valid
function isValidName(name) {
  var i = 0;

  for (i = 0; i < name.length; i++) {
    if (isNameUnsafe(name.charAt(i)) == true) return false;
  }

  return true;
}

function isNameUnsafeEx(compareChar) {
  if (compareChar.charCodeAt(0) > 32 && compareChar.charCodeAt(0) < 127)
    return false; // found no unsafe chars, return false
  else return true;
}
// Check if a name valid
function isValidNameEx(name) {
  var i = 0;

  for (i = 0; i < name.length; i++) {
    if (isNameUnsafeEx(name.charAt(i)) == true) return false;
  }

  return true;
}

// same as is isNameUnsafe but allow spaces
function isCharUnsafe(compareChar) {
  var unsafeString = "\"<>%\\^[]`+$,='#&.:\t";

  if (
    unsafeString.indexOf(compareChar) == -1 &&
    compareChar.charCodeAt(0) >= 32 &&
    compareChar.charCodeAt(0) < 123
  )
    return false; // found no unsafe chars, return false
  else return true;
}
//same as is isValidName but allow spaces
function isValidNameWSpace(name) {
  var i = 0;

  for (i = 0; i < name.length; i++) {
    if (isCharUnsafe(name.charAt(i)) == true) return false;
  }

  return true;
}

//用于isValidString内部调用

function isStringUnsafe(compareChar) {
  var unsafeString = '"';

  if (
    unsafeString.indexOf(compareChar) == -1 &&
    compareChar.charCodeAt(0) > 31 &&
    compareChar.charCodeAt(0) < 127
  )
    return false; // found no unsafe chars, return false
  else return true;
}

// Check if a string valid 用于tr069
//a valid string do not contain '"' and each char is validAscII
function isValidString(name) {
  var i = 0;

  for (i = 0; i < name.length; i++) {
    if (isStringUnsafe(name.charAt(i)) == true) return false;
  }

  return true;
}

function isInteger(value) {
  if (/^(\+|-)?\d+$/.test(value)) {
    return true;
  } else {
    return false;
  }
}

function isPlusInteger(value) {
  if (isInteger(value) && parseInt(value) >= 0) {
    return true;
  } else {
    return false;
  }
}

function isFloat(value) {
  if (/^(\+|-)?\d+($|\.\d+$)/.test(value)) {
    return true;
  } else {
    return false;
  }
}

function isPlusFloat(value) {
  if (isFloat(value) && parseFloat(value) >= 0.000001) {
    return true;
  } else {
    return false;
  }
}

function isNetIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var addrParts = address.split(".");
  var num = 0;

  num = parseInt(addrParts[3]);
  if (num == 0) {
    return false;
  }

  return true;
}

/*adjust the data of network format*/
function isValidIpAddress(address) {
  var i = 0;

  if (address == "0.0.0.0" || address == "255.255.255.255") return false;

  var addrParts = address.split(".");
  if (addrParts.length != 4) return false;
  for (i = 0; i < 4; i++) {
    if (
      isNaN(addrParts[i]) ||
      addrParts[i] == "" ||
      addrParts[i].charAt(0) == "+" ||
      addrParts[i].charAt(0) == "-"
    )
      return false;
    if (addrParts[i].length > 3 || addrParts[i].length < 1) {
      return false;
    }
    if (!isInteger(addrParts[i]) || addrParts[i] < 0) {
      return false;
    }
    num = parseInt(addrParts[i]);
    if (i == 0 && num == 0) {
      return false;
    }
    if (num < 0 || num > 255) return false;
  }
  return true;
}

function isValidIpAddr(ip1, ip2, ip3, ip4) {
  if (ip1 == 0 || ip4 == 0 || ip4 == 255 || ip1 == 127) return false;

  return true;
}

function inValidIPAddr(Address) {
  var address = Address.match("^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$");
  var digits;
  var i;

  if (address == null) {
    alert("Invalid IP address " + Address);
    return true;
  }

  digits = address[0].split(".");
  for (i = 0; i < 4; i++) {
    if (
      Number(digits[i]) > 255 ||
      Number(digits[i]) < 0 ||
      Number(digits[0]) > 223 ||
      digits[i] == null
    ) {
      alert("Invalid IP address " + Address);
      return true;
    }
  }
  if (!isValidIpAddr(digits[0], digits[1], digits[2], digits[3], false)) {
    alert("Invalid IP address " + Address);
    return true;
  }
  return false;
}

function trim(s) {
  var l = 0;
  var r = s.length - 1;
  while (l < s.length && s[l] == " ") {
    l++;
  }
  while (r > l && s[r] == " ") {
    r -= 1;
  }
  return s.substring(l, r + 1);
}

function inValidIPv6Addr(Address1) {
  var regExp =
    /^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/;

  var Address = trim(Address1);
  var address = Address.match(regExp);
  if (address == null) {
    alert("Invalid IPv6 Address: " + Address);
    return true;
  }
  return false;
}

function isBroadcastIp(ipAddress, subnetMask) {
  var maskLenNum = 0;
  tmpMask = subnetMask.split(".");
  tmpIp = ipAddress.split(".");

  if (parseInt(tmpIp[0]) > 223 || 127 == parseInt(tmpIp[0])) {
    return true;
  }

  for (maskLenNum = 0; maskLenNum < 4; maskLenNum++) {
    if (parseInt(tmpMask[maskLenNum]) < 255) break;
  }

  tmpNum0 = parseInt(tmpIp[maskLenNum]);
  tmpNum1 = 255 - parseInt(tmpMask[maskLenNum]);
  tmpNum2 = tmpNum0 & tmpNum1;
  if (tmpNum2 != 0 && tmpNum2 != tmpNum1) {
    return false;
  }

  if (maskLenNum == 3) {
    //掩码最后一位不等于255: 255.255.255.xxx
    return true;
  } else if (maskLenNum == 2) {
    //255.255.xxx.xxx
    if (
      (tmpIp[3] == 0 && tmpNum2 == 0) ||
      (tmpIp[3] == 255 && tmpNum2 == tmpNum1)
    ) {
      return true;
    }
  } else if (maskLenNum == 1) {
    //255.xxx.xxx.xxx
    if (
      (tmpNum2 == 0 && tmpIp[3] == 0 && tmpIp[2] == 0) ||
      (tmpNum2 == tmpNum1 && tmpIp[3] == 255 && tmpIp[2] == 255)
    ) {
      return true;
    }
  } else if (maskLenNum == 0) {
    //xxx.xxx.xxx.xxx
    if (
      (tmpNum2 == 0 && tmpIp[3] == 0 && tmpIp[2] == 0 && tmpIp[1] == 0) ||
      (tmpNum2 == tmpNum1 &&
        tmpIp[3] == 255 &&
        tmpIp[2] == 255 &&
        tmpIp[1] == 255)
    ) {
      return true;
    }
  }

  return false;
}

function isAbcIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var addrParts = address.split(".");
  var num = 0;

  num = parseInt(addrParts[0]);
  if (num < 1 || num >= 224 || num == 127) {
    return false;
  }
  /* start of HG_Maintenance 2007.10.24 ATPV100R001C01B011 AU4D00155
    num = parseInt(addrParts[3]);
    if (num == 255)
    {
        return false;
    }
   end of HG_Maintenance 2007.10.24 ATPV100R001C01B011 AU4D00155 */

  return true;
}

/* start of HG_Maintenance 2007.10.24 ATPV100R001C01B011 AU4D00155 */
function isHostIpWithSubnetMask(address, subnet) {
  if (isAbcIpAddress(address) == false) {
    return false;
  }
  if (isValidSubnetMask(subnet) == false) {
    return false;
  }

  var addr = IpAddress2DecNum(address);
  var mask = IpAddress2DecNum(subnet);

  /* 是网段Ip */
  if (0 == (addr & ~mask)) {
    return false;
  }

  /* 是广播Ip */
  if (isBroadcastIp(address, subnet) == true) {
    return false;
  }

  return true;
}
/* end of HG_Maintenance 2007.10.24 ATPV100R001C01B011 AU4D00155 */

function isDeIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var num = 0;
  var addrParts = address.split(".");
  if (addrParts.length != 4) {
    return false;
  }

  if (!isInteger(addrParts[0]) || addrParts[0] < 0) {
    return false;
  }
  num = parseInt(addrParts[0]);
  if (!(num >= 224 && num <= 247)) {
    return false;
  }

  for (var i = 1; i <= 3; i++) {
    if (!isInteger(addrParts[i]) || addrParts[i] < 0) {
      return false;
    }
    num = parseInt(addrParts[i]);
    if (!(num >= 0 && num <= 255)) {
      return false;
    }
  }

  return true;
}

function isBroadcastIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var addrParts = address.split(".");
  if (addrParts[3] == "255") {
    return true;
  }
  return false;
}

function isNtwkSgmtIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var addrParts = address.split(".");
  if (addrParts[3] == "0") {
    return true;
  }
  return false;
}

function isLoopIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var addrParts = address.split(".");
  if (addrParts[0] == "127") {
    return true;
  }
  return false;
}

function getLeftMostZeroBitPos(num) {
  var i = 0;
  var numArr = [128, 64, 32, 16, 8, 4, 2, 1];

  for (i = 0; i < numArr.length; i++) if ((num & numArr[i]) == 0) return i;

  return numArr.length;
}
function getRightMostOneBitPos(num) {
  var i = 0;
  var numArr = [1, 2, 4, 8, 16, 32, 64, 128];

  for (i = 0; i < numArr.length; i++)
    if ((num & numArr[i]) >> i == 1) return numArr.length - i - 1;

  return -1;
}
function isValidSubnetMask(mask) {
  var i = 0,
    num = 0;
  var zeroBitPos = 0,
    oneBitPos = 0;
  var zeroBitExisted = false;

  if (mask == "0.0.0.0") return false;

  var maskParts = mask.split(".");
  if (maskParts.length != 4) return false;

  for (i = 0; i < 4; i++) {
    if (
      isNaN(maskParts[i]) == true ||
      maskParts[i] == "" ||
      maskParts[i].charAt(0) == "+" ||
      maskParts[i].charAt(0) == "-"
    )
      return false;
    if (!isInteger(maskParts[i]) || maskParts[i] < 0) {
      return false;
    }
    num = parseInt(maskParts[i]);
    if (num < 0 || num > 255) return false;
    if (zeroBitExisted == true && num != 0) return false;
    zeroBitPos = getLeftMostZeroBitPos(num);
    oneBitPos = getRightMostOneBitPos(num);
    if (zeroBitPos < oneBitPos) return false;
    if (zeroBitPos < 8) zeroBitExisted = true;
  }

  return true;
}

function isValidPort(port) {
  if (!isInteger(port) || port < 1 || port > 65535) {
    return false;
  }

  return true;
}

function isValidPortPair(StartPort, EndPort) {
  if (!isValidPort(StartPort) || !isValidPort(EndPort)) {
    return false;
  }

  if (parseInt(StartPort) <= parseInt(EndPort)) return false;

  return true;
}

function isValidMacAddress(address) {
  var c = "";
  var i = 0,
    j = 0;

  if (address.toLowerCase() == "ff:ff:ff:ff:ff:ff") {
    return false;
  }

  addrParts = address.split(":");
  if (addrParts.length != 6) return false;

  for (i = 0; i < 6; i++) {
    if (addrParts[i] == "") return false;

    if (addrParts[i].length != 2) {
      return false;
    }

    if (addrParts[i].length != 2) {
      return false;
    }

    for (j = 0; j < addrParts[i].length; j++) {
      c = addrParts[i].toLowerCase().charAt(j);
      if ((c >= "0" && c <= "9") || (c >= "a" && c <= "f")) continue;
      else return false;
    }
  }

  return true;
}

function isNtwkSgmtIpAddress(address) {
  if (isValidIpAddress(address) == false) {
    return false;
  }

  var addrParts = address.split(".");
  if (addrParts[3] == "0") {
    return true;
  }
  return false;
}

function isSameSubNet(Ip1, Mask1, Ip2, Mask2) {
  var count = 0;
  //alert('isSameSubNet');
  lan1a = Ip1.split(".");
  lan1m = Mask1.split(".");
  lan2a = Ip2.split(".");
  lan2m = Mask2.split(".");

  for (i = 0; i < 4; i++) {
    l1a_n = parseInt(lan1a[i]);
    l1m_n = parseInt(lan1m[i]);
    l2a_n = parseInt(lan2a[i]);
    l2m_n = parseInt(lan2m[i]);
    if ((l1a_n & l1m_n) == (l2a_n & l2m_n)) count++;
  }
  if (count == 4) return true;
  else return false;
}

/////////////////////////////////////////////////

//将IP地址转换为十进制整数
function IpAddress2DecNum(address) {
  if (isValidIpAddress(address) == false) {
    return -1;
  }
  var addrParts = address.split(".");
  var num = 0;
  for (i = 0; i < 4; i++) {
    num += parseInt(addrParts[i]) * Math.pow(256, 3 - i);
  }
  return num;
}

/*
function port_check(start, end) {
   if ( (start <= 21) && (end >= 21) )
   {
       return 21;
   }

   if ( (start <= 6667) && (end >= 6667) )
   {
       return 6667;
   }

   if ( (start <= 69) && (end >= 69) )
   {
       return 69;
   }

   if ( (start <= 161) && (end >= 161) )
   {
       return 161;
   }

   if ( (start <= 162) && (end >= 162) )
   {
       return 162;
   }

   if ( (start <= 517) && (end >= 517) )
   {
       return 517;
   }

   if ( (start <= 518) && (end >= 518) )
   {
       return 518;
   }

   if ( (start <= 1720) && (end >= 1720) )
   {
       return 1720;
   }

   if ( (start <= 1723) && (end >= 1723) )
   {
       return 1723;
   }

   if ( (start <= 80) && (end >= 80) )
   {
       return 80;
   }
   
   return 0;
}
*/
//var hexVals = new Array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
//             "A", "B", "C", "D", "E", "F");

/*the change of data type*/
/*
function encodeUrl(val)
{
   var len     = val.length;
   var i       = 0;
   var newStr  = "";
   var original = val;

   for ( i = 0; i < len; i++ ) {
      if ( val.substring(i,i+1).charCodeAt(0) < 255 ) {
         // hack to eliminate the rest of unicode from this
         if (isUnsafe(val.substring(i,i+1)) == false)
            newStr = newStr + val.substring(i,i+1);
         else
            newStr = newStr + convert(val.substring(i,i+1));
      } else {
         // woopsie! restore.
         alert ("Found a non-ISO-8859-1 character at position: " + (i+1) + ",\nPlease eliminate before continuing.");
         newStr = original;
         // short-circuit the loop and exit
         i = len;
      }
   }

   return newStr;
}
*/

//web Element
/*start of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/
/*get element by name or id*/
function getElById(sId) {
  return getElement(sId);
}

function getElementById(sId) {
  if (document.getElementById) {
    return document.getElementById(sId);
  } else if (document.all) {
    // old IE
    return document.all(sId);
  } else if (document.layers) {
    // Netscape 4
    return document.layers[sId];
  } else {
    return null;
  }
}

/*getElByName*/
function getElementByName(sId) {
  // standard
  if (document.getElementsByName) {
    var element = document.getElementsByName(sId);

    if (element.length == 0) {
      return null;
    } else if (element.length == 1) {
      return element[0];
    }

    return element;
  }
}

function getElement(sId) {
  var ele = getElementByName(sId);
  if (ele == null) {
    return getElementById(sId);
  }
  return ele;
}
/*end of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/

function getOptionIndex(sId, sValue) {
  var selObj = getElById(sId);
  if (selObj == null) {
    return -1;
  }

  for (i = 0; i < selObj.length; i++) {
    if (selObj.options[i].value == sValue) {
      return i;
    }
  }
}

/*----------------getLength-----------------*/
function getTextLength(sId) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return -1;
  }

  return item.length;
}

function getSelectLength(sId) {
  return getTextLength(sId);
}

function getValue(sId) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return -1;
  }

  return item.value;
}

/* Web page manipulation functions */
function setElementStyle(sId, sStyle, sVal) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return false;
  }

  if (document.getElementById) {
    // DOM3 = IE5, NS6
    eval("document.getElementById(sId).style." + sStyle + "='" + sVal + "'");
  } else {
    if (document.layers == false) {
      // IE4
      eval("document.all[sId].style." + sStyle + "='" + sVal + "'");
    } else {
      if (document.layers[sId]) {
        //NS4
        eval("document.layers[sId]." + sStyle + "='" + sVal + "'");
      } else if (document.all != null) {
        eval("document.all[sId]." + sStyle + "='" + sVal + "'");
      }
    }
  }

  return true;
}

/*start of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/
function setDisplay(sId, sh) {
  var status;
  if (sh > 0) {
    status = "";
  } else {
    status = "none";
  }

  getElement(sId).style.display = status;
}
/*end of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/

function setVisible(sId, sh) {
  var status;
  if (sh > 0) {
    status = "visible";
  } else {
    status = "hidden";
  }

  if (setElementStyle(sId, "visibility", status)) return true;
  else return false;
}

function setSelect(sId, sValue) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return false;
  }

  for (var i = 0; i < item.options.length; i++) {
    if (item.options[i].value == sValue) {
      item.selectedIndex = i;
      return true;
    }
  }

  alert("the option which value is " + sValue + " is not existed in " + sId);
  return false;
}

function htmlCharacterEscaping(str) {
  if (str.length == 0) return "";

  s = str.toString().replace(/&lt;/g, "<");
  s = s.toString().replace(/&gt;/g, ">");
  s = s.toString().replace(/&amp;/g, "&");
  s = s.toString().replace(/&quot;/g, '"');

  return s;
}

function setText(sId, sValue) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return false;
  }

  item.value = htmlCharacterEscaping(sValue);
  return true;
}

function setCheck(sId, value) {
  var item;
  item = getElById(sId);
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return false;
  }

  if (value == "1") {
    item.checked = true;
    // item.value = 1;
  } else {
    item.checked = false;
    // item.value = 0;
  }

  return true;
}

function setRadio(sId, sValue) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return false;
  }

  for (i = 0; i < item.length; i++) {
    if (item[i].value == sValue) {
      item[i].checked = true;
      return true;
    }
  }

  alert("the option which value is " + sValue + " is not existed in " + sId);
  return false;
}

function setDisable(sId, flag) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return false;
  }

  if (flag == 1 || flag == "1") {
    item.disabled = true;
  } else {
    item.disabled = false;
  }

  return true;
}

/*-----select------*/
function addOption(sId, OptionName, OptionValue, OptionText) {
  var Param = document.createElement("option");
  Param.name = OptionName;
  Param.value = OptionValue;
  Param.innerText = OptionText;

  var selItem;
  if ((selItem = getElById(sId)) != null) {
    selItem.appendChild(Param);
    return true;
  } else {
    alert(sId + " is not existed");
    return false;
  }
}

function removeOption(sId, sValue) {
  var selItem;
  if ((selItem = getElById(sId)) != null) {
    var index = getOptionIndex(sId, sValue);
    if (index >= 0) {
      selItem.removeChild(selItem.options[index]);
      return true;
    } else {
      alert("the option which value is " + sValue + " is not existed");
      return false;
    }
  }

  alert(sId + " is not existed");
  return false;
}

function removeAllOption(sId) {
  var selItem;
  if ((selItem = getElById(sId)) != null) {
    //var list =selItem.childNodes;
    //for( var i in list)
    //	{
    //	    selItem.removeChild(selItem.options[0]);
    //	}
    //alert(selItem.length)
    selItem.length = 0;
    //alert(selItem.length)
    return true;
  }

  alert(sId + " is not existed");
  return false;
}

/////////////////////////////////////////////////////
// Load / submit functions
/*
function getSelect(item)
{
	var idx;
	if (item.options.length > 0) 
	{
	    idx = item.selectedIndex;
	    return item.options[idx].value;
	}
	else 
	{
		return '';
    }
}
*/
/*
//获取List列表中有多少项被选中，返回选中的个数
function getListSelectedCount(List)
{
    //如果是多项列表
    if (List.length > 0)
    {
        var SelectedCount = 0;
        
        //统计选择个数
        for (i = 0; i < List.length; i++)
        {
            if (List[i].checked == true)
            {
                SelectedCount++;
            }
        }
        
        return SelectedCount;
    }
    //如果是单项列表
    else
    {
        if (List.checked == true)
        {
            return 1;
        }
        
        return 0;
    }
}
*/
//the functions for the internal call

/*
var unsafeString = "\"<>%\\^[]`\+\$\,'#&/";
// deleted these chars from the include list ";", "/", "?", ":", "@", "=", "&" and #
// so that we could analyze actual URLs
function isUnsafe(compareChar)
// this function checks to see if a char is URL unsafe.
// Returns bool result. True = unsafe, False = safe
{
   if ( unsafeString.indexOf(compareChar) == -1 && compareChar.charCodeAt(0) > 32
        && compareChar.charCodeAt(0) < 123 )
      return false; // found no unsafe chars, return false
   else
      return true;
}

var markStrChars = "\"'";
// Checks to see if a char is used to mark begining and ending of string.
// Returns bool result. True = special, False = not special
function isMarkStrChar(compareChar)
{
   if ( markStrChars.indexOf(compareChar) == -1 )
      return false; // found no marked string chars, return false
   else
      return true;
}*/

/*
function decToHex(num, radix)
// part of the hex-ifying functionality
{
   var hexString = "";
   while ( num >= radix ) 
   {
      temp = num % radix;
      num = Math.floor(num / radix);
      hexString += hexVals[temp];
   }
   hexString += hexVals[num];
   return reversal(hexString);
}

function reversal(s)
// part of the hex-ifying functionality
{
   var len = s.length;
   var trans = "";
   for (i = 0; i < len; i++)
      trans = trans + s.substring(len-i-1, len-i);
   s = trans;
   return s;
}
function convert(val)
// this converts a given char to url hex form
{
   return  "%" + decToHex(val.charCodeAt(0), 16);
}*/
/////////////////////////////////////////////////////
/*
/*
//no using
// use backslash in front one of the escape codes to process
// marked string characters.
// Returns new process string
function processMarkStrChars(str) 
{
   var i = 0;
   var retStr = '';

   for ( i = 0; i < str.length; i++ ) {
      if ( isMarkStrChar(str.charAt(i)) == true )
         retStr += '\\';
      retStr += str.charAt(i);
   }

   return retStr;
}
*/

////////////////////////////////////////////////////////提交
function webSubmitForm(sFormName, DomainNamePrefix) {
  /*-----------------------internal method------------------------*/
  this.setPrefix = function (Prefix) {
    if (Prefix == null) {
      this.DomainNamePrefix = ".";
    } else {
      this.DomainNamePrefix = Prefix + ".";
    }
  };

  this.getDomainName = function (sName) {
    if (this.DomainNamePrefix == ".") {
      return sName;
    } else {
      return this.DomainNamePrefix + sName;
    }
  };

  this.getNewSubmitForm = function () {
    var submitForm = document.createElement("FORM");
    document.body.appendChild(submitForm);
    submitForm.method = "POST";
    return submitForm;
  };

  /*start of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/
  this.createNewFormElement = function (elementName, elementValue) {
    var newElement = document.createElement("INPUT");
    newElement.setAttribute("name", elementName);
    newElement.setAttribute("value", elementValue);
    newElement.setAttribute("type", "hidden");
    return newElement;
  };

  /*---------------------------external method----------------------------*/
  this.addForm = function (sFormName, DomainNamePrefix) {
    this.setPrefix(DomainNamePrefix);
    var srcForm = getElement(sFormName);
    if (
      srcForm != null &&
      srcForm.length > 0 &&
      this.oForm != null &&
      srcForm.style.display != "none"
    ) {
      MakeCheckBoxValue(srcForm);

      for (i = 0; i < srcForm.elements.length; i++) {
        var type = srcForm.elements[i].type;
        if (type != "button" && srcForm.elements[i].disabled == false) {
          if (this.DomainNamePrefix != ".") {
            var ele = this.createNewFormElement(
              this.DomainNamePrefix + srcForm.elements[i].name,
              srcForm.elements[i].value
            );
            this.oForm.appendChild(ele);
          } else {
            var ele = this.createNewFormElement(
              srcForm.elements[i].name,
              srcForm.elements[i].value
            );
            this.oForm.appendChild(ele);
          }
        }
      }
    } else {
      this.status = false;
    }

    this.DomainNamePrefix = ".";
  };
  /*end of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/

  this.addDiv = function (sDivName, Prefix) {
    // this.setPrefix(DomainNamePrefix);
    if (Prefix == null) {
      Prefix = "";
    } else {
      Prefix += ".";
    }

    var srcDiv = getElement(sDivName);
    if (srcDiv == null) {
      alert(sDivName + " is not existed!");
      return;
    }
    if (srcDiv.style.display == "none") {
      return;
    }
    //alert(srcDiv)
    var eleSelect = srcDiv.getElementsByTagName("select");
    if (eleSelect != null) {
      for (k = 0; k < eleSelect.length; k++) {
        if (eleSelect[k].disabled == false) {
          this.addParameter(Prefix + eleSelect[k].name, eleSelect[k].value);
        }
      }
    }

    MakeCheckBoxValue(srcDiv);
    var eleInput = srcDiv.getElementsByTagName("input");
    if (eleInput != null) {
      for (k = 0; k < eleInput.length; k++) {
        if (eleInput[k].type != "button" && eleInput[k].disabled == false) {
          this.addParameter(Prefix + eleInput[k].name, eleInput[k].value);
        }
      }
    }
  };

  this.addParameter = function (sName, sValue) {
    //检查是否存在这个元素
    var DomainName = this.getDomainName(sName);

    for (i = 0; i < this.oForm.elements.length; i++) {
      if (this.oForm.elements[i].name == DomainName) {
        this.oForm.elements[i].value = sValue;
        this.oForm.elements[i].disabled = false;
        return;
      }
    }

    //没有发现这个元素
    if (i == this.oForm.elements.length) {
      var ele = this.createNewFormElement(DomainName, sValue);
      this.oForm.appendChild(ele);
    }
  };

  this.disableElement = function (sName) {
    var DomainName = this.getDomainName(sName);
    for (i = 0; i < this.oForm.elements.length; i++) {
      if (this.oForm.elements[i].name == DomainName) {
        this.oForm.elements[i].disabled = true;
        return;
      }
    }
  };

  this.usingPrefix = function (Prefix) {
    this.DomainNamePrefix = Prefix + ".";
  };

  this.endPrefix = function () {
    this.DomainNamePrefix = ".";
  };

  this.setMethod = function (sMethod) {
    if (sMethod.toUpperCase() == "GET") this.oForm.method = "GET";
    else this.oForm.method = "POST";
  };

  this.setAction = function (sUrl) {
    this.oForm.action = sUrl;
    var findlog = sUrl.indexOf("login");
    if (findlog == -1) {
      var temp = sUrl.lastIndexOf("/") + 1;
      top.g_url = sUrl.substr(temp);
    }
  };

  this.setTarget = function (sTarget) {
    this.oForm.target = sTarget;
  };

  this.submit = function (sURL, sMethod) {
    if (sURL != null && sURL != "") this.setAction(sURL);
    if (sMethod != null && sMethod != "") this.setMethod(sMethod);

    if (this.status == true) this.oForm.submit();
  };

  this.status = true;
  /*--------------------------------excute by internal-------------------------*/
  this.setPrefix(DomainNamePrefix);
  this.oForm = this.getNewSubmitForm();
  if (sFormName != null && sFormName != "") {
    this.addForm(sFormName, this.DomainNamePrefix);
    //this.DomainNamePrefix = '.';
  }
}

function MakeCheckBoxValue(srcForm) {
  var Inputs = srcForm.getElementsByTagName("input");
  for (var i = 0; i < Inputs.length; i++) {
    if (Inputs[i].type == "checkbox") {
      var CheckBox = getElById(Inputs[i].name);
      //alert(Inputs[i].name)
      if (CheckBox.checked == true) {
        CheckBox.value = 1;
      } else {
        CheckBox.value = 0;
      }
    } else if (Inputs[i].type == "radio") {
      var radio = getElById(Inputs[i].name);
      for (k = 0; k < radio.length; k++) {
        if (radio[k].checked == false) {
          radio[k].disabled = true;
        }
      }
    }
  }
}

function Submit(type) {
  if (CheckForm(type) == true) {
    var Form = new webSubmitForm();
    AddSubmitParam(Form, type);
    Form.submit();
  }
}

////////////////////////////////////////////////////
function FinishLoad() {
  //	alert("FinishLoad");
}

function DoUnload() {
  /*
	if (typeof(event) != 'undefined' && event != null)
    {
		if (event.clientY < 0||event.altKey)
		{//alert(2)
			//top.location.replace("/logout.cgi"); 
		}
	}
	*/
}

function DoLogout() {
  //document.cookie = 'Cookie=default;path=/';
}

//创建XMLHttp对象
function CreateXMLHttp() {
  var xmlhttp = null;
  var aVersions = [
    "MSXML2.XMLHttp.5.0",
    "MSXML2.XMLHttp.4.0",
    "MSXML2.XMLHttp.3.0",
    "MSXML2.XMLHttp",
    "Microsoft.XMLHttp",
  ];

  if (window.XMLHttpRequest) {
    try {
      xmlhttp = new XMLHttpRequest();
    } catch (e) {}
  } else {
    if (window.ActiveXObject) {
      //IE6、IE5
      for (var i = 0; i < 5; i++) {
        try {
          xmlhttp = new ActiveXObject(aVersions[i]);
          return xmlhttp;
        } catch (e) {}
      }
    }
  }

  return xmlhttp;
}

/////////////////////////////////////
function AssociateParam(dest, src, name) {
  var DestObj = eval(dest);
  var SrcObj = eval(src);
  var NameArray = name.split("|");

  for (j = 0; j < DestObj.length; j++) {
    if (DestObj[j] == null) break;
    for (i = 0; i < SrcObj.length; i++) {
      if (SrcObj[i] == null) break;
      if (DestObj[j].key.indexOf(SrcObj[i].key) > -1) {
        try {
          eval(
            dest + "[" + j + "]" + "." + "Relating" + "=" + src + "[" + i + "]"
          );
        } catch (e) {}
        for (k = 0; k < NameArray.length; k++) {
          if (NameArray[k] == "") {
            continue;
          }

          try {
            eval(
              dest +
                "[" +
                j +
                "]" +
                "." +
                NameArray[k] +
                "=" +
                src +
                "[" +
                i +
                "]" +
                "." +
                NameArray[k]
            );
          } catch (e) {}
        }
        break;
      }
    }
  }
}

function getBoolValue(param) {
  var value = parseInt(param);
  if (isNaN(value) == true) {
    var LowerParam = param.toLowerCase();
    if (LowerParam == "enable") {
      return 1;
    } else {
      return 0;
    }
  } else {
    return value;
  }
}

function getCheckVal(sId) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return -1;
  }
  if (item.checked == true) {
    return 1;
  } else {
    return 0;
  }
}

function getRadioVal(sId) {
  var item;
  if (null == (item = getElById(sId))) {
    alert(sId + " is not existed");
    return -1;
  }
  for (i = 0; i < item.length; i++) {
    //alert(item[i].checked)
    if (item[i].checked == true) {
      return item[i].value;
    }
  }

  return -1;
}

function getSelectVal(sId) {
  return getValue(sId);
}

/*start of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/
function getDisplayText(val, lineLength) {
  if (lineLength == null) lineLength = 20;
  var content = "";
  var index = 0;
  var len = val.length;

  while (len > lineLength) {
    content += val.substr(index, lineLength) + "<br>";
    len -= lineLength;
    index += lineLength;
  }
  content += val.substr(index);

  return content;
}
/*end of HGW 2008.1.10 For A36D04370 FireFox 显示 V100R001C02B013 by w00104696*/

//IPv6
function ParseIpv6Array(str) {
  var Num;
  var i, j;
  var finalAddrArray = new Array();
  var falseAddrArray = new Array();

  var addrArray = str.split(":");
  Num = addrArray.length;
  if (Num > 8) {
    return falseAddrArray;
  }

  for (i = 0; i < Num; i++) {
    if (addrArray[i].length > 4 || addrArray[i].length < 1) {
      return falseAddrArray;
    }
    for (j = 0; j < addrArray[i].length; j++) {
      if (
        addrArray[i].charAt(j) < "0" ||
        addrArray[i].charAt(j) > "f" ||
        (addrArray[i].charAt(j) > "9" && addrArray[i].charAt(j) < "a")
      ) {
        return falseAddrArray;
      }
    }

    finalAddrArray[i] = "";
    for (j = 0; j < 4 - addrArray[i].length; j++) {
      finalAddrArray[i] += "0";
    }
    finalAddrArray[i] += addrArray[i];
  }

  return finalAddrArray;
}

function getFullIpv6Address(address) {
  var c = "";
  var i = 0,
    j = 0,
    k = 0,
    n = 0;
  var startAddress = new Array();
  var endAddress = new Array();
  var finalAddress = "";
  var startNum = 0;
  var endNum = 0;
  var lowerAddress;
  var totalNum = 0;

  lowerAddress = address.toLowerCase();

  var addrParts = lowerAddress.split("::");
  if (addrParts.length == 2) {
    if (addrParts[0] != "") {
      startAddress = ParseIpv6Array(addrParts[0]);
      if (startAddress.length == 0) {
        return "";
      }
    }
    if (addrParts[1] != "") {
      endAddress = ParseIpv6Array(addrParts[1]);
      if (endAddress.length == 0) {
        return "";
      }
    }

    if (startAddress.length + endAddress.length >= 8) {
      return "";
    }
  } else if (addrParts.length == 1) {
    startAddress = ParseIpv6Array(addrParts[0]);
    if (startAddress.length != 8) {
      return "";
    }
  } else {
    return "";
  }

  for (i = 0; i < startAddress.length; i++) {
    finalAddress += startAddress[i];
    if (i != 7) {
      finalAddress += ":";
    }
  }
  for (; i < 8 - endAddress.length; i++) {
    finalAddress += "0000";
    if (i != 7) {
      finalAddress += ":";
    }
  }
  for (; i < 8; i++) {
    finalAddress += endAddress[i - (8 - endAddress.length)];
    if (i != 7) {
      finalAddress += ":";
    }
  }

  return finalAddress;
}

function isIpv6Address(address) {
  if (getFullIpv6Address(address) == "") {
    return false;
  }

  return true;
}

function isUnicastIpv6Address(address) {
  var tempAddress = getFullIpv6Address(address);

  if (
    tempAddress == "" ||
    tempAddress == "0000:0000:0000:0000:0000:0000:0000:0000" ||
    tempAddress == "0000:0000:0000:0000:0000:0000:0000:0001" ||
    tempAddress.substring(0, 2) == "ff"
  ) {
    return false;
  }

  return true;
}

function isGlobalIpv6Address(address) {
  var tempAddress = getFullIpv6Address(address);

  if (
    tempAddress == "" ||
    tempAddress == "0000:0000:0000:0000:0000:0000:0000:0000" ||
    tempAddress == "0000:0000:0000:0000:0000:0000:0000:0001" ||
    tempAddress.substring(0, 3) == "fe8" ||
    tempAddress.substring(0, 3) == "fe9" ||
    tempAddress.substring(0, 3) == "fea" ||
    tempAddress.substring(0, 3) == "feb" ||
    tempAddress.substring(0, 2) == "ff" ||
    tempAddress.substring(0, 4) == "fecc"
  ) {
    return false;
  }

  return true;
}

/* 判断两个地址是否相等，如果不相等或者地址有误返回false，否则返回true
 * 本函数依赖于 getFullIpv6Address
 */
function CompareTwoAddress(addr1, plen1, addr2, plen2) {
  var x = 0;
  var j = 0;
  var i = 0;

  var addr1Tmp = getFullIpv6Address(addr1);
  var addr2Tmp = getFullIpv6Address(addr2);

  if (addr1Tmp == "" || addr2Tmp == "") {
    return false;
  }

  /* 将地址转换为8个数组每一个存放的是16bit的字符 */
  var addr1Comp = addr1Tmp.split(":");
  var addr2Comp = addr2Tmp.split(":");

  //alert('addr1: ' + addr1Comp + ' plen1: ' + plen1
  //	+ ' addr2: ' + addr2Comp + ' plen2: ' + plen2);

  if (plen1 != plen2) {
    return false;
  }

  x = plen1 / 16;
  /* 将x向整数靠拢 */
  for (i = 0; i < 8; i++) {
    if (i <= x && i + 1 >= x) {
      x = i;
      break;
    }
  }

  /* 先比较可以整除16bit的字符串部分 */
  for (i = 0; i < x; i++) {
    if (addr1Comp[i] != addr2Comp[i]) {
      return false;
    }
  }

  j = plen1 % 16;
  if (0 == j) {
    /* 如果前缀是16的整数倍，那么两地址匹配 */
    return true;
  }

  //alert('addr ' + x + ' ' + addr1Comp[x] + ' ' + addr2Comp[x] + ' j ' + j);

  /* 小于16bit的则转换为数字形式比较 */
  x1 = parseHex(addr1Comp[x], 16);
  x2 = parseHex(addr2Comp[x], 16);

  if ((x1 ^ x2) >= 1 << (16 - j)) {
    return false;
  }

  return true;
}

function cmpIpv6Address(minAddr, maxAddr) {
  var fullMinAddr = getFullIpv6Address(minAddr);
  var fullMaxAddr = getFullIpv6Address(maxAddr);

  var minParts = fullMinAddr.split(":");
  var maxParts = fullMaxAddr.split(":");

  var retVal = false;

  if (minParts.length != 8 || maxParts.length != 8) {
    return retVal;
  }

  for (var i = 0; i < 8; i++) {
    if (minParts[i] > maxParts[i]) {
      retVal = false;
      break;
    } else if (minParts[i] < maxParts[i]) {
      retVal = true;
      break;
    }
  }

  if (i == 8) {
    retVal = true;
  }

  return retVal;
}
function RefreshPage() {
  location.href = document.location.href;
}

function isValidCfgStr(cfgName, val, len) {
  if (isValidAscii(val) != "") {
    alert(cfgName + ' has invalid character "' + isValidAscii(val) + '".');
    return false;
  }
  if (val.length > len) {
    alert(cfgName + " has up to " + len + " characters.");
    return false;
  }
}

function isSafeStringExc(compareStr, UnsafeStr) {
  for (var i = 0; i < compareStr.length; i++) {
    var c = compareStr.charAt(i);
    if (isValidAscii(c) != "") {
      return false;
    } else {
      if (UnsafeStr.indexOf(c) > -1) {
        return false;
      }
    }
  }
  return true;
}

function isValidCfgInteger(cfgName, val, start, end) {
  if (isInteger(val) == false) {
    alert(cfgName + " is invalid, it must be digist.");
    return false;
  }
  var temp = parseInt(val);
  if (temp < start || temp > end) {
    alert(
      cfgName +
        " must be greater than " +
        start.toString() +
        " and less than " +
        end.toString() +
        "."
    );
    return false;
  }
}

//将subnet地址转换为十进制整数
function SubnetAddress2DecNum(address) {
  if (isValidSubnetMask(address) == false) {
    return -1;
  }
  var addrParts = address.split(".");
  var num = 0;
  for (i = 0; i < 4; i++) {
    num += parseInt(addrParts[i]) * Math.pow(256, 3 - i);
  }
  return num;
}

function getDivInnerId(divID) {
  var nameStartPos = -1;
  var nameEndPos = -1;
  var ele;

  divHTML = getElement(divID).innerHTML;
  nameStartPos = divHTML.indexOf("name=");
  nameEndPos = divHTML.indexOf(" ", nameStartPos);
  if (nameEndPos <= 0) {
    nameEndPos = divHTML.indexOf(">", nameStartPos);
  }

  try {
    ele = eval(divHTML.substring(nameStartPos + 3, nameEndPos));
  } catch (e) {
    ele = divHTML.substring(nameStartPos + 3, nameEndPos);
  }
  return ele;
}

function toBreakWord(val, lineLength) {
  var content = "";
  var index = 0;
  var len = val.length;

  while (len > lineLength) {
    content += val.substr(index, lineLength) + "<br>";
    len -= lineLength;
    index += lineLength;
  }
  content += val.substr(index);

  return content;
}

function isMaskOf24BitOrMore(mask) {
  var i = 0,
    num = 0;
  if (false == isValidSubnetMask(mask)) {
    return false;
  }
  var maskParts = mask.split(".");
  for (i = 0; i < 3; i++) {
    num = parseInt(maskParts[i]);
    if (num != 255) return false;
  }
  return true;
}

function ipInSubnet(ip, subnetStart, subnetEnd) {
  var ipDec;
  var subnetStartDec;
  var subnetEndDec;

  ipDec = IpAddress2DecNum(ip);
  /* BEGIN: Added by c00147909, 2009/2/6  PN: AI8D02757*/
  subnetStartDec = SubnetAddress2DecNum(subnetStart);
  subnetEndDec = SubnetAddress2DecNum(subnetEnd);
  /* END:   Added by c00147909, 2009/2/6 */
  if (ipDec >= subnetStartDec && ipDec <= subnetEndDec) {
    return true;
  }

  return false;
}
function netmaskIsContinue(Mask) {
  var ulmask;
  var i;
  var ulTmp = 0xffffffff;
  /* BEGIN: Added by c00147909, 2009/2/6  PN: AI8D02757 */
  ulmask = SubnetAddress2DecNum(Mask);
  /* END:   Added by c00147909, 2009/2/6 */
  for (i = 0; i < 32; i++) {
    if (ulTmp == ulmask) {
      return 0;
    }

    ulTmp <<= 1;
  }

  return 1;
}

function getmaskLength(Mask) {
  var ulTmp;
  var ulCount = 0;
  var ulmask;
  ulTmp = IP_NetmaskIsContinue(Mask);
  /* BEGIN: Added by c00147909, 2009/2/6  PN: AI8D02757 */
  ulmask = SubnetAddress2DecNum(Mask);
  /* END:   Added by c00147909, 2009/2/6 */
  if (ulTmp) {
    return 0; /* 掩码不连续 */
  }

  while (ulmask != 0) {
    ulmask = ulmask << 1;
    ulCount++;
  }
  return ulCount;
}

function removeSpaceTrim(inputStr) {
  var inputStrTemp;
  var i,
    j = 0;

  if (inputStr == "") {
    return "";
  }

  for (i = 0; i < inputStr.length; i++) {
    if (inputStr.charAt(i) == " ") {
      continue;
    } else {
      break;
    }
  }

  inputStrTemp = inputStr.substr(i, inputStr.length - i);

  if (inputStrTemp == "") {
    return "";
  }

  for (i = inputStrTemp.length - 1; i >= 0; i--) {
    if (inputStrTemp.charAt(i) == " ") {
      j++;
      continue;
    } else {
      break;
    }
  }

  inputStrTemp = inputStrTemp.substr(0, inputStrTemp.length - j);

  return inputStrTemp;
}

// JavaScript Document
function writeFile(str) {
  var fso, ctf;
  try {
    if (window.ActiveXObject) {
      fso = new ActiveXObject("Scripting.FileSystemObject");
      ctf = fso.CreateTextFile("c:\\test.txt", true);
      ctf.Write(str);
      ctf.Close();
    }
  } catch (e) {}
}

function selectLine(id) {
  var objTR = getElement(id);

  if (objTR != null) {
    var temp = objTR.id.split("_")[1];
    if (temp == "null") {
      setControl(-1);
      setLineHighLight(objTR);
    } else if (temp == "no") {
      setControl(-2);
    } else {
      var index = parseInt(temp);
      setControl(index);
      setLineHighLight(objTR);
    }
  }
}

function clickAdd(tabTitle) {
  var tab = document.getElementById(tabTitle).getElementsByTagName("table");

  var row, col;
  var rowLen = tab[0].rows.length;
  var firstRow = tab[0].rows[0];
  var lastRow = tab[0].rows[rowLen - 1];

  if (lastRow.id == "record_null") {
    selectLine("record_null");
    return;
  } else if (lastRow.id == "record_no") {
    tab[0].deleteRow(rowLen - 1);
    rowLen = tab[0].rows.length;
  }

  row = tab[0].insertRow(rowLen);

  var appName = navigator.appName;
  if (appName == "Microsoft Internet Explorer") {
    g_browserVersion = 1; /* IE */
    row.className = "trTabContent";
    row.id = "record_null";
    row.attachEvent("onclick", function () {
      selectLine("record_null");
    });
  } else {
    g_browserVersion = 2; /* firefox */
    row.setAttribute("class", "trTabContent");
    row.setAttribute("id", "record_null");
    row.setAttribute("onclick", "selectLine(this.id);");
  }

  for (var i = 0; i < firstRow.cells.length; i++) {
    col = row.insertCell(i);
    col.innerHTML = "----";
  }
  selectLine("record_null");
}

function addNullInst(tabTitle) {
  var tab = document.getElementById(tabTitle).getElementsByTagName("table");
  var row, col;
  var rowLen = tab[0].rows.length;
  var firstRow = tab[0].rows[0];
  var lastRow = tab[0].rows[rowLen - 1];

  tab[0].deleteRow(rowLen - 1);
  rowLen = tab[0].rows.length;
  row = tab[0].insertRow(rowLen);

  var appName = navigator.appName;
  if (appName == "Microsoft Internet Explorer") {
    g_browserVersion = 1; /* IE */
    row.className = "trTabContent";
    row.id = "record_no";
    row.attachEvent("onclick", function () {
      selectLine("record_no");
    });
  } else {
    g_browserVersion = 2; /* firefox */
    row.setAttribute("class", "trTabContent");
    row.setAttribute("id", "record_no");
    row.setAttribute("onclick", "selectLine(this.id);");
  }

  for (var i = 0; i < firstRow.cells.length; i++) {
    col = row.insertCell(i);
    col.innerHTML = "----";
  }
  selectLine("record_no");
}

function removeInst(url) {
  var rml = getElement("rml");
  if (rml == null) return;

  var SubmitForm = new webSubmitForm();
  var cnt = 0;
  with (document.forms[0]) {
    if (rml.length > 0) {
      for (var i = 0; i < rml.length; i++) {
        if (rml[i].checked == true) {
          SubmitForm.addParameter(rml[i].value, "");
          cnt++;
        }
      }
    } else if (rml.checked == true) {
      SubmitForm.addParameter(rml.value, "");
      cnt++;
    }
  }

  SubmitForm.setAction("del.cgi?RequestFile=" + url);
  SubmitForm.submit();
}

function writeTabHeader(tabTitle, width, titleWidth, type) {
  var labelNew = "新建";

  if (tabTitle == "Wan Connection") {
    labelNew = "新建";
  }

  if (width == null) width = "70%";

  if (titleWidth == null) titleWidth = "120";

  var html =
    '<table width="' +
    width +
    '" border="0" cellpadding="0" cellspacing="0">' +
    "<tr>" +
    "<td>" +
    '<table width="100%" border="0" cellpadding="0" cellspacing="0">' +
    "<tr>" +
    ' <td width="7" height="22"> </td>' +
    '<td valign="bottom" align="center" width="' +
    titleWidth +
    '" >' +
    "</td>" +
    '<td width="7"></td>' +
    '<td align="right">' +
    '<table border="0" cellpadding="1" cellspacing="0">' +
    "<tr>";

  if ("info" == type) {
  } else if ("cfg" == type) {
    html +=
      '<td><input id = "newWanBtnID" class="submit" type="button" value="' +
      labelNew +
      '" ' +
      "onclick=\"clickAdd('" +
      tabTitle +
      "');\"></td>" +
      '<td><input id="removeWanBtnID" class="submit" type="button" value="删除" ' +
      "onclick=\"clickRemove('" +
      tabTitle +
      "');\"></td>" +
      '<td width="3"></td>';
  }

  html +=
    "</tr>" +
    "</table>" +
    "</td>" +
    "</tr>" +
    "</table>" +
    "</td>" +
    "</tr>" +
    "<tr>" +
    '<td id="' +
    tabTitle +
    '">';

  document.write(html);
}

function writeTabInfoHeader(tabTitle, tabWidth, titleWidth) {
  writeTabHeader(tabTitle, tabWidth, titleWidth, "info");
}

function writeTabCfgHeader(tabTitle, tabWidth, titleWidth) {
  writeTabHeader(tabTitle, tabWidth, titleWidth, "cfg");
}

function writeTabTail() {
  document.write("</td></tr></table>");
}

var previousTR = null;
function setLineHighLight(objTR) {
  if (previousTR != null) {
    previousTR.style.backgroundColor = "#f4f4f4";
    for (var i = 0; i < previousTR.cells.length; i++) {
      previousTR.cells[i].style.color = "#000000";
    }
  }

  objTR.style.backgroundColor = "#D1D1D1";
  for (var i = 0; i < objTR.cells.length; i++) {
    objTR.cells[i].style.color = "#000000";
  }
  previousTR = objTR;
}

function WanNameSort(a, b) {
  var a_dig = a.IfaceName.split("_");
  var b_dig = b.IfaceName.split("_");
  var a_v = 0,
    b_v = 0;

  if (a_dig.length < 1 || b_dig.length < 1) return -1;

  if (isPlusInteger(a_dig[0])) a_v = parseInt(a_dig[0]);

  if (isPlusInteger(b_dig[0])) b_v = parseInt(b_dig[0]);

  return a_v - b_v;
}

function SortObject(IfaceName, RecordIdx) {
  this.IfaceName = IfaceName;
  this.RecordIdx = RecordIdx;
}

function SortWanNameInterface() {
  this.SortObjList = null;
  this.SortObjLen = 0;
  this.Repflag = 0;
  this.SetReplaceStrflag = SetReplaceStrflag;
  this.UpdateWanIFName = UpdateWanIFName;
  this.SortMyArray = SortMyArray;

  function SetReplaceStrflag(flag) {
    this.Repflag = flag;
  }

  function UpdateWanIFName(sortArray, len) {
    var i = 0;
    this.SortObjList = new Array(len);
    this.SortObjLen = len;

    for (i = 0; i < len; i++) {
      this.SortObjList[i] = new SortObject(sortArray[i], i);
    }
    this.SortObjList.sort(WanNameSort);

    return this.SortMyArray(sortArray);
  }

  function SortMyArray(myArray) {
    var oldArray = myArray;
    var i = 0;
    var arrLen = this.SortObjLen;
    var newArray = new Array(arrLen);

    for (i = 0; i < arrLen; i++) {
      newArray[i] = oldArray[this.SortObjList[i].RecordIdx];
      if (this.Repflag && null != newArray[i]) {
        newArray[i] = newArray[i].replace(/N\/A/g, "-");
        if (newArray[i] == "") newArray[i] = "-";
      }
    }

    return newArray;
  }
}

var SortUtil = new SortWanNameInterface();

function GetQueryString(name) {
  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
  var r = window.location.search.substr(1).match(reg);
  if (r != null) return unescape(r[2]);
  return null;
}

function checkVoipIdle() {
  var voipIdle = 1;

  $.ajaxSetup({
    async: false,
  });

  $.getJSON("/cgi-bin/getvoipidle.asp", function (data, status) {
    voipIdle = data.voipIdle;
  });

  if (voipIdle == 0) {
    alert(
      "During a broadband phone call, you cannot save it.Please save it after the call ends"
    );
    return false;
  }

  return true;
}

var login_check_addr = "/cgi-bin/check_auth.json"; ////////////////

function crc32(str) {
  var table =
    "00000000 77073096 EE0E612C 990951BA 076DC419 706AF48F E963A535 9E6495A3 0EDB8832 79DCB8A4 E0D5E91E 97D2D988 09B64C2B 7EB17CBD E7B82D07 90BF1D91 1DB71064 6AB020F2 F3B97148 84BE41DE 1ADAD47D 6DDDE4EB F4D4B551 83D385C7 136C9856 646BA8C0 FD62F97A 8A65C9EC 14015C4F 63066CD9 FA0F3D63 8D080DF5 3B6E20C8 4C69105E D56041E4 A2677172 3C03E4D1 4B04D447 D20D85FD A50AB56B 35B5A8FA 42B2986C DBBBC9D6 ACBCF940 32D86CE3 45DF5C75 DCD60DCF ABD13D59 26D930AC 51DE003A C8D75180 BFD06116 21B4F4B5 56B3C423 CFBA9599 B8BDA50F 2802B89E 5F058808 C60CD9B2 B10BE924 2F6F7C87 58684C11 C1611DAB B6662D3D 76DC4190 01DB7106 98D220BC EFD5102A 71B18589 06B6B51F 9FBFE4A5 E8B8D433 7807C9A2 0F00F934 9609A88E E10E9818 7F6A0DBB 086D3D2D 91646C97 E6635C01 6B6B51F4 1C6C6162 856530D8 F262004E 6C0695ED 1B01A57B 8208F4C1 F50FC457 65B0D9C6 12B7E950 8BBEB8EA FCB9887C 62DD1DDF 15DA2D49 8CD37CF3 FBD44C65 4DB26158 3AB551CE A3BC0074 D4BB30E2 4ADFA541 3DD895D7 A4D1C46D D3D6F4FB 4369E96A 346ED9FC AD678846 DA60B8D0 44042D73 33031DE5 AA0A4C5F DD0D7CC9 5005713C 270241AA BE0B1010 C90C2086 5768B525 206F85B3 B966D409 CE61E49F 5EDEF90E 29D9C998 B0D09822 C7D7A8B4 59B33D17 2EB40D81 B7BD5C3B C0BA6CAD EDB88320 9ABFB3B6 03B6E20C 74B1D29A EAD54739 9DD277AF 04DB2615 73DC1683 E3630B12 94643B84 0D6D6A3E 7A6A5AA8 E40ECF0B 9309FF9D 0A00AE27 7D079EB1 F00F9344 8708A3D2 1E01F268 6906C2FE F762575D 806567CB 196C3671 6E6B06E7 FED41B76 89D32BE0 10DA7A5A 67DD4ACC F9B9DF6F 8EBEEFF9 17B7BE43 60B08ED5 D6D6A3E8 A1D1937E 38D8C2C4 4FDFF252 D1BB67F1 A6BC5767 3FB506DD 48B2364B D80D2BDA AF0A1B4C 36034AF6 41047A60 DF60EFC3 A867DF55 316E8EEF 4669BE79 CB61B38C BC66831A 256FD2A0 5268E236 CC0C7795 BB0B4703 220216B9 5505262F C5BA3BBE B2BD0B28 2BB45A92 5CB36A04 C2D7FFA7 B5D0CF31 2CD99E8B 5BDEAE1D 9B64C2B0 EC63F226 756AA39C 026D930A 9C0906A9 EB0E363F 72076785 05005713 95BF4A82 E2B87A14 7BB12BAE 0CB61B38 92D28E9B E5D5BE0D 7CDCEFB7 0BDBDF21 86D3D2D4 F1D4E242 68DDB3F8 1FDA836E 81BE16CD F6B9265B 6FB077E1 18B74777 88085AE6 FF0F6A70 66063BCA 11010B5C 8F659EFF F862AE69 616BFFD3 166CCF45 A00AE278 D70DD2EE 4E048354 3903B3C2 A7672661 D06016F7 4969474D 3E6E77DB AED16A4A D9D65ADC 40DF0B66 37D83BF0 A9BCAE53 DEBB9EC5 47B2CF7F 30B5FFE9 BDBDF21C CABAC28A 53B39330 24B4A3A6 BAD03605 CDD70693 54DE5729 23D967BF B3667A2E C4614AB8 5D681B02 2A6F2B94 B40BBE37 C30C8EA1 5A05DF1B 2D02EF8D";
  var crc = 0;
  var n = 0,
    x = 0;
  crc = crc ^ 0xffffffff;

  for (var i = 0, iTop = str.length; i < iTop; i++) {
    n = (crc ^ str.charCodeAt(i)) & 0xff;
    x = "0x" + table.substr(n * 9, 8);
    crc = (crc >>> 8) ^ x;
  }
  return (crc ^ 0xffffffff) >>> 0;
}

function setEBooValueCookie(formObj) {
  var $fo = $(formObj);

  var i = 0;
  var post_str = "";
  var pname = new Array();
  var pvalue = new Array();
  var t = $fo.serializeArray();
  /*console.log(t);*/
  $.each(t, function () {
    for (i = 0; i <= pname.length; i++) {
      if (pname[i] == this.name) break;
    }

    if (i > pname.length) {
      pname[i - 1] = this.name;
      pvalue[i - 1] = this.value;
    } else {
      pvalue[i] += "\n" + this.value;
    }
  });

  if (0 == pname.length) {
    document.cookie = "EBOOVALUE=ecntBaorga";
    return false;
  } else {
    for (i = 0; i < pname.length; i++) {
      post_str += pname[i] + pvalue[i];
    }
  }

  /*console.log('post_str==>[' + post_str +']');*/
  if ("" == post_str) {
    document.cookie = "EBOOVALUE=ecntBaorga";
    return false;
  }
  var cookie_crc = crc32(post_str).toString(16);
  /*console.log('cookie_crc==>[' + cookie_crc +']');*/
  document.cookie = "EBOOVALUE=" + cookie_crc;
  return true;
}

function resetEBooValueCookie() {
  document.cookie = "EBOOVALUE=ecntBaorga";
  return;
}
