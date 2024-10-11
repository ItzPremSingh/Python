import "jquery.js";
import "util.js";

if (self != top) top.location.href = "/cgi-bin/login.asp";
function getsec(str) {
  var str1 = str.substring(1, str.length) * 1;
  var str2 = str.substring(0, 1);
  if (str2 == "s") {
    return str1 * 1000;
  } else if (str2 == "h") {
    return str1 * 60 * 60 * 1000;
  } else if (str2 == "d") {
    return str1 * 24 * 60 * 60 * 1000;
  }
}
function refreshself() {
  top.window.location.href = "/cgi-bin/login.asp";
}

function GET_C(Name) {
  var search = Name + "=";
  if (document.cookie.length > 0) {
    offset = document.cookie.indexOf(search);
    if (offset != -1) {
      offset += search.length;
      end = document.cookie.indexOf(";", offset);
      if (end == -1) end = document.cookie.length;
      return unescape(document.cookie.substring(offset, end));
    } else return "";
  } else return "";
}

function SET_C_T(name, value, time) {
  var strsec = getsec(time);
  var exp = new Date();
  exp.setTime(exp.getTime() + strsec * 1);
  document.cookie =
    name + "=" + escape(value) + ";expires=" + exp.toGMTString() + ";path=/;";
}

function SET_C(name, value) {
  document.cookie = name + "=" + escape(value) + ";path=/;";
}

function DEL_C(name) {
  var exp = new Date();
  exp.setTime(exp.getTime() - 10000);
  document.cookie = name + "=del;expires=" + exp.toGMTString();
  document.cookie = name + "=del;expires=" + exp.toGMTString() + ";path=/;";
}

function onHandleKeyDown(e) {
  var key = 0;
  if (window.event) {
    key = window.event.keyCode;
  } else if (e) {
    key = e.which;
  }
  if (key == 13 && document.activeElement.id != "loginbutton") {
    doLogin();
  }
}
document.onkeypress = onHandleKeyDown;

var loginTimes = 0;

function doLogin() {
  var Captchastr = document.getElementById("ValidateCode");
  var Captchaimg = document.getElementById("captchaimg").src;
  var Captchaurl = document.getElementById("Captcha_url");
  var captcha = "";
  var captchaIndx = "";
  /* check empty */
  if (0 == $("#username").val().length) {
    alert("Username cannot be null");
    return false;
  }

  if (0 == $("#password").val().length) {
    alert("Password cannot be null");
    return false;
  }

  if (Captchastr.value == "") {
    alert("ValidateCode cannot be null");
    return false;
  }
  // captha_4.gif
  captcha = Captchaimg.split("_"); // [captha, 4.gif]
  captchaIndx = captcha[1].split("."); // [4, gif]
  Captchaurl.value = captchaIndx[0]; // 4

  if (GET_C("loginTimes") != "" && typeof GET_C("loginTimes") != "undefined")
    loginTimes = parseInt(GET_C("loginTimes"));
  if (loginTimes >= 3) {
    $("#errmsg").text(
      "Login three times fail, Webpage locked,please login after 1 minute!"
    );
    return false;
  }
  SET_C_T("loginTimes", loginTimes, "s60");
  var form = $("#loginui");
  $.ajax({
    url: login_check_addr,
    type: form.attr("method"),
    data: form.serialize(),
    dataType: "json",
    beforeSend: function () {
      $("#loginbutton").attr("disabled", true);
    },
    error: function () {
      $("#loginbutton").attr("disabled", false);
      alert("fetal error!");
    },
    complete: function () {
      $("#loginbutton").attr("disabled", false);
    },
    success: function (result) {
      if ("1" == result.Locked) {
        $("#errmsg").text(
          "Login three times fail, Webpage locked,please login after 1 minute!"
        );
        loginTimes = 0;
        DEL_C("loginTimes");
      } else if ("1" == result.Logged) {
        $("#errmsg").text("Admistrator account is login!");
        loginTimes = 0;
        DEL_C("loginTimes");
      } else if ("2" == result.Logged) {
        $("#errmsg").text("User account is already login!");
        loginTimes = 0;
        DEL_C("loginTimes");
      } else if ("2" == result.CaptchaOK) {
        $("#errmsg").text("ValidateCode Error");
      } else if ("0" == result.Privilege) {
        loginTimes += 1;
        SET_C_T("loginTimes", loginTimes, "s60");
        $("#errmsg").text(
          "You already login incorrectly for " + loginTimes + " time!"
        );
      } else if ("1" == result.Privilege || "2" == result.Privilege) {
        loginTimes = 0;
        DEL_C("loginTimes");
        SET_C("ecntToken", result.ecntToken);
        top.location.href = "/cgi-bin/content.asp";
      }
    },
  });
}

function LoadFrame() {
  $("#username").val("admin");
  $("#username").focus();
}

function LanguageSelect() {
  var vForm = document.loginui;
  vForm.selectLanguage.value = "English";
  switch (vForm.selectLanguage.value) {
    case "Chinese":
      vForm.Language_Flag.value = "1";
      break;

    case "English":
      vForm.Language_Flag.value = "2";
      break;

    default:
      vForm.Language_Flag.value = "2";
      break;
  }

  document.loginui.submit();
}
