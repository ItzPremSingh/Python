"use strict";

function getCurrentSettings() {
    const [settingType, settingName] = document.getElementById('settingType').value.split(':');
    const settingInput = document.getElementById('settingInput');
    return { settingType, settingName, settingInput };
}

function changeSettingType() {
    const { settingType, settingName, settingInput } = getCurrentSettings();
    settingInput.type = settingType;
    settingInput.value = localStorage.getItem(settingName);
}

function saveSettings() {
    const { settingType, settingName, settingInput } = getCurrentSettings();
    localStorage.setItem(settingName, settingInput.value);
    console.log(settingName);
    console.log(settingInput.value);
    alert('Settings saved successfully!');
}

function resetSettings() {
    localStorage.clear();
    alert('All settings reset!');
}

changeSettingType();
